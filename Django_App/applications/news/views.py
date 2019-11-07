from django.contrib import auth
from django.shortcuts import render, redirect, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.urls import reverse
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

            return HttpResponseRedirect('/accounts/login')
        else:
            return render_to_response('invalid_reg.html')

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
            all_news = News.objects.filter(news_content__icontains=search_str) .filter(news_content__icontains=search_str)
        return render(request, 'news/search.html', {'all_news': all_news})
    except:
        return render(request, 'news/search.html', {})
