from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(label='Miejscowość', required=False)
    price_from = forms.DecimalField(required=False)
    price_to = forms.DecimalField(required=False)
    area_from = forms.DecimalField(required=False)
    area_to = forms.DecimalField(required=False)
    keyword = forms.CharField(label='Szukana fraza', required=False)
    price_per_sqm_from = forms.DecimalField(required=False)
    price_per_sqm_to = forms.DecimalField(required=False)
    
    sorting_choices = [
        ('price_asc', 'Cena rosnąco'),
        ('price_desc', 'Cena malejąco'),
        ('', 'Domyślne'),
        ('newest', 'Najnowsze'),
    ]
    sorting = forms.ChoiceField(label='Sortowanie', choices=sorting_choices, initial='')

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
