from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:news_id>/', views.one_by_one, name='one_by_one'),
    path('news/<int:news_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('news/<int:news_id>/add_fav', views.add_to_favourites, name='add_to_fav'),
    path('news/<slug:section>/', views.section_news, name='section_news'),
    path('accounts/register/', views.register_user, name='register'),
    path('archive/', views.archive, name='archive'),
    path('search/', views.search, name='search'),
    path('accounts/confirming_registration', views.confirming_register, name='reg_confirm'),
    path('accounts/<slug:slug>/profile/', views.show_profile, name='profile'),
    path('accounts/edit_profile', views.edit_profile, name='edit_profile'),
    path('accounts/<slug:slug>/profile/favourites', views.show_favourites, name='show_favourites'),
    path('accounts/profile/change_avatar', views.profile_avatar, name='change_avatar'),
]
