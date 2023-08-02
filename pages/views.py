from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Repair
from django.http import Http404
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'pages/home.html')
def about(request):
    return render(request, 'pages/about.html')
@login_required(redirect_field_name='login')
def sale(request):
    products = Product.objects.all()
    context = {
        'products': products
        }
    return render(
        request,
        'pages/sale.html',
        context
    )

def sale_detail(request, pk, slug):
    try:
        product = Product.objects.get(id=pk, slug=slug)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product': product
    }
    return render(
        request,
        'pages/sale_detail.html',
        context
    )
def sale_delete(request, pk, slug):
    product = Product.objects.get(id=pk, slug=slug)
    product.delete()
    return redirect(to='sale')

def sale_update(request, pk, slug):
    product = Product.objects.get(id=pk, slug=slug)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            condition = form.cleaned_data['condition']

            product.title = title
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.condition = condition
            product.save()

            return redirect(to='sale')
    context = {
        'form': form
    }

    return render(request, 'pages/update.html', context)


@login_required(redirect_field_name='login')
def repairs(request):
    repairs = Repair.objects.all()
    context = {'repairs': repairs}
    return render(
        request,
        'pages/repairs.html',
        context
    )
def repair_detail(request, pk):
    try:
        repair = Repair.objects.get(id=pk)
    except Repair.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'repair': repair
    }
    return render(
        request,
        'pages/repair_detail.html',
        context
    )

@login_required(redirect_field_name='login')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='sale')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)
def aboutme(request):
    return render(request, 'pages/aboutme.html')
