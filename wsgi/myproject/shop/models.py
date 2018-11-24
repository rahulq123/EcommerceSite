from django.db import models
from django.core.urlresolvers import reverse


# creates the member model in the database to store user information

class Member(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.username

# creates the model of the product category name and slug in the database
# this is will be displayed on the website of the left hand side on the product page
		
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

def __str__(self):
    return self.name

	
	
# creates product model to store the information about the product in the database to display on the website

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'),)

def __str__(self):
    return self.name
