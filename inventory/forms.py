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

class RecipeRequirmentCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirment
        fields = "__all__"

class RecipeRequirmentUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirment
        fields = "__all__"


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

