from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    year = forms.IntegerField(label='Год рождения')


class BookForm(forms.Form):
    title = forms.CharField(label='Название')
    genre = forms.CharField(label='Жанр')
    year = forms.IntegerField(label='Год')
    annotation = forms.CharField(label='Аннотация')
