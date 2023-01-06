from django import forms
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase


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


class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class RecipieRequirmentCreateForm(forms.ModelForm):
    model = RecipeRequirment
    fields = "__all__"

class RecipieRequirmentUpdateForm(forms.ModelForm):
    model = RecipeRequirment
    fields = "__all__"


class PurchaseCreateForm(forms.ModelForm):
    model = Purchase
    fields = "__all__"

class PurchaseUpdateForm(forms.ModelForm):
    model = Purchase
    fields = "__all__"

