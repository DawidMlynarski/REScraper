from bs4 import BeautifulSoup
import requests 
from concurrent.futures import ThreadPoolExecutor, as_completed 



# Function to scrape a specific site
def scrape_page(page_number):
    url = f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={page_number}"
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    titles = soup.find_all("h6", attrs={"class":"css-16v5mdi er34gjf0"})
    prices = soup.find_all("p",attrs={"data-testid":"ad-price","class":"css-10b0gli er34gjf0"})
    
    data = [(title.text.strip(), price.text.strip()) for title, price in zip(titles, prices)]
    return data

# Function to scrape multiple sites

def scrape_multiple_pages(start_page, end_page):
    offers_data = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_page = {executor.submit(scrape_page, page_number): page_number for page_number in range(start_page, end_page + 1)}
        for future in as_completed(future_to_page): 
            page_number = future_to_page[future]
            try:
                data = future.result()
                for title, price in data:
                    offers_data.append((title, price))
            except Exception as exc:
                print(f"Strona {page_number} zgłosiła wyjątek: {exc}")

    return offers_data


