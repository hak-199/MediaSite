from django.contrib import admin
from .models import *
from admin_auto_filters.filters import AutocompleteFilter


class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('id','name','public')
	list_display_links = ('id','name',)
	list_editable = ('public',)
	prepopulated_fields = {"slug":("name",)}





class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','name','category','date','photo','public')
	list_display_links = ('id','name')
	list_editable = ('public',)
	list_filter = ('category','date','public')
	prepopulated_fields = {"slug":("name","category",)}





admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News, NewsAdmin)

