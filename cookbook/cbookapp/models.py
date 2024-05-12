from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Этапы приготовления')
    cooking_time = models.CharField(max_length=15, verbose_name='Время приготовления, мин.')
    img_file = models.ImageField(upload_to='media/products/', null=True, blank=True, verbose_name='Изображение')
    author = models.CharField(max_length=100, verbose_name='Автор рецепта')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'name: {self.name}, cooking_time: {self.cooking_time}'


class Catalog(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)

