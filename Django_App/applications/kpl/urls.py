from django.urls import path
from . import views

app_name = 'kpl'
urlpatterns = [
    path('kaz-premier-league/tournament_table/', views.tournament_table, name='tournament_table'),
    path('kaz-premier-league/calendar/', views.show_calendar, name='calendar'),
    path('<slug:tournament_table>/tournament_table/', views.UCL_mainTable, name='euro_main_table'),
    path('<slug:tournament_type>/group/<slug:group>/', views.UCL_groupTable, name='euro_group_table'),
    path('rating/uefa-coefficients/', views.coefficient_table, name='coefficient_table'),
    path('rating/fifa-coefficients/', views.coefficient_table_FIFA, name='coefficient_table_FIFA')
]
