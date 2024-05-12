from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import logging
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import Recipe, Categories, Catalog
from .forms import RecipeForm, CategoryForm

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'cbookapp/index.html')


def about(request):
    logger.info('About page accessed')
    return render(request, 'cbookapp/about.html')


def get_recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes, 'name': 'Рецепты'}
    return render(request, 'cbookapp/recipe.html', context)


def get_recipe(request):
    recipe = Recipe.objects.all()
    context = {'recipe': recipe, 'name': 'Рецепты'}
    return render(request, 'cbookapp/recipe.html', context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = Categories(name=name)
            category.save()
            return render(request, 'cbookapp/recipe_form.html', {'answer': "Категория добавлена"})
    else:
        form = CategoryForm()
        message = 'Добавить категорию'
    return render(request, 'cbookapp/recipe_form.html', {'form': form, 'message': message})


def get_category(request):
    categories = Categories.objects.all()
    context = {'categories': categories, 'name': 'Категории'}
    return render(request, 'cbookapp/get_category.html', context)


def upd_category(request, cat_name):
    category = Categories.objects.filter(name=cat_name).first()
    if category is not None:
        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                name = form.cleaned_data['name']
                form.save()
                return redirect('get_category')
        else:
            form = CategoryForm(instance=category)
            message = f'Изменить категорию - {cat_name}'
        return render(request, 'cbookapp/recipe_form.html', {'form': form, 'message': message})
    return render(request, 'cbookapp/page_404.html', {'message': cat_name})


# @login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            cooking_time = form.cleaned_data['cooking_time']
            author = form.cleaned_data['author']
            ingredients = form.cleaned_data['ingredients']
            category = form.cleaned_data['category']
            try:
                img_file = form.cleaned_data['img_file']
                # fs = FileSystemStorage()
                # fs.save(img_file.name, img_file)
                recipe = Recipe(name=name, description=description, cooking_steps=cooking_steps,
                                cooking_time=cooking_time,
                                author=author, ingredients=ingredients, category=category, img_file=img_file)
            except:
                recipe = Recipe(name=name, description=description, cooking_steps=cooking_steps,
                                cooking_time=cooking_time, author=author, ingredients=ingredients, category=category)
            # recipe.save()
            # recipe = form.save(commit=False)
            # recipe.author = request.user
            recipe.save()
            return render(request, 'cbookapp/recipe_form.html', {'answer': "Рецепт добавлен"})
    else:
        form = RecipeForm()
        message = 'Добавить рецепт'
    return render(request, 'cbookapp/recipe_form.html', {'form': form, 'message': message})


# @login_required
def get_recipe_by_name(request, name):
    recipe = Recipe.objects.filter(name=name).first()
    if recipe is not None:
        recipe.save()
        context = {'recipe': recipe, 'name': f'Рецепт {name}'}
        return render(request, 'cbookapp/recipe.html', context)
    return render(request, 'cbookapp/page_404.html', {'message': name})


# @login_required
def upd_recipe(request, name):
    recipe = Recipe.objects.filter(name=name).first()
    if recipe is not None:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                name = form.cleaned_data['name']
                form.save()
                return redirect('get_recipe_by_name', name=name)
        else:
            form = RecipeForm(instance=recipe)
            message = f'Внести изменение в рецепт "{name}"'
        return render(request, 'cbookapp/recipe_form.html', {'form': form, 'message': message})
    return render(request, 'cbookapp/page_404.html', {'message': name})
