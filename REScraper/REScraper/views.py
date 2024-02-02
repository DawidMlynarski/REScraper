from django.shortcuts import render
from .scraper import mieszkania



def index(request):
    return render(request, 'index.html')

def offers(request):

    # Wywołaj funkcję do scrapowania stron
    offers_data = mieszkania.scrape_multiple_pages(1, 2)
    for title, price in offers_data:
        print(title + price)

    # Przekazanie danych do szablonu HTML
    return render(request, 'offers.html', {'offers_data': offers_data})
def search(request):
    return render(request, "search.html")