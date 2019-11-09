from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:news_id>/', views.one_by_one, name='one_by_one'),
    path('news/<int:news_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('accounts/register/', views.register_user, name='register'),
    path('archive/', views.archive, name='archive'),
    path('search/', views.search, name='search'),
    path('accounts/confirming_registration', views.confirming_register, name='reg_confirm'),
    path('accounts/profile/', views.show_profile, name='profile'),
    path('accounts/edit_profile', views.edit_profile, name='edit_profile'),
]
