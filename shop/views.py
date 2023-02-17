from django.shortcuts import render, get_object_or_404
from .models import Category, Product, OilType, Viscosity, Compound, Fuel

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    oiltype = OilType.objects.all()
    viscosity = Viscosity.objects.all()
    compound = Compound.objects.all()
    fuel = Fuel.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)

    data = {
        'category': category,
        'categories': categories,
        'oiltype': oiltype,
        'viscosity': viscosity,
        'compound': compound,
        'fuel': fuel,
        'products': products
    }
    return render(request, 'shop/product/list.html', data)

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html', {'product': product })
