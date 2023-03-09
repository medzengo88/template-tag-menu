from django.shortcuts import render


def menu_list(request):
    return render(request, 'shop/index.html')


def punkt_menu(request, menu_slug):
    return render(request, 'shop/menu.html', {'menu_slug': menu_slug})
