from django.shortcuts import render

from .models import Product
# Create your views here.
from .forms import ProductForm

def product_create_view(request):
    # FOR POST  {% csrf_token %} SECURITY IS NEEDED
    #print(request.GET)
    #print(request.GET['title'])
    #print(request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)
        # Product.objects.create(title=my_new_title)    
    context = {
        
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm() # RE-RENDER IT 

#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_details.html", context) 
