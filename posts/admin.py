from django.contrib import admin
from posts.models import Post, Category, Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'rate', 'author']
    search_fields = ['title', 'content']
    list_filter = ['category']
    list_editable = ['rate', 'author']
admin.site.register(Category)
admin.site.register(Tag)