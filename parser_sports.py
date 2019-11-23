import requests
from bs4 import BeautifulSoup
from django.apps import apps

base_url = 'https://football.kulichki.net/league/'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


# Function parsing from sports.kz
def parse_news(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = BeautifulSoup(request.content, 'html.parser')
        strongs = soup.find_all('table', attrs={'border': '1', 'bgcolor': '#FFFFCC', 'id': 'table149'})
        club_str = ""
        for strong in strongs:
            clubs_str = strong.text
        club_list = list(clubs_str)
        clubs = []
        club = ""
        for i in range(len(club_list)):
            if club_list[i] == "\n":
                clubs.append(club)
                club = ""
            else:
                club += club_list[i]
        clubs = set(clubs)
        clubs = list(clubs)
        clubs.remove('')
        a = []
        for club in clubs:
            if club.find("Группа") == -1:
                a.append(club.swapcase().capitalize())
        return a
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')


clubs = parse_news(base_url, headers)
print(clubs)
EUClub = apps.get_model('kpl', 'Eu_club')
for club in clubs:
    EUClub.objects.create(club_name=club)
    EUClub.save
