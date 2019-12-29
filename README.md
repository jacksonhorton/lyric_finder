# lyric_finder.py
This is a very simple console lyric lookup tool that uses lyrics.com's website.

# How to use
All you have to do is clone this repo or download *lyric_finder.py*. Then follow the steps below:
1. Enter the song title you want to find lyrics for.
2. Songs and its author's name will be printed. If the song displayed is the song you are looking for, type '*y*' and then hit enter. Otherwise, type '*n*' or any other key and hit enter. Example shown below.
```
--========================--
** Song 1:                                                **
--========================--
Title: Earthquake
Artist: Marshmello, TYNAN
Album: Joytime III
Year: 2019
}Is this the correct song? (y/n): 
```
3. The lyrics will be loaded and displayed with the link and song title above them.

# Requirements
You only need the *requests* and *beautifulsoup4* modules. To install them, use the commands below in a terminal:
```
pip install beautifulsoup4
pip install requests
```
*Note: If you have Python 2 installed, use pip3 to install for the correct version of Python!*