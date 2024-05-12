from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('all_recipes/', views.get_recipes, name='get_recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('get_recipe/<str:name>/', views.get_recipe_by_name, name='get_recipe_by_name'),
    # path('add_blin/', views.add_recipe, name='add_blin'),
    path('upd_recipe/<str:name>/', views.upd_recipe, name='upd_recipe'),
    path('add_category/', views.add_category, name='add_category'),
    path('get_category/', views.get_category, name='get_category'),
    path('upd_category/<str:cat_name>/', views.upd_category, name='upd_category'),
    # path('', index, name='index'),
    # path('recipes/', recipes, name='recipes'),
    # path('recipe_create/', add_recipe, name='add_recipe'),
    # path('recipe_update/<str:recipe_name>/', update_recipe, name='update_recipe'),
    # path('recipes/<str:recipe_name>/', get_recipes_on_name, name='recipe'),
    # path('categories/', get_categories, name='categories'),
    # path('categories/<str:category>', get_recipes_on_categories, name='category_recipes'),
    # path('category_create/', add_categories, name='add_categories'),
]


