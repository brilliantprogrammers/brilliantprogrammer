from django.contrib import admin
from django.urls import path,include
from bp.api import views

urlpatterns = [
    path('blog/',views.blog_list),
    path('blog/<slug:slug>',views.blog_detail),
    path('popular_posts/',views.popular_blog_detail),
    path('tags/<slug:slug>',views.search_blog_by_tag),
]