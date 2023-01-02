from django.db import models

# Create your models here.
class Ingredient(models.Model):
    TABLESPOON = "tbsp"
    TEASPOON = "tsp"
    OUNCE = "oz"
    FLUIDOUNCE = "fl. oz"
    CUP = "c"
    QUART = "qt"
    PINT = "pint"
    GALLON = "gal"
    POUND = "lbs"
    MILLILITER = "ml"
    GRAM = "g"
    KILOGRAM = "kg"
    LITER = "l"
    NONUNIT = "nonunit"

    UNIT_CHOICES = [
        (TABLESPOON, "Tablespoon"),
        (TEASPOON, "Teaspoon"),
        (OUNCE, "Ounce"),
        (FLUIDOUNCE, "Fluid Ounce"),
        (CUP, "Cup"),
        (QUART, "Quart"),
        (PINT, "Pint"),
        (GALLON, "Gallon"),
        (POUND, "Pound"),
        (MILLILITER, "Milliliter"),
        (GRAM, "Gram"),
        (KILOGRAM, "Kilogram"),
        (LITER, "Liter")
    ]

    name = models.CharField(max_length=25)
    quantity = models.DecimalField(default=0)
    unit = models.CharField(max_length=8, choices=UNIT_CHOICES, default=NONUNIT)
    