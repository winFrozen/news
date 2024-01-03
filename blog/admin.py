from django.contrib import admin
from .models import New, Trandingnews, Categorynews, Singlenews, Comments, Indexnews, News, Contact, Newsletter, Comment, Products

@admin.register(Categorynews)
class Categorynews(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
@admin.register(New)
class New(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
@admin.register(Trandingnews)
class Trandingnews(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Comments)
class Comments(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
@admin.register(Singlenews)
class Singlenews(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
@admin.register(Indexnews)
class Indexnewsadmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    list_filter = ['data']
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'slug']
    list_filter = ['status', 'created_time']

admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Comment)

@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['price']
    prepopulated_fields = {'slug': ('name',)}