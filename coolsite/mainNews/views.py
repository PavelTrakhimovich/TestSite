from django.http import HttpResponse
from django.http.response import  HttpResponseNotFound
from django.shortcuts import redirect, render


def index(request):
    return HttpResponse("Page MainNews.")


def categories(request, name_cat):
    if request.GET:
        print(request.Get)
    return HttpResponse(f"<h1>News categorise.<h1><p>{name_cat}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound ('<h1>Page not found</h1>')


def archive(request, year):
    if int(year) > 2022:
        return redirect(f'/archive/2022/', permanent=True)
    return HttpResponse(f"<h1>Archive for years</h1><p>{year}</p>")
    