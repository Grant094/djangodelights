from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField()
    quantity = models.FloatField(default=0.0)
    unit = models.CharField()
    unit_price = models.FloatField(default=0.0)

class MenuItem(models.Model):
    title = models.CharField()
    price = models.FloatField(default=0.0)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
