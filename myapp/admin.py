from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    list_filter = ['category', 'tag']
    search_fields = ['title', 'content']


admin.site.register(Tag)
admin.site.register(Category)

