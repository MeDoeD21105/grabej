# Generated by Django 5.0.1 on 2024-02-07 23:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos/ ', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Количество')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('sellerr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='MedoedPJ.seller')),
            ],
        ),
    ]
