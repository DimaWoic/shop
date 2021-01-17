from django.shortcuts import render
from .models import Category, Product
from django.views.generic import ListView, DetailView


class AllProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'shop/product_list.html'
    template_name_suffix = '_list'
    ordering = ['created']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context