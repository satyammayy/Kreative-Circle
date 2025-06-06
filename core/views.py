from django.shortcuts import render
from .models import Photo, Category
from .forms import QuoteRequestForm
from django.shortcuts import render, redirect

def home(request):
    featured_photos = Photo.objects.filter(is_featured=True).order_by('-uploaded_at')[:5]
    photos = Photo.objects.all().order_by('-uploaded_at')
    categories = Category.objects.all()
    
    return render(request, 'core/home.html', {
        'featured_photos': featured_photos,
        'photos': photos,
        'categories': categories
    })

def about(request):
    return render(request, 'core/about.html')

def features(request):
    return render(request, 'core/features.html')

def gallery(request):
    category_id = request.GET.get('category')
    photos = Photo.objects.all()
    if category_id:
        photos = photos.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'core/gallery.html', {
        'photos': photos,
        'categories': categories,
        'selected_category': category_id
    })

def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # redirect after successful save
    else:
        form = QuoteRequestForm()

    return render(request, 'core/get_quote.html', {'form': form})

# Add to your imports
from django.shortcuts import render

def loading(request):
    photos = Photo.objects.all()
    image_urls = [photo.image.url for photo in photos]
    return render(request, 'core/loading.html', {'image_urls': image_urls})

def quote_thanks(request):
    return render(request, 'core/quote_thanks.html')

    