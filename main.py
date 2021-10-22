import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
page = requests.get(url)
# print(url)

soup = BeautifulSoup(page.text, 'html.parser')
produit = soup.find_all(name="table", attrs={"class": "table table-striped"})
# print(produit)
article = soup.find("article", "product_page")
# print(article)
product_description = article.h1.text
# print(product_description)

upc = article.td.text
# print(upc)

price_including_tax = soup.find("article", "product_page").find(
    "tr", {"td": "Price (excl. tax)"})  # .findPrevious().text
# print(price_including_tax)

# price_excluding_tax
category = soup.find("ul", "breadcrumb").find(
    "li", {"class": "active"})  # .findPrevious().text
# print(category)

links = []
tds = soup.findAll('td')
for td in tds:
    th = td.find('th')
# print(tds)

all_arcticles = soup.find("div", id_="content_inner")
all_arcticles
=======
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
page = requests.get(url)

# connection site
# url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
# reponse = requests.get(url)
# page = (reponse.content)
# affiche la page HTML
# print(page)
# transforme (parse) le HTML en objet BeautifulSoup
# codebon soup = BeautifulSoup(page.text, 'html.parser')
# codebon produit = soup.find_all(name="div", attrs={"id": "content_inner"})
prixx = []  # stocker les prix
produits = []
images = []

page_web = BeautifulSoup(page.content, 'lxml')
all_products = page_web.find_all('div', class_='row')
# récupérer le product page
# product_page = "product_page"
# product = soup.find(nameuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upcuniversal_ product_code (upc="id", attrs={"class": "product_description"})
# print(product)
# title = soup.find('title')
>>>>>>> 6a85969d134855ad81346f9a9a0e517f957da368
