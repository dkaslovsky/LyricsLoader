from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='lyricsloader',
    version='0.0.1',
    author='Daniel Kaslovsky',
    author_email='dkaslovsky@gmail.com',
    license='MIT',
    description='Library for downloading song lyrics from lyrics.wikia.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['beautifulsoup4', 'requests'],
    url='https://github.com/dkaslovsky/LyricsLoader',
    keywords=['python', 'lyrics', 'scrape'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
