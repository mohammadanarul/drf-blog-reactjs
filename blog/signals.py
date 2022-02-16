from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Post
from .utils import unique_slug_generator

@receiver(pre_save, sender=Post)
def blog_post_slug(sender, instance, *args, **kwargs):
    if not instance.slug: 
       instance.slug = unique_slug_generator(instance)