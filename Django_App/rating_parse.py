import requests
from bs4 import BeautifulSoup
from django.apps import apps
base_url = 'https://football.kulichki.net/uefa.htm'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


# Function parsing from sports.kz
def parse_news(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('Parsing is doing...')
        soup = BeautifulSoup(request.content, 'html.parser')
        strongs = soup.find_all('table', attrs={'width': '95%'})
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
            elif clubs_str[i] == "":
                pass
            elif clubs_str[i] == '\xa0':
                pass
            elif clubs_str[i] == '-' and clubs_str[i-1] != 'н':
                clubs.append(0)
                club = ""
            else:
                club += clubs_str[i]
        new_club_list = []
        for i in range(21 , len(clubs)):
            if clubs[i] != '' and clubs[i] != ' ':
                new_club_list.append(clubs[i])
        a = []
        j = 0
        b = []
        for i in range(55):
            b.append(new_club_list[j + 0])
            b.append(new_club_list[j + 1])
            b.append(float(new_club_list[j + 2])*1000)
            b.append(float(new_club_list[j + 3])*1000)
            b.append(float(new_club_list[j + 4])*1000)
            b.append(float(new_club_list[j + 5])*1000)
            b.append(float(new_club_list[j + 6])*1000)
            b.append(float(new_club_list[j + 7])*1000)
            b.append(new_club_list[j + 8])
            a.append(b)
            b = []
            j += 9
        print(a)
        return a
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')


club_list = parse_news(base_url, headers)
RatingCountry = apps.get_model('kpl', 'RatingCountry')
for i in range(55):
    RatingCountry.objects.create(place=club_list[i][0], country_name=club_list[i][1], season15_16=club_list[i][2],
                                 season16_17=club_list[i][3], season17_18=club_list[i][4], season18_19=club_list[i][5],
                                 season19_20=club_list[i][6], total_rating=club_list[i][7], command_count=club_list[i][8])
