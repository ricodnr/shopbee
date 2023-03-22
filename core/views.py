from django.shortcuts import render
from .models import ShopeeItem
from django.views.generic import ListView,DetailView
# Create your views here.


class HomePageView(ListView):
    template_name = "home.html"
    model = ShopeeItem

class ItemDetailView(DetailView):
    template_name='product.html'
    model = ShopeeItem