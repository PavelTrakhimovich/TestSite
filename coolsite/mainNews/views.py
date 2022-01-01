from django.http import HttpResponse
from django.http.response import  HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import *



def index(request):
    posts = News.objects.all()
    context = {
        'posts':posts,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'mainNews/index.html', context=context)


def about(request):
    return render(request, 'mainNews/about.html', {'title': 'About site',})


def addpage(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Login")


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    
    context = {
        'post':post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'mainNews/post.html', context=context)


def show_category(request, cat_id):
    posts = News.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404()


    context = {
        'posts':posts,
        'title': 'Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'mainNews/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound ('<h1>Page not found</h1>')

