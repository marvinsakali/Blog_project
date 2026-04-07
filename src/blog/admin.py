from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'date_posted']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
