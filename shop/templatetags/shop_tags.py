from django import template
from shop.models import *

register = template.Library()


@register.inclusion_tag('templates_menu/list_menu.html')
def draw_menu(catalog_name):
    mens = Menu.objects.filter(cat__catalog_name=catalog_name, is_published=True)
    return {'mens': mens}


@register.inclusion_tag('templates_menu/list_punkt_menu.html')
def show_menu(menu_slug):
    pods = PodPunktMenu.objects.select_related('punktmen').values(
        'podpunkt_name',
        'punktmen__punkt_name',
        'punktmen__men__menu_name',
        'punktmen__men__slug').filter(punktmen__men__slug=menu_slug, is_published=True)
    return {'pods': pods, 'menu_slug': menu_slug}
