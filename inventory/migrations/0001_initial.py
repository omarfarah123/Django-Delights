# Generated by Django 4.1.4 on 2023-01-02 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('quantity', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('unit', models.CharField(choices=[('tbsp', 'Tablespoon'), ('tsp', 'Teaspoon'), ('oz', 'Ounce'), ('fl. oz', 'Fluid Ounce'), ('c', 'Cup'), ('qt', 'Quart'), ('pint', 'Pint'), ('gal', 'Gallon'), ('lbs', 'Pound'), ('ml', 'Milliliter'), ('g', 'Gram'), ('kg', 'Kilogram'), ('l', 'Liter')], default='nonunit', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='RecipieRequirment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, default=0.0, max_digits=6)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem')),
            ],
        ),
    ]