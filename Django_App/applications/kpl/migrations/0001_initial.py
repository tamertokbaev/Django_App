# Generated by Django 2.2.6 on 2019-11-27 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('club_icon', models.ImageField(upload_to='images/')),
                ('matches_played', models.IntegerField(default=0)),
                ('count_of_wins', models.IntegerField(default=0)),
                ('count_of_draws', models.IntegerField(default=0)),
                ('count_of_loses', models.IntegerField(default=0)),
                ('goals_scored', models.IntegerField(default=0)),
                ('goals_conceded', models.IntegerField(default=0)),
                ('earned_points', models.IntegerField(default=0)),
                ('started_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eu_club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('matches_played', models.IntegerField(default=0)),
                ('count_of_wins', models.IntegerField(default=0)),
                ('count_of_draws', models.IntegerField(default=0)),
                ('count_of_loses', models.IntegerField(default=0)),
                ('goal_difference', models.CharField(default=0, max_length=10)),
                ('earned_points', models.IntegerField(default=0)),
                ('started_points', models.IntegerField(default=0)),
                ('tournament_played', models.CharField(default='UCL', max_length=100)),
                ('group', models.CharField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RatingCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(default=1, null=True)),
                ('country_name', models.CharField(max_length=100)),
                ('season15_16', models.FloatField(default=0, null=True)),
                ('season16_17', models.FloatField(default=0, null=True)),
                ('season17_18', models.FloatField(default=0, null=True)),
                ('season18_19', models.FloatField(default=0, null=True)),
                ('season19_20', models.FloatField(default=0, null=True)),
                ('total_rating', models.FloatField(default=0, null=True)),
                ('command_count', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='RatingCountryFifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(default=1, null=True)),
                ('country_name', models.CharField(max_length=100)),
                ('prev_match_rating', models.IntegerField(default=0, null=True)),
                ('next_match_rating', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_id', models.IntegerField(default=1)),
                ('home_goals', models.IntegerField(default=0)),
                ('away_goals', models.IntegerField(default=0)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='molekulam', to='kpl.Club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salam', to='kpl.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Eu_cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(default=0, max_length=10)),
                ('tournament_played', models.CharField(default='UEL', max_length=100)),
                ('group', models.CharField(default='L', max_length=1)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='molekulam', to='kpl.Eu_club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salam', to='kpl.Eu_club')),
            ],
        ),
    ]
