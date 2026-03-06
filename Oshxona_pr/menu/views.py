from django.shortcuts import render, get_object_or_404
from .models import Category, Menu


def categories(request):
    categories = Category.objects.all()
    return render(request, 'menu/categories.html', {'categories': categories})


def category_menu(request, slug):
    category = get_object_or_404(Category, slug=slug)
    menus = Menu.objects.filter(category=category)

    return render(request, 'menu/category_menu.html', {
        'category': category,
        'menus': menus
    })