from distutils import text_file
from enum import unique
from pickle import TRUE
from django.db import models
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from category.models import Category

class Post(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish'),
    )
    title = models.CharField(_("title"), max_length=50)
    slug = models.SlugField(_("slug"), unique=True, blank=True)
    desciption = models.TextField(_('desciption'))
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    tags = TaggableManager()
    status = models.CharField(_("status"), max_length=10, choices=STATUS_CHOICES)
    create_at = models.DateTimeField(_("create at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    
    
    def __str__(self):
        return self.title
