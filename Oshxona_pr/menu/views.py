from django.shortcuts import render
from .models import Menu, Category

def menu_list(request):
    categories = Category.objects.all()
    menus = Menu.objects.all()

    return render(request, 'menu.html', {
        'categories': categories,
        'menus': menus
    })