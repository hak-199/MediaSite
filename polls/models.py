from django.db import models
from django.urls import reverse


class Categories(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150)
	public = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name}"

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def get_absolute_url(self):
		return reverse("category",kwargs={'cat_slug':self.slug})



class News(models.Model):
	category = models.ForeignKey(Categories,on_delete=models.CASCADE, verbose_name='Main Category', related_name='main')
	aditional_category = models.ManyToManyField(Categories,blank=True,verbose_name='Aditional Category',related_name='aditional')
	name = models.CharField(max_length=300)
	slug = models.SlugField(max_length=350,unique=True)
	text = models.TextField(max_length=10000)
	date = models.DateTimeField(auto_now=True)
	photo = models.ImageField(upload_to='photos')
	public = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.id} {self.name}"

	class Meta:
		verbose_name = 'News'
		verbose_name_plural = 'Posts'
