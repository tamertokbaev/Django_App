from django.http import Http404
from django.shortcuts import render
from django.apps import apps

from .models import Club, GameCycle, Eu_cycle, Eu_club

# Create your views here.


def tournament_table(request):
    clubs = Club.objects.all()
    game_cycle = GameCycle.objects.all()
    for i in clubs:
        count_of_wins = 0
        count_of_draws = 0
        count_of_loses = 0
        goals_scored = 0
        goals_conceded = 0
        for j in game_cycle:
            if j.home_team.id == i.id:
                if j.home_goals > j.away_goals:
                    count_of_wins += 1
                elif j.home_goals == j.away_goals:
                    count_of_draws += 1
                else:
                    count_of_loses += 1
                goals_scored += j.home_goals
                goals_conceded += j.away_goals
            elif j.away_team.id == i.id:
                if j.home_goals < j.away_goals:
                    count_of_wins += 1
                elif j.home_goals == j.away_goals:
                    count_of_draws += 1
                else:
                    count_of_loses += 1
                goals_scored += j.away_goals
                goals_conceded += j.home_goals
        i.count_of_wins = count_of_wins
        i.count_of_loses = count_of_loses
        i.count_of_draws = count_of_draws
        i.matches_played = count_of_wins + count_of_loses + count_of_draws
        i.goals_scored = goals_scored
        i.goals_conceded = goals_conceded
        i.earned_points = count_of_wins*3 + count_of_draws + i.started_points
        i.save()
    clubs = Club.objects.order_by('-earned_points')
    News = apps.get_model('news', 'News')
    latest_news = News.objects.order_by('-publication_date')[:4]

    return render(request, 'kpl/tournament_table.html', {'club_list': clubs, 'latest_news': latest_news})


def show_calendar(request):
    counter = 1
    tours = []
    for i in range(33):
        cycle = GameCycle.objects.filter(tour_id=counter)
        counter += 1
        games_in_single_tour = []
        for j in cycle:
            games_in_single_tour.append(j)
        tours.append(games_in_single_tour)
    News = apps.get_model('news', 'News')
    latest_news = News.objects.order_by('-publication_date')[:4]
    context = {'tours': tours, 'latest_news': latest_news}
    return render(request, 'kpl/calendar.html', context)


def UCL_mainTable(request, tournament_table):
    try:
        if tournament_table == 'UCL':
            News = apps.get_model('news', 'News')
            latest_news = News.objects.order_by('-publication_date')[:4]
            club_list = Eu_club.objects.filter(tournament_played='UCL')
            context = {'latest_news': latest_news, 'club_list': club_list}
            group_list = [
                Eu_club.objects.filter(tournament_played='UCL', group='A').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='B').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='C').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='D').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='E').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='F').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='G').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UCL', group='H').order_by('-earned_points')
            ]
            context.update({'group_list': group_list, 'tournament_type': 'Лиги Чемпионов УЕФА', 'tournament': 'UCL'})
        elif tournament_table == 'UEL':
            News = apps.get_model('news', 'News')
            latest_news = News.objects.order_by('-publication_date')[:4]
            club_list = Eu_club.objects.filter(tournament_played='UCL')
            context = {'latest_news': latest_news, 'club_list': club_list}
            group_list = [
                Eu_club.objects.filter(tournament_played='UEL', group='A').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='B').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='C').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='D').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='E').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='F').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='G').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='H').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='I').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='J').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='K').order_by('-earned_points'),
                Eu_club.objects.filter(tournament_played='UEL', group='L').order_by('-earned_points')
            ]
            context.update({'group_list': group_list, 'tournament_type': 'Лиги Европы УЕФА', 'tournament': 'UEL'})
    except:
        raise Http404("Запрашиваемая ваша страница либо перемещена либо навсегда удалена!")
    return render(request, 'kpl/euro_main_table.html', context)


def UCL_groupTable(request, group, tournament_type):
    try:
        if tournament_type == 'UCL':
            News = apps.get_model('news', 'News')
            latest_news = News.objects.order_by('-publication_date')[:4]
            club_list = Eu_club.objects.filter(tournament_played='UCL', group=group).order_by('-earned_points')
            matches_played = Eu_cycle.objects.filter(tournament_played='UCL', group=group)
            context = {'latest_news': latest_news, 'club_list': club_list, 'matches_played': matches_played}
            print('SALAMMOLEKULAM')
            return render(request, 'kpl/eu_group.html', context)
        elif tournament_type == 'UEL':
            News = apps.get_model('news', 'News')
            latest_news = News.objects.order_by('-publication_date')[:4]
            club_list = Eu_club.objects.filter(tournament_played='UEL', group=group).order_by('-earned_points')
            matches_played = Eu_cycle.objects.filter(tournament_played='UEL', group=group)
            context = {'latest_news': latest_news, 'club_list': club_list, 'matches_played': matches_played}
            print('eto liga evrop   i')
            return render(request, 'kpl/eu_group.html', context)
        else:
            render(request, 'kpl/eu_group.html', {})
    except:
        raise Http404("Запрашиваемая ваша страница либо перемещена либо навсегда удалена!")


