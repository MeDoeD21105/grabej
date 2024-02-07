from django.contrib import admin

from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
     list_display = ("title","slug", "content", "price", "quantity", "sellerr")
     prepopulated_fields = {"slug": ("title", )}

admin.site.register(Product, ProductAdmin)

admin.site.register(Seller)
