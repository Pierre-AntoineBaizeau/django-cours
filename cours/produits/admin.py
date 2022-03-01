from django.contrib import admin

# Register your models here.
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity','image']

admin.site.register(Produit)
