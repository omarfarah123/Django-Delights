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
    quantity = models.DecimalField(decimal_places=1, max_digits=5, default=0)
    unit = models.CharField(max_length=8, choices=UNIT_CHOICES, default=NONUNIT)

    def __str__(self):
        return f"Ingredient {self.name} Quantity In Stock {self.quantity} {self.unit}"

class MenuItem(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)
    
    def __str__(self):
        return f"Title {self.title} Price {self.price}"

class RecipieRequirment(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=1, max_digits=6, default=0.0)
    def __str__(self):
        return f"Menu Item {self.menu_item} Ingredient {self.ingredient} Quantity Required for {self.menu_item} {self.quantity}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Menu Item Purchased {self.menu_item} at {self.timestamp}"

 