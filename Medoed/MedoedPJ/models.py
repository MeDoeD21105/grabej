from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название")
    content = models.TextField(verbose_name = "Описание")
    photo = models.ImageField(upload_to = "photos/ ",blank = True, verbose_name = "Фото")
    price = models.DecimalField( max_digits = 7, decimal_places = 2, verbose_name = "Цена")
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)], verbose_name = "Количество")
    sellerr = models.ForeignKey("Seller", on_delete = models.PROTECT, null = True,)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, blank = True, null = True)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug })
    
    def __str__(self):
        return self.title
    
class Seller(models.Model):
    name = models.CharField(max_length=100, db_index=True )
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name