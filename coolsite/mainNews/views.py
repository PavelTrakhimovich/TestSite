from django.http import HttpResponse
from django.http.response import  HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *



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
    if request.method == 'POST':
        form = AddPageForm(request.POST)
        if form.is_valid():
            try:
                News.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error add post')
            
    else:
        form = AddPageForm()
    return render (request, 'mainNews/addpage.html', {'form': form, 'title':'Create news'})


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


def show_category(request, cat_slug):
    posts = News.objects.filter(cat__slug=cat_slug)




    context = {
        'posts':posts,
        'title': 'Categories',
        'cat_selected': cat_slug,
    }

    return render(request, 'mainNews/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound ('<h1>Page not found</h1>')

