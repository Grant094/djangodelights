from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def home(request):
    return render(request, "inventory/home.html")

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientCreateForm
    template_name = "inventory/ingredient_create_form.html"

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientUpdateForm
    template_name = "inventory/ingredient_update_form.html"

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = "inventory/menuitem_create_form.html"

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemUpdateForm
    template_name = "inventory/menuitem_update_form.html"

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementCreateForm
    template_name = "inventory/reciperequirement_create_form.html"

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseCreateForm
    template_name = "inventory/purchase_create.html"

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = 0
        total_cost = 0
        for purchase in Purchase.objects.all():
            revenue += purchase.menu_item.price
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.quantity
        
        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context