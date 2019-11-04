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
    context = {}
    for i in range(33):
        cycle = GameCycle.objects.get(tour_id=counter)
        counter += 1
        games_in_single_tour = []
        for j in cycle:
            games_in_single_tour.append(j)
        context.update({str(cycle.tour_id): games_in_single_tour})
    print(context)
    return render(request, 'kpl/calendar.html', context)
