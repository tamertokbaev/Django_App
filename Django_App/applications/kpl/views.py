from django.shortcuts import render
from .models import Club, GameCycle

# Create your views here.


def tournament_table(request):
    clubs = Club.objects.all()
    for i in clubs:
        i.earned_points = i.count_of_wins*3 + i.count_of_draws
        i.save()
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
