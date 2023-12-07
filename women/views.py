from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse(b"hello gigachad")


def categories(request, cat_id):
    return HttpResponse(f"<h1>cats a lot cats!!!</h1>"
                        f"<p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>many a lot of slugs!!!</h1>"
                        f"<p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1>"
                        f"<p>year: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
