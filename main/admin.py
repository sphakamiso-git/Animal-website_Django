from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
            'title',
               'subtitle',
                 'slug', 
                 #'published'
                 'author',
                 'image'
                 ]

class ArtitleAdmin(admin.ModelAdmin):
    fieldsets = [('header',{'fields':['title', 'subtitle', 'article_slug', 'series', 'author','image']}),
                ('Content',{'fields':['content', 'notes']}),
                ('Date', {'fields':['modified']})
    ]


admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArtitleAdmin)