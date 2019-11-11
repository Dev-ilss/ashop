from django.db import models
# Create your models here.
from django.urls import reverse
 
class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_price = models.CharField(max_length=5)
    product_desc = models.CharField(max_length=100)
    product_image = models.ImageField(default='default.png', upload_to='product_files')
    def __str__(self):
        return f'{self.product_title}'
    # on submit click on the product entry page, it redirects to the url below. 
    def get_absolute_url(self):
        return reverse('shop:index')
