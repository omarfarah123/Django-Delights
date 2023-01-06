from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
# Create your views here.
class HomeView(TemplateView): 
    template_name = "inventory/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["Ingredient"] = Ingredient.objects.all()
        context["MenuItem"] = MenuItem.objects.all()
        context["RecipeRequirment"] = RecipeRequirment.objects.all()
        return context

class IngredientListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientCreateForm

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientUpdateForm

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "inventory/ingredients.html"

class MenuItemListView(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"

class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemCreateForm

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItemUpdateForm

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menu_item.html"
    success_url = "inventory/menu.html"

class RecipeRequirmentListView(ListView):
    model = RecipeRequirment
    template_name = "inventory/recipie_requirments.html"

class RecipeRequirmentCreateView(CreateView):
    model = RecipeRequirment
    template_name = "inventory/add_recipe_requirment.html"
    form_class = RecipieRequirmentCreateForm

class RecipeRequirmentUpdateView(UpdateView):
    model = RecipeRequirment
    template_name = "inventory/update_recipe_requirment.html"
    form_class = RecipieRequirmentUpdateForm

class RecipeRequirmentDeleteView(DeleteView):
    model = RecipeRequirment
    template_name = "inventory/delete_recipe_requirment.html"

class PurchaseListView(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseCreateForm

class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseUpdateForm

class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    success_url = "inventory/purchases.html"

def profit_vs_revenue(request):
    revenue = 0
    purchase = Purchase.objects.all()
    for item in purchase:
        revenue += item.menu_item.price
    context = {
        "revenue": revenue
    }
    return render(request, 'inventory/profitvsrevenue.html', context)


