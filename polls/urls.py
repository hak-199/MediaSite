from django.urls import path
from .models import *
from .views import *

urlpatterns = [
	path('',NewsListView.as_view(), name='news'),
	path('post/<slug:slug>/',NewsDetailView.as_view(), name = 'post'),
	path('categories/',NewsCategory.as_view(), name='cat'),
	path('<slug:cat_slug>/',CategoriesListView.as_view(), name='category')
]
