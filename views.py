from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ShopLogo
from django.views.generic import ListView, DetailView, TemplateView


class MainView(TemplateView):
    template_name = 'shop/main.html'


class AllProductListView(ListView):
    queryset = Product.objects.filter(available=True)
    context_object_name = 'products'
    template_name = ''
    template_name_suffix = '_list'
    ordering = ['created']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['shop'] = ShopLogo.objects.first()
        return context

"""
class ProductsByCategorySlug(ListView):
    context_object_name = 'products'
    template_name = 'shop/by_category_slug.html'
    template_name_suffix = '_slug'
    ordering = ['created']

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        query = Product.objects.filter(pk=category.pk, available=True)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['current_category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        return context

"""


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
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'


class AboutUsView(TemplateView):
    template_name = 'shop/about.html'


class ServicesView(TemplateView):
    template_name = 'shop/services.html'


class ContactsView(TemplateView):
    template_name = 'shop/contact.html'
