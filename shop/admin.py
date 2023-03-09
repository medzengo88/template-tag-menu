from django.contrib import admin

from .models import *


class PodPunktMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'podpunkt_name', 'punktmen', 'slug', 'is_published')
    list_display_links = ('id', 'podpunkt_name')
    list_editable = ('is_published',)
    search_fields = ('podpunkt_name',)
    prepopulated_fields = {'slug': ('podpunkt_name',)}


class PunktMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'punkt_name', 'men', 'slug', 'is_published')
    list_display_links = ('id', 'punkt_name')
    list_editable = ('is_published',)
    search_fields = ('punkt_name',)
    prepopulated_fields = {'slug': ('punkt_name',)}


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_name', 'cat', 'is_published')
    list_display_links = ('id', 'menu_name')
    list_editable = ('is_published',)
    search_fields = ('menu_name',)
    prepopulated_fields = {'slug': ('menu_name',)}


class CatalogMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'catalog_name', 'is_published')
    list_display_links = ('id', 'catalog_name')
    list_editable = ('is_published',)
    search_fields = ('catalog_name',)


admin.site.register(PodPunktMenu, PodPunktMenuAdmin)
admin.site.register(PunktMenu, PunktMenuAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(CatalogMenu, CatalogMenuAdmin)
