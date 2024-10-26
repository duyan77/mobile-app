from django.db import models


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Product(models.Model):
	# FK
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
								 null=True)  # null=True is added to allow for products without a category
	title = models.CharField(max_length=255)
	brand = models.CharField(max_length=255, default='un-branded')
	description = models.TextField(blank=True)
	slug = models.SlugField(max_length=255, unique=True)
	price = models.DecimalField(max_digits=10, decimal_places=0)
	image = models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = 'products'

	def __str__(self):
		return self.title

	def formatted_price(self):
		return f"{self.price:,.0f}₫"
