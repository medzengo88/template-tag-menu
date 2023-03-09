from django.db import models
from django.urls import reverse


class PodPunktMenu(models.Model):
    podpunkt_name = models.CharField(max_length=100, verbose_name='Название подпункта меню')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL подпункта')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    punktmen = models.ForeignKey('PunktMenu', on_delete=models.PROTECT, verbose_name='Пункт меню')

    def __str__(self):
        return self.podpunkt_name

    class Meta:
        verbose_name = 'Подпункт меню'
        verbose_name_plural = 'Подпункты меню'


class PunktMenu(models.Model):
    punkt_name = models.CharField(max_length=100, db_index=True, verbose_name='Название пункта меню')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL пункта меню')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    men = models.ForeignKey('Menu', on_delete=models.PROTECT, verbose_name='Меню')

    def __str__(self):
        return self.punkt_name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Menu(models.Model):
    menu_name = models.CharField(max_length=100, db_index=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL меню')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('CatalogMenu', on_delete=models.PROTECT, verbose_name='Каталог меню')

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse('menu_list', kwargs={'menu_slug': self.slug})


class CatalogMenu(models.Model):
    catalog_name = models.CharField(max_length=100, db_index=True, verbose_name='Название каталога меню')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.catalog_name

    class Meta:
        verbose_name = 'Каталог меню'
        verbose_name_plural = 'Каталог меню'
