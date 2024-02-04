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
            price = form.cleaned_data['price']
            keyword = form.cleaned_data['keyword']
            area = form.cleaned_data['area']
            price_per_sqm = form.cleaned_data['price_per_sqm']
            sorting = form.cleaned_data['sorting']

            # Wywołaj funkcję do scrapowania stron
            offers_data = scrape_multiple_pages(1,2,location, price, keyword, area, price_per_sqm, sorting)

            # Przekazanie danych do szablonu HTML
            return render(request, 'offers.html', {'offers_data': offers_data})
    else:
        form = SearchForm()
    return render(request, "search.html", {'form': form})


def index(request):
    return render(request, 'index.html')

# def offers(request):

#     # Wywołaj funkcję do scrapowania stron
#     offers_data = mieszkania.scrape_multiple_pages(1, 2)
#     for title, price in offers_data:
#         print(title + price)

#     # Przekazanie danych do szablonu HTML
#     return render(request, 'offers.html', {'offers_data': offers_data})
