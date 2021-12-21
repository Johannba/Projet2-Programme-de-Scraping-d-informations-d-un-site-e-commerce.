import csv
from book import extract_url, extract_book_data
import math
from pathlib import Path
import requests

# Récupération de l'url d'un livre

def get_category_book_urls(category_urls):
    category_book_urls = []
    for category_url in category_urls:
        soup = extract_url(category_url)
        allh3 = soup.find_all("h3")
        for h3 in allh3:
            href = h3.find("a")["href"]
            if "../../.." in href:
                url = href.replace(
                    "../../../", "http://books.toscrape.com/catalogue/")
            else:
                url = "http://books.toscrape.com/"+href

            category_book_urls.append(url)
    return category_book_urls


# Récupération le nombre de page
def number_of_page_category(category_url):
    soup = extract_url(category_url)
    number_element_page = soup.select("strong")[1].text
    convers_page = int(number_element_page)
    division_pages = convers_page/20
    number_of_page = math.ceil(division_pages)
    return number_of_page


# Boucle des pages d'une categories
def get_category_urls(category_url):
    category_urls = []
    # boucle avec le nombre page des urls de la category
    number_pages = number_of_page_category(category_url)
    if number_pages == 1:
        category_urls.append(category_url)
    else:
        for i in range(number_pages):
            new_url = category_url.replace("index.", f"page-{i+1}.")
            category_urls.append(new_url)

    return category_urls

# creations du dossier d'une categories

def scrap_category(category_url):
    books_infos = []
    category_urls = get_category_urls(category_url)
    book_urls = get_category_book_urls(category_urls)
    for url in book_urls:
        # appell fonction qui extrait infos d'un livre
        book = extract_book_data(url)
        books_infos.append(book)
        # nom du dossier
        name_dossier = books_infos[0]["category"]
        # creationn du dossier avec le nom
        path = Path(f"{name_dossier}")
        path.mkdir(parents=True, exist_ok=True)
    return name_dossier, books_infos

#Creation du dossier csv
def folder_category(category_url):
    call_fontion = scrap_category(category_url)
    name = call_fontion[0]
    books = call_fontion[1]
    name_folder = (f"{name}/{name}.csv")
    with open(name_folder, "w+") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book)
    for book in books:
        upc = book["universal_product_code"]
        url = book["image"]
        with open(f"{name}/{upc}.jpg", "wb") as f:
            response = requests.get(f"{url}")
            f.write(response.content)
