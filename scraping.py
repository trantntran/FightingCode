from bs4 import BeautifulSoup as BS
import requests

def scrap_lyric(search_input):
    # Format Input
    search_input = search_input.replace(' ', '+') if search_input != '' else 'Hello'

    # Get the 1st song in the search list
    page_search = requests.get("http://search.azlyrics.com/search.php?q=" + search_input)
    soup = BS(page_search.text,'html.parser')

    link_search = []
    table_tag = soup.findAll('table', attrs={'class':'table table-condensed'})
    
    if len(table_tag) == 2:
        td_tag = table_tag[1].find('td', attrs ={'class':'text-left visitedlyr'}).a['href']
        link_search.append(td_tag)
    elif len(table_tag) == 3:
        td_tag = table_tag[2].find('td', attrs ={'class':'text-left visitedlyr'}).a['href']
        link_search.append(td_tag)   
    else:
        td_tag = table_tag[0].find('td', attrs ={'class':'text-left visitedlyr'}).a['href']
        link_search.append(td_tag)
        
    # Get the lyric/title/single
    
    page_lyric = requests.get(link_search[0])
    soup_lyric = BS(page_lyric.text,'html.parser')
    div_tag = soup_lyric.findAll('div', attrs={'class':'col-xs-12 col-lg-8 text-center'})
    #title
    title = div_tag[0].h1.text
    #singer
    artist = div_tag[0].find('div', attrs={'class':'lyricsh'}).h2.text
    #lyric
    lyric = div_tag[0].find('div', attrs={'class':''})
    
    # Get the description (if any) - writer...
   
    try:
    # Writer
        writer_list = []
        writer_tag = soup_lyric.findAll('div', attrs={'class':'smt'})
        for i in writer_tag:    
            writer_list.append(i.text)
        writer = writer_list[-1]
        #print(writer)

    # Short description:
        description_str = ''
        writer = soup_lyric.findAll('div', attrs={'class':'panel album-panel noprint'})
        for i in writer:
            description_str = description_str + str(i.text)

    except:
        pass

    return {"artist":artist, "title":title, "description": description_str, "lyric": lyric}
