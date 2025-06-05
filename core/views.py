from django.shortcuts import render
from .models import Photo, Category

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
            return redirect('home')
    else:
        form = QuoteRequestForm()
    return render(request, 'core/get_quote.html', {'form': form})