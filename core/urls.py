from django.urls import path
from .views import HomePageView, ItemDetailView


urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('product/<int:pk>/',ItemDetailView.as_view(),name='product'),
]