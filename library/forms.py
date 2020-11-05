from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    year = forms.IntegerField(label='Год рождения')
