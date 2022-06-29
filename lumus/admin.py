from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    #prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'date_posted']
    list_filter = ['category', 'status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'status', 'date_posted', 'post']
    list_filter = ['author', 'status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)