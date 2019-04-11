from django.shortcuts import render
from django.http import HttpResponse # Make string to html

# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs) # REQUEST
    print(request.user) # USER NAME
    return HttpResponse("<h1>Hello World!</h1>") # string of HTML code

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")



def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")    