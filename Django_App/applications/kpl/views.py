from django.shortcuts import render
from .models import Club

# Create your views here.


def tournament_table(request):
    clubs = Club.objects.all()
    for i in clubs:
        i.earned_points = i.count_of_wins*3 + i.count_of_draws
        i.save()
    return render(request, 'kpl/tournament_table.html', {'club_list': clubs})
