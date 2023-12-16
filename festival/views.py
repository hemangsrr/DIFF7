# Assuming this is your Django app's views.py file

from django.shortcuts import render

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def elements_view(request):
    return render(request, 'elements.html')

def guests_view(request):
    return render(request, 'guests.html')

def index_view(request):
    return render(request, 'index.html')

def main_view(request):
    return render(request, 'main.html')

def program_view(request):
    return render(request, 'Program.html')

def single_blog_view(request):
    return render(request, 'single-blog.html')

def venue_view(request):
    return render(request, 'venue.html')
