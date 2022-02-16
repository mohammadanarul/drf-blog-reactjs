from django.urls import path
from .views import (
    blog_post_list,
    create_blog_post,
    partiali_update_blog_post,
    update_blog_post,
)

urlpatterns = [
    path('blog-post/', blog_post_list),
    path('create-blog-post/', create_blog_post),
    path('update-blog-post/<int:pk>/', update_blog_post),
    path('partiali-update-blog-post/<int:pk>/', partiali_update_blog_post),
]
