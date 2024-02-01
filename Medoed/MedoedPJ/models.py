from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название")
    content = models.TextField(verbose_name = "Описание")
    photo = models.ImageField(upload_to = "photos/ ",blank = True, verbose_name = "Фото")
    price = models.DecimalField( max_digits = 7, decimal_places = 2, verbose_name = "Цена")
    quantity = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)], verbose_name = "Количество")
    