from .models import Produit
from django import forms

class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = "__all__"


class ProduitQForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = ('quantity',)