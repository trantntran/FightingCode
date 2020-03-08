from bs4 import BeautifulSoup
import requests
import re

def scrape_song(search_input):
    """ Input:  String 
                Search Term for artist or song
        Output: Dictionary
                Information for the song. If it's an artist, for the first song found. 
    """
    
    # BASE_URL = 'https://www.azlyrics.com/'
    
    # Format input and get right URL for HTML
    SEARCH_URL = 'https://search.azlyrics.com/search.php?q='
    search_input = search_input.replace(' ', '+') if search_input != None else 'Hello'
    req = requests.get(SEARCH_URL+search_input) # use site search for input
    soup = BeautifulSoup(req.text, 'html.parser')

    # Find first listed song URL
    song_link = soup.find_all(lambda tag:tag.name=='td' and "1." in tag.text)
    
    # Regex to find URLS /https.+?(?<=html)/ in Beautiful Soup Object
    song_link = re.findall(r'https.+?(?<=html)', str(song_link))
    
    # Remove all non-song links 
    song_link = ''.join([s for s in song_link if '/lyrics/' in s])
    #print( song_link )


    # Move req and soup to Song website and parse it
    req = requests.get(song_link)
    soup = BeautifulSoup(req.text, 'html.parser')

    song_info = {
                    'artist': '',
                    'title': '',
                    'description': '',
                    'lyrics': ''
    }

    song_info['artist'] = soup.find('div', 'lyricsh').text

    



    return song_info