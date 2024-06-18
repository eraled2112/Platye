from django.shortcuts import render
from django.views import generic
from .models import *


class HomePageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['products_hit'] = Product.objects.all().order_by('?'[:4])
        context['products_rec'] = Product.objects.all().order_by('?'[:4])
        return context


class ProductDetailView(generic.DetailView):
    template_name = 'productDetail.html'
    queryset = Product.objects.all()
    model = Product
    context_object_name = 'product'


class AllProducts(generic.TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_products'] = Product.objects.all()


