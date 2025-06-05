from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('gallery/', views.gallery, name='gallery'),
    path('get-quote/', views.get_quote, name='get_quote'),
]