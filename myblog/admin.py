from django.contrib import admin
from .models import Article, Category, Tag
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'create_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'modify_time']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'modify_time']