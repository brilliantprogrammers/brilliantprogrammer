from django.contrib import admin
from django.urls import path,include
from bp.api import views

urlpatterns = [
    path('blog/',views.blog_list),
    path('blog/<int:pk>',views.blog_detail)
]