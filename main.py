import requests
from bs4 import BeautifulSoup
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
