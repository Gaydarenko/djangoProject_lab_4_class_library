from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    year = forms.IntegerField(label='Год рождения')


class BookForm(forms.Form):
    name = forms.CharField(label='Название')
    surname = forms.CharField(label='Жанр')
    year = forms.IntegerField(label='Год рождения')
    annotation = forms.CharField(label='Аннотация')
