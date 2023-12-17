from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import redirect, render, reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '<b>Та</b> ещё соска\nсасная', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


# Create your views here.
def index(request: HttpRequest):
    data = {
        'title': 'Главная страница naebal',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, 'women/about.html', context=data)


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data = {
        'title': 'Mapping with rubric',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def show_post(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Обратная связь")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
