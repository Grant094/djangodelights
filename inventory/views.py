from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"

class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"