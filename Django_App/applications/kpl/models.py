from django.db import models


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
    started_points = models.IntegerField(default=0)

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
        return str(self.tour_id) + ' ' + str(self.home_team) + ' ' + str(self.home_goals) + ':' + ' '\
               + str(self.away_goals) + ' ' + str(self.away_team)


class Eu_club(models.Model):
    club_name = models.CharField(max_length=100)
    matches_played = models.IntegerField(default=0)
    count_of_wins = models.IntegerField(default=0)
    count_of_draws = models.IntegerField(default=0)
    count_of_loses = models.IntegerField(default=0)
    goal_difference = models.CharField(default=0, max_length=10)
    earned_points = models.IntegerField(default=0)
    started_points = models.IntegerField(default=0)
    tournament_played = models.CharField(default='UCL', max_length=100)
    group = models.CharField(default=0, max_length=1)

    def __str__(self):
        return str(self.club_name)


class Eu_cycle(models.Model):
    home_team = models.ForeignKey(Eu_club, on_delete=models.CASCADE, related_name='salam')
    away_team = models.ForeignKey(Eu_club, on_delete=models.CASCADE, related_name='molekulam')
    result = models.CharField(default=0, max_length=10)
    tournament_played = models.CharField(default='UEL', max_length=100)
    group = models.CharField(default='L', max_length=1)

    def __str__(self):
        return self.home_team.club_name + ' ' + self.result + ' ' + self.away_team.club_name + '. Группа ' +\
               self.group + ' ' + self.tournament_played


class RatingCountry(models.Model):
    place = models.IntegerField(null=True, default=1)
    country_name = models.CharField(max_length=100)
    season15_16 = models.FloatField(null=True, default=0)
    season16_17 = models.FloatField(null=True, default=0)
    season17_18 = models.FloatField(null=True, default=0)
    season18_19 = models.FloatField(null=True, default=0)
    season19_20 = models.FloatField(null=True, default=0)
    total_rating = models.FloatField(null=True, default=0)
    command_count = models.CharField(max_length=7)

    def __str__(self):
        return self.country_name + " " + str(self.total_rating)


class RatingCountryFifa(models.Model):
    place = models.IntegerField(null=True, default=1)
    country_name = models.CharField(max_length=100)
    prev_match_rating = models.IntegerField(null=True, default=0)
    next_match_rating = models.IntegerField(null=True, default=0)