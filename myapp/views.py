from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, CreateView, UpdateView,ListView
from .models import Product
from .forms import ProductForm


# Create your views here.

class Insert_product(FormView):
    form_class = ProductForm
    template_name = 'insert-product.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('product-list'))

class Product_list(ListView):
    model = Product
    template_name = 'product-list.html'

