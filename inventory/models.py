from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=30, blank=True)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.quantity) + " " + self.ingredient.unit + " " + self.ingredient.name + " for " + self.menu_item.title

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item.title + " at " + str(self.timestamp)