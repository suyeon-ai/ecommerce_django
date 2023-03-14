from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    
    class Meta:
        verbose_name_plural = 'categories'
        
    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name


class Product(models.Model):
    # foreign keys
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    
    # to be exposed
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='images/')
    detail_image = models.ImageField(upload_to='images/')
    
    # necessary for operation
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = 'products'
        # listed in descending order by creation date
        ordering = ('-created',)

    def __str__(self):
        return self.product_name