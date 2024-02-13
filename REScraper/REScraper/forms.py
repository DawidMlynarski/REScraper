# forms.py
from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='Miejscowość', required=False)
    price = forms.DecimalField(label='Cena', required=False)
    keyword = forms.CharField(label='Szukana fraza', required=False)
    area = forms.DecimalField(label='Metraż', required=False)
    price_per_sqm = forms.DecimalField(label='Cena za metr kwadratowy', required=False)
    sorting_choices = [
        ('price_asc', 'Cena rosnąco'),
        ('price_desc', 'Cena malejąco'),
        (' ', 'Domyślne'),
        ('newest', 'Najnowsze'),
    ]
    sorting = forms.ChoiceField(label='Sortowanie', choices=sorting_choices, initial='domyslne')

    TRANSACTION_CHOICES = [
        ('wynajem', 'Wynajem'),
        ('sprzedaz', 'Sprzedaż'),
    ]
    transaction = forms.ChoiceField(label='Typ transakcji', choices=TRANSACTION_CHOICES, widget=forms.RadioSelect)
    NUMBER_OF_ROOMS_CHOICES = [
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4 i więcej'),
    ]
    number_of_rooms = forms.ChoiceField(label='Ilość pokoi', choices=NUMBER_OF_ROOMS_CHOICES)