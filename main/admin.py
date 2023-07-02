from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
            'title',
               'subtitle',
                 'slug', 
                 #'published'
                 ]

class ArtitleAdmin(admin.ModelAdmin):
    fieldsets = [('header',{'fields':['title', 'subtitle', 'article_slug', 'series']}),
                ('Content',{'fields':['content', 'notes']}),
                ('Date', {'fields':['modified']})
    ]


admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArtitleAdmin)