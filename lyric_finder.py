# lyric_finder.py v1.0
from bs4 import BeautifulSoup
from os import system, name  
import requests


def parseHTMLData(html):
	soup = BeautifulSoup(html.content, 'html.parser')
	search_results = soup.find_all("div", {"class": "lyric-meta within-lyrics"})
	for item in search_results:
		# [artist, album, album_year]
		if item is not None:
			meta = [item.find('p', class_='lyric-meta-artists').getText(), item.find('p', class_='lyric-meta-album').getText(), item.find('p', class_='lyric-meta-album-year').getText()]
			getData(item.find('p', class_='lyric-meta-title').getText(), meta)

  
def clear():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def getData(title, meta):
	songs[len(songs)] = title, meta[0], meta[1], meta[2]


def main():
	song = input(':What song would you like to find lyrics for? ')
	parseHTMLData(requests.get('https://www.lyrics.com/lyrics/{}'.format(song.replace(' ', '%20'))))
	clear()
	for key in songs.keys():
		print('--' + '='*56 + '--')
		print('** ' + 'Song {}:'.format(key+1) + ' '*(49-len(str(key+1))) + '**')
		print('--' + '='*56 + '--')
		print('Title: {}'.format(songs.get(key)[0]) + '\nArtist: {}'.format(songs.get(key)[1]) + '\nAlbum: {}'.format(songs.get(key)[2]) + '\nYear: {}'.format(songs.get(key)[3]))
		if 'y' == input('}Is this the correct song? (y/n): ').lower():
			correct_song = key
			break
		else:
			correct_song = None
			clear()
	if correct_song == None:
		print("Couldn't find any other songs... Sorry!")
		main()
	soup = BeautifulSoup(requests.get('https://www.lyrics.com/lyrics/{}'.format(song.replace(' ', '%20'))).content, 'html.parser')
	search = str(soup.find_all('pre', {'class': 'lyric-body'})[correct_song])
	link = search[search.find('https://'):search.find(';')-1]
	soup = BeautifulSoup(requests.get(link).content, 'html.parser')
	lyrics = soup.find('pre').text
	print('--' + '='*56 + '--\nLink: {}\nSong: {}\n'.format(link, songs.get(key)[0]) + '--' + '='*56 + '--\n{}'.format(lyrics) + '\n--' + '='*56 + '--')





songs = {}
main()

