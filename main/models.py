from django.db import models
from django.utils import timezone
# modules for tinymce
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class ArticleSeries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ['-published']


class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default= '', blank=True)
    article_slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    #content = models.TextField()
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField('Date published', default= timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default='', verbose_name='Series', on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title
    
    @property
    def slug(self):
        return self.series + '/'+ self.article_slug
    
    class Meta:
        verbose_name_plural = 'Article'
        ordering = ['-published']
    



