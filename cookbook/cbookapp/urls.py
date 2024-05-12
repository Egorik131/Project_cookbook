from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('all_recipes/', views.get_recipes, name='all_recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('get_recipe/<str:name>/', views.get_recipe_by_name, name='get_recipe_by_name'),
    path('upd_recipe/<str:name>/', views.upd_recipe, name='upd_recipe'),
    path('add_category/', views.add_category, name='add_category'),
    path('get_category/', views.get_category, name='get_category'),
    path('upd_category/<str:cat_name>/', views.upd_category, name='upd_category'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),

]


