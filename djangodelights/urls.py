"""
URL configuration for djangodelights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
    path('ingredients', views.IngredientList.as_view(), name="ingredients"),
    path('ingredient/create', views.IngredientCreate.as_view(), name="ingredientcreate"),
    path('ingredient/<pk>/update', views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path('ingredient/<pk>/delete', views.IngredientDelete.as_view(), name='ingredient_delete'),
    path('menuitems', views.MenuItemList.as_view(), name="menuitems"),
    path('menuitem/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path('menuitem/<pk>/update', views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name="reciperequirementcreate"),
    path('purchases', views.PurchaseList.as_view(), name="purchases"),
    path('purchase/create', views.PurchaseCreate.as_view(), name="purchasecreate"),
    path('report', views.ReportView.as_view(), name="report"),
]
