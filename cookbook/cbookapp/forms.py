from django import forms
from .models import Categories, Recipe


# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=20, label='Категория')
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        labels = {'name': 'Категория'}

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': 'Введите категорию'})


# class RecipeForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Название блюда', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Шашлык'}))
#     description = forms.CharField(label='Описание', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Свинной шашлык на углях'}))
#     cooking_steps = forms.CharField(label='Шаги приготовления', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '1. Нарезать мясо, 2. Замариновать'}))
#     cooking_time = forms.CharField(max_length=15, label='Время приготовления', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '120 минут'}))
#     img_file = forms.ImageField(label='Изображение', required=False,
#                                 widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Bзображение'}))
#     author = forms.CharField(max_length=100, label='Автор рецепта', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Егор'}))
#     ingredients = forms.CharField(label='Ингредиенты', widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Мясо, Лук, Соль, ...'}))
#     category = forms.ModelChoiceField(label='Категория', queryset=Categories.objects.all(),
#                                       empty_label='Категория не выбрана')


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'img_file', 'author', 'ingredients',
                  'category']
        labels = {'name': 'Название блюда', 'description': 'Описание', 'cooking_steps': 'Шаги приготовления',
                  'cooking_time': 'Время приготовления', 'img_file': 'Изображение', 'author': 'Автор рецепта',
                  'ingredients': 'Ингредиенты', 'category': 'Категория'}
        # field_classes = {
        #     'category': forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label='Категория не выбрана')}

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Шашлык'})
        self.fields['description'].widget = forms.TextInput(attrs={'placeholder': 'Свинной шашлык на углях'})
        self.fields['cooking_steps'].widget = forms.TextInput(attrs={'placeholder': '1. Нарезать мясо, 2. ...'})
        self.fields['cooking_time'].widget = forms.TextInput(attrs={'placeholder': '120 минут'})
        self.fields['img_file'].widget = forms.FileInput(attrs={'placeholder': 'Bзображение'})
        self.fields['author'].widget = forms.TextInput(attrs={'placeholder': 'Имя автора'})
        self.fields['ingredients'].widget = forms.TextInput(attrs={'placeholder': 'Мясо, Лук, Соль, ...'})
