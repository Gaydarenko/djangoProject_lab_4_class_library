from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    year = forms.IntegerField(label='Год рождения')


class BookForm(forms.Form):
    # author = forms.ModelChoiceField
    title = forms.CharField(label='Название')
    genre = forms.CharField(label='Жанр')
    year = forms.IntegerField(label='Год')
    annotation = forms.CharField(label='Аннотация')


class SearchForm(forms.Form):
    title = forms.CharField(label='Название', required=False)
    genre = forms.CharField(label='Жанр', required=False)
    year = forms.IntegerField(label='Год', required=False)

