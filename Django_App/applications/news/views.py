from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from .models import News, Comment
# Create your views here.


def index(request):
    news_list = News.objects.all()

    return render(request, 'news/index.html', {'news_list': news_list})


def one_by_one(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404("Статья не найдена!")
    comment_list = a.comment_set.all()
    return render(request, 'news/detail.html', {'news': a, 'comments_list': comment_list})


def leave_comment(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404("Статья не найдена!")
    a.comment_set.create(comment_author=auth.get_user(request), comment_text=request.POST['comment_text'])
    return HttpResponseRedirect(reverse('news:one_by_one', args=(news_id,)))


# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = User(password=User.set_password(password), username=username, first_name=first_name, last_name=last_name,
#                     email=email)
#         user.save()


class RegistrationForm(FormView):
    form_class = UserCreationForm

    # After registration of a new user, client will be redirected to this URL
    success_url = '/accounts/login'

    # Template that is used to show registration page
    template_name = 'register.html'

    def form_valid(self, form):
        # if everything is clear during registration, we will add this user into a database
        form.save()
        return super(RegistrationForm, self).form_valid(form)
