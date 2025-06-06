from django.contrib import admin
from .models import Photo, Category, QuoteRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'uploaded_at')
    list_filter = ('category', 'is_featured', 'uploaded_at')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'category')
        }),
        ('Featured Options', {
            'fields': ('is_featured',),
            'description': 'For best display in the Latest Works section, featured photos should ideally have a 16:9 aspect ratio.'
        })
    )
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'submitted_at')
    search_fields = ('name', 'email', 'project_type')
