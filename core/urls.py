from django.urls import path
from . import views

urlpatterns = [
    # Add to your url patterns

    path('', views.loading, name='loading'),  # Make this the root URL
    path('home/', views.home, name='home'),  # Make this the root URL
    path('home/', views.home, name='home'),   # Move home to /home/
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('gallery/', views.gallery, name='gallery'),
    path('get-quote/', views.get_quote, name='get_quote'),
    path('quote-thanks/', views.quote_thanks, name='success_page'),
]