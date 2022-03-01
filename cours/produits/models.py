# produits/models.py

from django.db import models


class Produit(models.Model):
    name = models.CharField(verbose_name="Produit name", max_length=65, unique=True)
    quantity = models.IntegerField(verbose_name="Produit quantity")
    price = models.IntegerField(verbose_name="Produit price")
    image = models.URLField(verbose_name="Produit image, url", default='https://www.datocms-assets.com/45470/1631795624-logo-django.png')

    def __str__(self):
        return self.name
