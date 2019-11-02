from django.db import models

# Create your models here.
from django.db.models import F


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
