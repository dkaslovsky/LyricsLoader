# LyricsLoader
LyricsLoader provides a small class for scraping song lyrics from [LyricWiki](https://lyrics.fandom.com/wiki/LyricWiki).

Usage is as follows:
```
>>> from lyricsloader import LyricsLoader

>>> loader = LyricsLoader('Pearl Jam')

>>> loader.albums
['Ten', 'Vs.', 'Vitalogy', 'No Code', 'Yield', 'Binaural', 'Riot Act', 'Lost Dogs', 'Live At Benaroya Hall', 'Rearviewmirror: Greatest Hits 1991-2003', 'Live At Easy Street', 'Pearl Jam', 'Live At The Gorge 05/06', 'Backspacer', 'Lightning Bolt', 'Songs on Singles', 'Live Songs', 'Other Releases', 'Unknown', 'Other Songs']

>>> loader.get_tracks('Vitalogy')
['Last Exit', 'Spin The Black Circle', 'Not For You', 'Tremor Christ', 'Nothingman', 'Whipping', 'Pry, To', 'Corduroy', 'Bugs', "Satan's Bed", 'Better Man', 'Aye Davanita', 'Immortality', "Hey Foxymophandlemama, That's Me"]

>>> lyrics = loader.get_lyrics('Whipping')
>>> print(lyrics)
Don't need a helmet, got a hard, hard head
Don't need a raincoat, I'm already wet
Don't need a bandage, there's too much blood
After a while, seems to roll right off

They're whipping
They're whipping
They're whipping
They're whipping

Don't need a hand, there's always arms attached
I don't get behind, I can't fall back
Why must we trust all these rusted rails?
They don't want no change we already have

They're whipping
They're whipping
They're whipping
They're whipping

Don't mean to push, but I'm being shoved
I'm just like you, think we've had enough
I can't believe a thing they want us to
We all got scars, they should have them, too

They're whipping
They're whipping
They're whipping
They're whipping

They're whipping
They're whipping
They're whipping
They're whipping
```
Hopefully I have not violated any copyright laws by displaying this output.  If I have, my sincerest apologies to Eddie, Jeff, Stone, Mike, and Matt.

A `LyricsLoaderError` is raised if an artist/album/track is not found.  To suppress this exception and instead return empty objects, pass `suppress_errs=True` to the constructor.  This exception can be imported for try/except logic:
```
>>> from lyricsloader import LyricsLoader, LyricsLoaderError
>>> try:
...     loader = LyricsLoader('Some Arist Not To Be Found')
... except LyricsLoaderError as e:
...     print(f'caught exception: {e}')
... 
caught exception: artist "Some Arist Not To Be Found" not found
```

### Installation
This package is not yet hosted on PyPI.  To install from source:
```
$ git clone https://github.com/dkaslovsky/LyricsLoader.git
$ cd LyricsLoader
$ python setup.py install
```

### Note
This work originally began as a fork and intended refactor of [PyLyrics](https://github.com/geekpradd/PyLyrics) but deviated significantly in design and API that it became its own project.  Nonetheless credit for the original implementation goes to [@geekpradd](https://github.com/geekpradd).
