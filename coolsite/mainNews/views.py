from django.http import HttpResponse
from django.http.response import  HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

from .models import *
from .forms import *


menu = [{'title':"About site", 'url_name': 'about'},
        {'title':"Add news", 'url_name': 'add_page'},
        {'title':"Feedback", 'url_name': 'contact'},
        {'title':"Sign In", 'url_name': 'login'},
        ]


class NewsHome(ListView):
    model = News
    template_name = 'mainNews/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context


    def get_queryset(self):
        return News.objects.filter(is_published=True)



def about(request):
    return render(request, 'mainNews/about.html', {'title': 'About site',})


class AddPost(CreateView):
    form_class = AddPageForm
    template_name = 'mainNews/addpost.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Create post'
        return context



def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Login")


class ShowPost(DetailView):
    model = News
    template_name = 'mainNews/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context



class NewsCategory(ListView):
    model = News
    template_name = 'mainNews/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


    def get_queryset(self):
        return News.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound ('<h1>Page not found</h1>')

