"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import PoolForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from app.models import Article
from app.models import Comment # использование модели комментариев
from app.forms import CommentForm, ArticleForm # использование формы ввода комментария

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страница контактов.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О сайте',
            'message':'Страница описания приложения.',
            'year':datetime.now().year,
        }
    )

def pool(request):
    """Renders the pool page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            return render(
                request,
                'app/pool_success.html',
                {
                    'request': request.POST,
                    'year':datetime.now().year,
                }
                )
    else:
        return render(
            request,
            'app/pool.html',
            {
                'pool_form': PoolForm(),
                'year':datetime.now().year,
            }
            )


def registration(request):

    """Renders the registration page."""

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

        regform = UserCreationForm (request.POST)

        if regform.is_valid(): #валидация полей формы

            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

            reg_f.is_staff = False # запрещен вход в административный раздел

            reg_f.is_active = True # активный пользователь

            reg_f.is_superuser = False # не является суперпользователем

            reg_f.date_joined = datetime.now() # дата регистрации

            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('home') # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

        return render(

                    request,

                    'app/registration.html',

                    {

                    'regform': regform, # передача формы в шаблон веб-страницы

                    'year':datetime.now().year,

                    }

                    )

def blog(request):

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Article.objects.all() # запрос на выбор всех статей блога из модели

    return render(

                request,

                'app/blog.html',

                {

                'title':'Блог',

                'posts': posts, # передача списка статей в шаблон веб-страницы

                'year':datetime.now().year,

                }

                )

def blogpost(request, parameter):

    """Renders the blogpost page."""

    assert isinstance(request, HttpRequest)

    post_1 = Article.objects.get(id=parameter) # запрос на выбор конкретной статьи по параметру

    comments = Comment.objects.filter(post=parameter)  # запрос на выбор всех её комментариев

    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = CommentForm(request.POST)

        if form.is_valid():

            comment_f = form.save(commit=False)

            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя

            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату

            comment_f.post = Article.objects.get(id=parameter) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий

            comment_f.save() # сохраняем изменения после добавления полей

        return redirect('blogpost', parameter=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:

            form = CommentForm() # создание формы для ввода комментария

    return render(

                request,

                'app/blogpost.html',

                {

                'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

                'year':datetime.now().year,

                'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы

                'form': form, # передача формы добавления комментария в шаблон веб-страницы

                }

                )

def newpost(request):
    """Renders the newpost page."""

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():

            article = Article()

            article.author = request.user
            article.header = request.POST.get('header')
            article.description = request.POST.get('description')
            article.content = request.POST.get('content')
            article.date = datetime.now() 
            article.image = request.FILES.get('image')
            article.save() 

            '''
            blog_f = form.save(commit=False)
            blog_f.date = datetime.now()
            blog_f.author = request.user
            blog_f.save()
            '''

        return redirect('blog')

    else:

            form = ArticleForm() 

    return render(

                request,

                'app/newpost.html',

                {

                'article_form': form,

                'year':datetime.now().year,

                }

                )

def videopost(request): 
    """Renders the video page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'О сайте',
            'message':'Страница описания приложения.',
            'year':datetime.now().year,
        }
    )