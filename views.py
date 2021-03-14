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


class ProductsByCategorySlug(ListView):
    context_object_name = 'products'
    template_name = 'shop/by_category_slug.html'
    template_name_suffix = '_slug'
    ordering = ['created']

    def get_queryset(self):
        query = Product.objects.get(category=self.kwargs['slug'], available=True)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['current_category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context


class ProductsByAvailable(ListView):
    context_object_name = 'products'
    template_name = 'shop/by_available.html'
    template_name_suffix = '_available'
    ordering = ['created']

    def get_queryset(self):
        query = Product.objects.filter(available=True)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'shop/detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        query = Product.objects.get(id=self.kwargs['id'], slug=self.kwargs['slug'], available=True)
        return query


