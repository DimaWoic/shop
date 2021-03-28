from django.contrib import admin

from .models import Category, Product, ShopLogo, GreetingText, Specials


class GreetingTextAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'greeting_text']


class ShopLogoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'logo_img']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class SpecialAdmin(admin.ModelAdmin):
    list_display = ['special_name', 'special_activate']


admin.site.register(ShopLogo, ShopLogoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(GreetingText, GreetingTextAdmin)
admin.site.register(Specials, SpecialAdmin)
