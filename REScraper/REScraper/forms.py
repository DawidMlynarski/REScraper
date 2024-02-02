# forms.py
from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='Miejscowość', required=False)
    price = forms.DecimalField(label='Cena', required=False)
    keyword = forms.CharField(label='Szukana fraza', required=False)
    area = forms.DecimalField(label='Metraż', required=False)
    price_per_sqm = forms.DecimalField(label='Cena za metr kwadratowy', required=False)
    sorting_choices = [
        ('cena_rosnaco', 'Cena rosnąco'),
        ('cena_malejaco', 'Cena malejąco'),
        ('domyslne', 'Domyślne'),
    ]
    sorting = forms.ChoiceField(label='Sortowanie', choices=sorting_choices, initial='domyslne')
