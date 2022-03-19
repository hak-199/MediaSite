from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy

class NewsListView(ListView):
	model = News
	# queruset = News.objects.filter(public=True).order_by('date')[4:]
	template_name = 'index.html'
	context_object_name = 'news_home'

	def get_context_data(self,**kwargs):
		context = super(NewsListView,self).get_context_data(**kwargs)
		context['cat'] = Categories.objects.all()
		context['news_main'] = News.objects.filter(public=True).order_by('-date')[:8]
		context['news_more'] = News.objects.filter(public=True).order_by('-date')[8:]
		context['title'] = 'Home Page'
		return context

		
class NewsDetailView(Categories,DetailView):
	model = News
	template_name = 'post.html'
	context_object_name = 'News'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['cat'] = Categories.objects.all()
		context['title'] = str(context['News'].name)
		return context



class NewsCategory(ListView):
	model = News
	template_name = 'categories.html'
	context_object_name = 'category'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = Categories.objects.all()
		context['title'] = 'Categories'
		return context



class CategoriesListView(ListView):
	model = News
	template_name = 'posts.html'
	context_object_name = 'post_category'
	allow_empty = False

	def get_queryset(self):
		return News.objects.filter(category__slug=self.kwargs['cat_slug'], public= True)

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = Categories.objects.all()
		context['title'] = 'Категория - ' + str(context['post_category'][0].category)
		return context

