from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.CharField(max_length=15)
    img_file = models.ImageField(upload_to='media/products/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Пользователь", null=True)
    ingredients = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'name: {self.name}, cooking_time: {self.cooking_time}'


class Catalog(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

