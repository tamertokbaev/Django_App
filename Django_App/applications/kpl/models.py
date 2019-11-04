from django.db import models
from django.utils import timezone


class Club(models.Model):
    club_name = models.CharField(max_length=100)
    club_icon = models.ImageField(upload_to='images/')
    matches_played = models.IntegerField(default=0)
    count_of_wins = models.IntegerField(default=0)
    count_of_draws = models.IntegerField(default=0)
    count_of_loses = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    earned_points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.club_name)

    def set_points(self, points):
        self.earned_points = points


class GameCycle(models.Model):
    tour_id = models.IntegerField(default=1)
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='salam')
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='molekulam')
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tour_id) + ' ' + str(self.home_team) + ' VS ' + str(self.away_team)
