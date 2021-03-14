from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='слаг')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:by_category_slug', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='слаг')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='изображение')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    stock = models.PositiveIntegerField(verbose_name='остаток товара')
    available = models.BooleanField(default=True, verbose_name='наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='добавлен')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлён')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
