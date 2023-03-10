from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredients'),
    path('ingredients/new', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('ingredients/<pk>/update', views.IngredientUpdateView.as_view(), name='update_ingredient'),
    path('ingredients/<pk>/delete', views.IngredientDeleteView.as_view(), name='delete_ingredient'),
    path('menuitems/', views.MenuItemListView.as_view(), name='menuitems'),
    path('menuitem/new', views.MenuItemCreateView.as_view(), name='add_menuitem'),
    path('menuitem/<pk>/update', views.MenuItemUpdateView.as_view(), name='update_menuitem'),
    path('menuitem/<pk>/delete', views.MenuItemDeleteView.as_view(), name='delete_menuitem'),
    path('purchases/', views.PurchaseListView.as_view(), name='purchases'),
    path('purchases/new', views.PurchaseCreateView.as_view(), name='add_purchase'),
    path('purchases/<pk>/update', views.PurchaseUpdateView.as_view(), name='update_purchase'),
    path('purchases/<pk>/delete', views.PurchaseDeleteView.as_view(), name='delete_purchase'),
    path('reciperequirments/', views.RecipeRequirmentListView.as_view(), name="reciperequirments"),
    path('reciperequirments/new', views.RecipeRequirmentCreateView.as_view(), name="add_reciperequirment"),
    path('reciperequirments/<pk>/update', views.RecipeRequirmentUpdateView.as_view(), name="update_reciperequirment"),
    path('reciperequirments<pk>/delete', views.RecipeRequirmentDeleteView.as_view(), name="delete_reciperequirment"),
    path('finances/', views.profit_vs_revenue, name='finance')
]