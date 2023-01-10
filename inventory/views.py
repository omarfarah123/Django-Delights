from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
# Create your views here.



def logout_view(request):
  logout(request)
  return redirect("home")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class HomeView(LoginRequiredMixin, TemplateView): 
    template_name = "inventory/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()
        context["menuitems"] = MenuItem.objects.all()
        context["reciperequirments"] = RecipeRequirment.objects.all()
        return context

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientCreateForm

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientUpdateForm

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/ingredients"

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu_items.html"

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemCreateForm

class MenuItemUpdateView(LoginRequiredMixin,UpdateView):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItemUpdateForm

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menu_item.html"
    success_url = "/menu_items"

class RecipeRequirmentListView(LoginRequiredMixin, ListView):
    model = RecipeRequirment
    template_name = "inventory/recipe_requirments.html"

class RecipeRequirmentCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirment
    template_name = "inventory/add_recipe_requirment.html"
    form_class = RecipeRequirmentCreateForm

class RecipeRequirmentUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirment
    template_name = "inventory/update_recipe_requirment.html"
    form_class = RecipeRequirmentUpdateForm

class RecipeRequirmentDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirment
    template_name = "inventory/delete_recipe_requirment.html"
    success_url = "/reciperequirments"

class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases.html"

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseCreateForm

class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseUpdateForm

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    success_url = "/purchases"

@login_required
def profit_vs_revenue(request):
    revenue = 0
    purchase = Purchase.objects.all()
    for item in purchase:
        revenue += item.menu_item.price
    context = {
        "revenue": revenue
    }
    return render(request, 'inventory/profitvsrevenue.html', context)


