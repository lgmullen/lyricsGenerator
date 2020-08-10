GENIUS_API_TOKEN='5x9S4cy3yV-_aJi0kbAxmy2LBDRnNcYxB08syeCmChmrWm3GcaYgvZkZqAFdqi3R'
# Make HTTP requests
import requests
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re
# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)
    
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
            
        if (len(songs) == song_cap):
            break
        else:
            page += 1
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    

# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    return lyrics

def write_lyrics_to_file(artist_name, song_count):
    space = '\n========\n'
    f = open('data/lyrics/' + artist_name.lower() + '.txt', 'w')
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics)
        f.write(space)
    num_lines = sum(1 for line in open('data/lyrics/' + artist_name.lower() + '.txt', 'rb'))
    print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))
