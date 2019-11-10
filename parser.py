import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'http://vesti.kz/football/archive/page/1/'


# Function for parsing from web-site
def parse_news(headers, base_url):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'item item-left'})
        for div in divs:
            title = div.find('div', attrs={'class': 'h'}).text
            print(title)
    elif request.status_code == 404:
        print('Something went wrong')
    else:
        print("Server doesn't work at that time")


parse_news(headers, base_url)


""" 
                                                    Author of the script - Tamerlan Tokbayev 
                                        This script parses vesti.kz for educational purposes only

"""