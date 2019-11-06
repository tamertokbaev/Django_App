from django.shortcuts import render
from .models import Club, GameCycle

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
    return render(request, 'kpl/tournament_table.html', {'club_list': clubs})


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
    context = {'tours': tours}
    return render(request, 'kpl/calendar.html', context)
