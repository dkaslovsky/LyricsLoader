from typing import Dict, List, Optional, Union

import requests
from bs4 import BeautifulSoup


class LyricsLoader:

    def __init__(self, artist: str, suppress_errs: bool = False) -> None:
        """
        :param artist: name of artist
        :param suppress_errs: whether to suppress LyricsLoaderException if artist/album/track not found
        """
        self.artist = artist
        self.suppress_errs = suppress_errs

        self._album_to_tracks = self._query_artist()
    
    def _check_result(self, result: Union[List[str], str], category: str, name: str) -> None:
        """
        Raise exception on empty result
        :param result: data structure to check if empty
        :param category: category of object that is potentially empty (artist/album/track)
        :param name: specific name that was not found if empty
        """
        if self.suppress_errs:
            return
        if not result:
            raise LyricsLoaderError(category, name)
    
    def _query_artist(self) -> Dict[str, List[str]]:
        """
        Get artist's albums and tracks from lyrics.wikia.com API
        """
        _artist = self.artist.replace(' ', '_')
        url = f'http://lyrics.wikia.com/api.php?action=lyrics&artist={_artist}&fmt=json'
        resp = requests.get(url)
        jresp = resp.json()
        self._check_result(jresp['albums'], 'artist', self.artist)
        return {album['album']: album['songs'] for album in jresp['albums']}

    @property
    def albums(self) -> List[str]:
        """
        Return list of album names
        """
        # no need to check results since _query_artist would have raised
        return list(self._album_to_tracks.keys())
    
    def get_tracks(self, album: str) -> List[str]:
        """
        Return list of tracks on album
        :param album: name of album
        """
        tracks = self._album_to_tracks.get(album, [])
        self._check_result(tracks, 'album', album)
        return tracks

    def get_lyrics(self, track: str) -> Optional[str]:
        """
        Return track lyrics
        :param track: name of track
        """
        _track = track.replace(' ', '_')
        url = f'http://lyrics.wikia.com/{self.artist}:{_track}'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        lyrics = soup.find("div", {'class': 'lyricbox'})
        if lyrics is None:
            return self._check_result(lyrics, 'track', track)

        # remove unecessary tags
        for tag in ['div', 'i', 'b', 'a']:
            for match in lyrics.findAll(tag):
                match.unwrap()

        # remove non unicode characters, replace <br> with newlines
        lyrics = (
            str(lyrics)
            .encode('utf-8', errors='replace')[22:-6:]
            .decode('utf-8')
            .replace('\n', '')
            .replace('<br/>', '\n')
        )
        return lyrics


class LyricsLoaderError(Exception):

    def __init__(self, category: str, name: str):
        """
        :param category: category of object not found (artist/album/track)
        :param name: specific name of object not found
        """
        self.category = category
        self.name = name

    def __str__(self):
        return f'{self.category} \"{self.name}\" not found'
