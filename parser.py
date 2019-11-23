import requests
from bs4 import BeautifulSoup
from django.apps import apps

base_url = 'https://football.kulichki.net/league/2020/a.htm'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


# Function parsing from sports.kz
def parse_news(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = BeautifulSoup(request.content, 'html.parser')
        strongs = soup.find_all('table', attrs={'id': 'table18'})
        club_str = ""
        for strong in strongs:
            clubs_str = strong.text
        clubs_str = list(clubs_str)
        clubs = []
        club = ""
        for i in range(len(clubs_str)):
            if clubs_str[i] == "\n":
                clubs.append(club)
                club = ""
            else:
                club += clubs_str[i]
        print(clubs)
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')


clubs = parse_news(base_url, headers)
# EUClub = apps.get_model('kpl', 'Eu_club')
# for club in clubs:
#     EUClub.objects.create(club_name=club)
#     EUClub.save
