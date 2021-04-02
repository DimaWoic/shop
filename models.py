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


class Specials(models.Model):
    special_name = models.CharField(max_length=100, verbose_name='название акции')
    special_activate = models.BooleanField(verbose_name='активация акции', blank=True)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.special_name


class Product(models.Model):
    special = models.ForeignKey(Specials, verbose_name='Акционный товар', on_delete=models.CASCADE,
                                related_name='special', null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='слаг')
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
        return reverse('product_detail', args=[self.id, self.slug])


class ShopLogo(models.Model):
    company_name = models.CharField(max_length=20, verbose_name='название магазина')
    logo_img = models.ImageField(verbose_name='лого магазина')

    class Meta:
        verbose_name = 'Логотип и название магазина'
        verbose_name_plural = 'Логотипы и названия магазина'

    def __str__(self):
        return self.company_name


class GreetingText(models.Model):
    shop_name = models.CharField(max_length=100, verbose_name='название магазина')
    greeting_text = models.TextField(verbose_name='текст приветствия')

    class Meta:
        verbose_name = 'Текст приветствия'
        verbose_name_plural = 'Тексты приветствия'

    def __str__(self):
        return self.shop_name


