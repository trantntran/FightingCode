from bs4 import BeautifulSoup
import requests

def scrape_song(search_input):
    """ Input:  String 
                Search Term for artist or song
        Output: Dictionary
                Information for the song. If it's an artist, for the first song found. 
    """
    
    # BASE_URL = 'https://www.azlyrics.com/'
    SEARCH_URL = 'https://search.azlyrics.com/search.php?q='
    req = requests.get(SEARCH_URL)
    soup = BeautifulSoup(req.text, 'html.parser')

    print(soup.prettify())
    
