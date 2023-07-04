from django.db import models
from django.utils import timezone
# modules for tinymce
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
import os


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete= models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.png', upload_to=image_upload_to, max_length=255)

    def __str__(self):
        return f'{self.title}'
    
   

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ['-published']




class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug), instance)
        return None
    
    image = models.ImageField(default='default/no_image.png', upload_to=image_upload_to, max_length=255)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default= '', blank=True)
    article_slug = models.SlugField('Series slug', null=False, blank=False, unique=True)
    #content = models.TextField()
    content = HTMLField(blank=True, default='')
    notes = HTMLField(blank=True, default='')
    published = models.DateTimeField('Date published', default= timezone.now)
    modified = models.DateTimeField('Date modified', default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default='', verbose_name='Series', on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title
    
    @property
    def slug(self):
        return self.series.slug + '/'+ self.article_slug
    
    class Meta:
        verbose_name_plural = 'Article'
        ordering = ['-published']
    



