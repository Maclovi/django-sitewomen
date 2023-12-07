from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render, reverse


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse(b"hello gigachad")


def categories(request: HttpRequest, cat_id):
    return HttpResponse(f"<h1>cats a lot cats!!!</h1>"
                        f"<p>id: {cat_id}</p>")


def categories_by_slug(request: HttpRequest, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>many a lot of slugs!!!</h1>"
                        f"<p>slug: {cat_slug}</p>")


def archive(request: HttpRequest, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1>"
                        f"<p>year: {year}")


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
