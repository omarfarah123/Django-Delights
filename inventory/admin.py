from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, RecipieRequirment, Purchase

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipieRequirment)
admin.site.register(Purchase)