from django.shortcuts import render
from .scraper import mieszkania
from .forms import SearchForm
from .scraper.mieszkania import scrape_multiple_pages

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Pobierz dane z formularza
            location = form.cleaned_data['location']
            price_from = form.cleaned_data['price_from']
            price_to = form.cleaned_data['price_to']
            keyword = form.cleaned_data['keyword']
            area_from = form.cleaned_data['area_from']
            area_to = form.cleaned_data['area_to']
            price_per_sqm_from = form.cleaned_data['price_per_sqm_from']
            price_per_sqm_to = form.cleaned_data['price_per_sqm_to']
            sorting = form.cleaned_data['sorting']
            transaction = form.cleaned_data['transaction']
            number_of_rooms = form.cleaned_data['number_of_rooms']

            # Wywołaj funkcję do scrapowania stron
            offers_data = scrape_multiple_pages(1,5,location, keyword, sorting,transaction,number_of_rooms,price_from,price_to,area_from,area_to,price_per_sqm_from,price_per_sqm_to)

            # Przekazanie danych do szablonu HTML
            return render(request, 'offers.html', {'offers_data': offers_data})
    else:
        form = SearchForm()
    return render(request, "search.html", {'form': form})


def index(request):
    return render(request, 'index.html')
