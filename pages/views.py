from django.shortcuts import render
from django.http import HttpResponse # Make string to html

# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hello World</h1>") # string of HTML code