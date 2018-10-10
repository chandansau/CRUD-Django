from django.shortcuts import render,redirect
from .models import products
from .forms import ProductForm

def list_product(request):
    product=products.objects.all()
    return render(request,'product.html',{'product': product})

def create_product(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_product')
    return render(request,'product-form.html',{'form':form})
def update_product(request,id):
    product=products.objects.get(id=id)
    form=ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_product')
    return render(request,'product-form.html',{'form':form,'product':product})

def delete_product(request,id):
    product=products.objects.get(id=id)
    if request.method=='POST':
        product.delete()
        return redirect('list_product')
    return render(request,'product-delete-form.html',{'product':product})
