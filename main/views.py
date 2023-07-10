from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article, ArticleSeries


def homepage(request):
    matching_series = ArticleSeries.objects.all()


    return render(request = request, template_name='main/home.html', context={'objects': matching_series, 'type': 'series'})

def series(request, series: str):
    matching_articles = Article.objects.filter(series__slug=series).all()

    return render(request, template_name='main/home.html', context={'objects': matching_articles, 'type':'article'})
    
def article(request, series: str, article:str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request=request, template_name='main/article.html', context={'object': matching_article})

def new_series(request):
    return redirect('/')

def new_post(request):
    return redirect('/')

def series_update(request, series):
    return redirect('/')

def series_delete(request, series):
    return redirect('/')

def article_update(request, series, article):
    return redirect('/')

def article_delete(request, series, article):
    return redirect('/')