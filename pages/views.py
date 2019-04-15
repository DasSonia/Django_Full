from django.shortcuts import render
from django.http import HttpResponse # Make string to html

# Create your views here.

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs) # REQUEST
    print(request.user) # USER NAME
    #return HttpResponse("<h1>Hello World!</h1>") # string of HTML code
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request,"contact.html",{})



def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_text": "This is about us text",
        "my_number": 123,
        "this_is_true": True,
        "my_list": [1313, 4231, 312, "Abc list"]

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Socail Page</h1>")    
    return render(request,"social.html",{})