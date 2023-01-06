from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, RecipeRequirment, Purchase

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirment)
admin.site.register(Purchase)