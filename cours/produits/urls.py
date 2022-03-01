
from django.urls import path, re_path
from . import views

app_name = 'produits'

urlpatterns = [

    # path('create/', views.produit_create, name='produit_create'),

    path('', views.produit_list, name='produit_list'),

    path('<id>', views.produit_detail, name='produit_detail'),

    path('update/<id>', views.produit_update, name='produit_update'),

    # re_path(r'^(?P<pk>\d+)/delete/$', views.produit_delete, name='produit_delete'),

]