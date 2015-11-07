from django.contrib import admin
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes')
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url', 'views']
    list_display = ('category', 'title', 'url')
    search_fields = ['title']

admin.site.register(Page, PageAdmin)