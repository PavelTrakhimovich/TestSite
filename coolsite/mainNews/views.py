from django.http import HttpResponse
from django.http.response import  HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from .models import *

menu = [{'title':"About site", 'url_name': 'about'},
        {'title':"Add news", 'url_name': 'add_page'},
        {'title':"Feedback", 'url_name': 'contact'},
        {'title':"Sign In", 'url_name': 'login'},
]

def index(request):
    posts = News.objects.all()
    context = {
        'menu': menu,
        'posts':posts,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'mainNews/index.html', context=context)


def about(request):
    return render(request, 'mainNews/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Login")


def show_post(request, post_id):
    return HttpResponse(f"Post {post_id}")


def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404()


    context = {
        'menu': menu,
        'posts':posts,
        'title': 'Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'mainNews/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound ('<h1>Page not found</h1>')

