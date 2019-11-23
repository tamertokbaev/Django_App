from django.urls import path
from . import views

app_name = 'kpl'
urlpatterns = [
    path('kaz-premier-league/tournament_table/', views.tournament_table, name='tournament_table'),
    path('kaz-premier-league/calendar/', views.show_calendar, name='calendar'),
    path('ucl/tournament_table/', views.UCL_mainTable, name='ucl_main_table'),
    path('ucl/group/<slug:group>/', views.UCL_groupTable, name='ucl_group_table')
]
