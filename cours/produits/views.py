
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Produit
from .forms import ProduitForm
from .forms import ProduitQForm
from django.http import HttpResponseRedirect


def produit_create(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("produits:produit_list"))
    else:
        form = ProduitForm()

    return render(request, "produits/produit_form.html", { "form": form, })


def produit_list(request):
    produits = Produit.objects.all()
    return render(request, "produits/produit_list.html", { "produits": produits,})


def produit_detail(request, id):
    context ={}
    context["data"] = Produit.objects.get(id = id)
    context["q"] = range(1, context["data"].quantity+1)
    return render(request, "produits/produit_detail.html", context)

def produit_update(request, id):
    quantityChose = request.POST.get('quantity')
    obj = get_object_or_404(Produit, id = id)
    Produit.objects.filter(id = id).update(quantity = obj.quantity - int(quantityChose))
    obj.refresh_from_db()
    return HttpResponseRedirect('/produits')

# def produit_delete(request, pk):
#     produit_obj = get_object_or_404(Produit, pk=pk)
#     produit_obj.delete()
#     return redirect(reverse("produits:produit_list"))
