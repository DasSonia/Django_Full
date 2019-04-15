from django.shortcuts import render

from .models import Product
# Create your views here.
from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # RE-RENDER IT 

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

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
