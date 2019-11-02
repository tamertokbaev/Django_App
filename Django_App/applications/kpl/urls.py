from django.urls import path
from . import views

app_name = 'kpl'
urlpatterns = [
    path('', views.tournament_table, name='tournament_table')
]
