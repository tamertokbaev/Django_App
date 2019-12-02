import requests
from bs4 import BeautifulSoup
from django.apps import apps

base_url = 'https://football.kulichki.net/uefa_cup/2020/g.htm'
headers = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                          'like Gecko) Ch   rome/78.0.3904.97 Safari/537.36'}


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
        club_list = clubs[14:]
        a = []
        j = 0
        counter = 0
        for i in range(4):
            if counter == 2:
                a.append(club_list[j+1:7+j+1])
                counter += 1
                j += 12
            elif counter == 1:
                a.append(club_list[j:7+j])
                j+= 12
                counter += 1
            elif counter == 3:
                a.append(club_list[j+2:7 + j + 2])
                j += 12
            else:
                a.append(club_list[j:7+j])
                counter += 1
                j += 12
        return a
    elif requests.status_code == 404:
        print('404 error, page not found!')
        print('Or you are banned because of parsing')


a = parse_news(base_url, headers)
for i in range(4):
    a[i][0] = a[i][0].lstrip().lower().capitalize()
print(a)

# Save to database
#
Eu_club = apps.get_model('kpl', 'Eu_club')
for i in range(4):
    club = Eu_club.objects.get(club_name=a[i][0])
    club.matches_played = a[i][1]
    club.count_of_wins = a[i][2]
    club.count_of_draws = a[i][3]
    club.count_of_loses = a[i][4]
    club.goal_difference = a[i][5]
    club.earned_points = a[i][6]
    club.group = 'G'
    club.save()
