import requests
from bs4 import BeautifulSoup
from django.apps import apps

base_url = 'https://football.kulichki.net/fifa.htm'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


# Function parsing from sports.kz
def parse_news(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = BeautifulSoup(request.content, 'html.parser')
        strongs = soup.find_all('table', attrs={'width': '80%'})
        club_str = ""
        for strong in strongs:
            club_str = strong.text
        clubs_str = list(club_str)
        clubs = []
        club = ""
        for i in range(len(clubs_str)):
            if clubs_str[i] == "\n":
                clubs.append(club)
                club = ""
            elif clubs_str[i] == "" or clubs_str[i] == " ":
                pass
            elif clubs_str[i] == '\xa0':
                pass
            else:
                club += clubs_str[i]
        new_club_list = []
        for i in range(21, len(clubs)):
            if clubs[i] == 'Северная':
                new_club_list.append('Северная Ирландия')
            elif clubs[i] == 'Ирландия' and clubs[i + 1] != '1480':
                pass
            elif clubs[i] == 'Саудовская':
                new_club_list.append('Саудовская Аравия')
            elif clubs[i] == 'Аравия':
                pass
            elif clubs[i] != '' and clubs[i] != ' ':
                new_club_list.append(clubs[i])
        b = []
        count = 0
        a = []
        for i in range(0, 440, 4):
            b.append(new_club_list[i + 0])
            b.append(new_club_list[i + 1])
            b.append(new_club_list[i + 2])
            b.append(new_club_list[i + 3])
            a.append(b)
            b = []
        print(a)
        return a
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')
    else:
        print("Unexpected error occurred")


club_list = parse_news(base_url, headers)
RatingCountryFifa = apps.get_model('kpl', 'RatingCountryFifa')
for i in range(209):
    RatingCountryFifa.objects.create(place=club_list[i][0], country_name=club_list[i][1],
                                     prev_match_rating=club_list[i][2], next_match_rating=club_list[i][3])