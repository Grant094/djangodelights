from django import forms
from .models import *

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["menu_item"]