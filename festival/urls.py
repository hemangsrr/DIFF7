# Assuming this is your Django app's urls.py file

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('elements/', views.elements_view, name='elements'),
    path('guests/', views.guests_view, name='guests'),
    path('', views.index_view, name='index'),
    path('main/', views.main_view, name='main'),
    path('program/', views.program_view, name='program'),
    path('single-blog/', views.single_blog_view, name='single_blog'),
    path('venue/', views.venue_view, name='venue'),
]