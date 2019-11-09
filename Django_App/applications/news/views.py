from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.urls import reverse
from django.core.mail import send_mail

from random import randint

from .models import News
from .forms import CustomRegistrationForm


# Данная функция используется для показа содержимого главной страницы
def index(request):
    news_list = News.objects.order_by('-count_of_views')[:8]
    return render(request, 'news/index.html', {'news_list': news_list})


# Данная функция используется для показа определенной новости по ссылке в urls.py news/<int:news_id>
def one_by_one(request, news_id):
    try:
        a = News.objects.get(id=news_id)
        a.count_of_views += 1
        a.save()
    except:
        raise Http404("Статья не найдена!")
    comment_list = a.comment_set.all()
    return render(request, 'news/detail.html', {'news': a, 'comments_list': comment_list})


# Данная функция используется для оставления комментария в новосте по ссылке news/<int:news_id>
def leave_comment(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404("Статья не найдена!")
    a.comment_set.create(comment_author=auth.get_user(request), comment_text=request.POST['comment_text'])
    return HttpResponseRedirect(reverse('news:one_by_one', args=(news_id,)))


# Данная функция используется для регистрации нового пользователя при помощи кастомной форм CustomRegistrationForm в
# forms.py
def register_user(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            secret_code = randint(1000, 9999)
            head_of_message = 'Подтверждение регистрации на Football-News-Portal'
            content_of_message = """
                Здравствуйте, ваш электронный адрес был выбран для регистрации на Football News Portal 
                Ваш секретный код: {} 

                Если вы не регистрировались на Football-News-Portal, то пожалуйста просто проигнорируйте это письмо!
                С уважением, Тамерлан Токбаев!
                """.format(secret_code)
            send_mail(head_of_message, content_of_message, "Tamerlan's website",
                      recipient_list=[form.cleaned_data['email']]
                      , fail_silently=False)
            request.session.update({'form': {'username': form.cleaned_data['username'],
                                             'secret_code': secret_code}})
            # form.save()
            return HttpResponseRedirect('/accounts/confirming_registration')
        else:
            return render_to_response('register.html', {'form': form})
    args = {}
    args.update(csrf(request))
    args['form'] = CustomRegistrationForm()
    return render_to_response('register.html', args)


# Данная функция используется для показа всех новостей по дате публикации на новой странице
def archive(request):
    try:
        news_list = News.objects.order_by('publication_date')
    except:
        raise Http404('Список новостей пуст')
    return render(request, 'news/archive.html', {'news_list': news_list})


# Данная функция используется для поиска на главной странице по содержимому и заголовку новости
# Возможны результаты больше чем 1, отображается на отдельной странице search.html
def search(request):
    all_news = []
    try:
        if request.method == 'POST':
            search_str = request.POST['searching_line']
            all_news = News.objects.filter(news_content__icontains=search_str).filter(
                news_content__icontains=search_str)
        return render(request, 'news/search.html', {'all_news': all_news})
    except:
        return render(request, 'news/search.html', {})


# Подтверждение регистрации через электронную почту
def confirming_register(request):
    session = request.session
    if request.method == 'POST':
        if session['form']['secret_code'] == int(request.POST['code_by_user']):
            username = session['form']['username']
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            return render(request, 'news/confirm.html',
                          {'result': 'Секретный код был введен неверно! Регистрация отменена!'})
    return render(request, 'news/confirm.html', {})
