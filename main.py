import requests
from bs4 import BeautifulSoup


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
