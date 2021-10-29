import requests
from bs4 import BeautifulSoup
from requests.api import request
from requests.models import Response

url_site = ''


def extract_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html parser')
    return soup


def extract_categories_url():
    """Récupérer la liste des catégories"""
    category_url = [
        'http://books.toscrape.com/catalogue/category/books_1/index.html']
    for list_categories in extract_url(url_site).find('ul', class_="nav").find_all('a', href=True):
        category_url.append(url_site + list_categories['href'])
        return category_url


def extract_books_url(url):
    """
    Récupérer la liste des livres
    """
    list_books = []
    ...
    return list_books


def extract_book_data(url):
    """
Récupérer la liste des infos d'un  livre
"""


# product_page_url
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
data = {}
page = requests.get(url)
# print(url)

soup = BeautifulSoup(page.text, 'html.parser')
# universal_ product_code (upc)
data["upc"] = soup.select("td")[0].text
upc = soup.select("td")[0].text
# print(upc)

# title
data["title"] = soup.select("h1")[0].text
title = soup.select("h1")[0].text
# print(title)

# price_including_tax
data["prix_avec_taxe"] = soup.select("td")[2].text
prix_avec_taxe = soup.select("td")[2].text
# print(prix_avec_taxe)

# price_excluding_tax
data["prix_sans_taxe"] = soup.select("td")[3].text
prix_sans_taxe = soup.select("td")[3].text
# print(prix_sans_taxe)

# number_available
data["stock"] = soup.select("td")[5].text
stock = soup.select("td")[5].text
# print(stock)

# product_description
data["description"] = soup.select("p")[3].text
description = soup.select("p")[3].text
# print(description)

# category
data["category"] = soup.select("a")[3].text
category = soup.select("a")[3].text
# print(category)

# review_rating
data["get_note"] = soup.find_all(
    "p", class_="star-rating")[0].get("class")[1]
get_note = soup.find_all("p", class_="star-rating")[0].get("class")[1]
# print(get_note)

# image_url
# data["image"] = soup.find("div", class_="item active").img["src"]
# image = soup.find("div", class_="item active").img["src"]
# image = "http://books.toscrape.com/" + image.replace('../', '')
# print(image)

"""url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'"""


def extract_books_url(url):
    """
    Récupérer la liste des livres
    """
    list_books = []
    ...
    return list_books


books_list = [
    "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",


]

for book_url in books_list:
    book_data = extract_book_data(book_url)
    # print(book_data)
