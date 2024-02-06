from bs4 import BeautifulSoup
import requests 
from concurrent.futures import ThreadPoolExecutor, as_completed 



# Function to scrape a specific site
def scrape_page(page_number,location,transaction,number_of_rooms):
    url = f"https://www.olx.pl/nieruchomosci/mieszkania/{transaction}/{location}/?page={page_number}/&search%5Bfilter_enum_rooms%5D%5B0%5D={number_of_rooms}"
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    titles = soup.find_all("h6", attrs={"class":"css-16v5mdi er34gjf0"})
    prices = soup.find_all("p",attrs={"data-testid":"ad-price","class":"css-10b0gli er34gjf0"})
    location_of_offer = soup.find_all("p", attrs={"data-testid":"location-date","class":"css-1a4brun er34gjf0"})
    link_to_offer_unfiltered = soup.find_all("a",attrs={"class":"css-rc5s2u"})
    link_to_offer = ["https://olx.pl/" + link['href'] for link in link_to_offer_unfiltered]

    
    data = [(title.text.strip(), price.text.strip(), location.text.strip(), link) \
        for title, price, location, link in zip(titles, prices, location_of_offer, link_to_offer)]


    return data

# Function to scrape multiple sites

def scrape_multiple_pages(start_page, end_page,location,price,keyword,area,price_per_sqm,sorting,transaction,number_of_rooms):
    offers_data = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_page = {executor.submit(scrape_page, page_number,location,transaction,number_of_rooms): page_number for page_number in range(start_page, end_page + 1)}
        for future in as_completed(future_to_page): 
            page_number = future_to_page[future]
            try:
                data = future.result()
                for title, price,location,link in data:
                    offers_data.append((title, price,location,link))
            except Exception as exc:
                print(f"Strona {page_number} zgłosiła wyjątek: {exc}")

    return offers_data

scrape_multiple_pages(1,2,"warszawa","","","","","","wynajem","one")
