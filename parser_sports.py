import requests
from bs4 import BeautifulSoup

base_url = 'https://www.sports.kz/small/football'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


# Function parsing from sports.kz
def parse_news(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = BeautifulSoup(request.content, 'html.parser')
        link_list = soup.find_all('ul', attrs={'class': 'news_all today_'})
        for link in link_list:
            print(link.get('span'))
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')


parse_news(base_url, headers)
