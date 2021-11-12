
import csv
import requests
from bs4 import BeautifulSoup


url = 'http://books.toscrape.com'


def extract_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def extract_categories_url():
    """Récupérer la liste des catégories"""
    category_url = [
        'http://books.toscrape.com/catalogue/category/books_1/index.html']
    for list_categories in extract_url(url).find('ul', class_="nav").find_all('a', href=True):
        category_url.append(url + list_categories['href'])
    return category_url


def extract_book_data(url):
    """
    Récupérer la liste des infos d'un  livre
    """""
    # product_page_url
    data = {}
    product_page_url = requests.get(url)
    soup = BeautifulSoup(product_page_url.content, 'html.parser')
    # universal_ product_code (upc)
    data["universal_product_code"] = soup.select("td")[0].text
    universal_product_code = soup.select("td")[0].text

    # title
    data["title"] = soup.select("h1")[0].text
    title = soup.select("h1")[0].text

    # price_including_tax
    data["price_including_tax"] = soup.select("td")[2].text
    price_including_tax = soup.select("td")[2].text

    # price_excluding_tax
    data["price_excluding_tax"] = soup.select("td")[3].text
    price_excluding_tax = soup.select("td")[3].text

    # number_available
    data["number_available"] = soup.select("td")[5].text
    number_available = soup.select("td")[5].text

    # product_description
    data["product_description"] = soup.select("p")[3].text
    product_description = soup.select("p")[3].text

    # category
    data["category"] = soup.select("a")[3].text
    category = soup.select("a")[3].text

    # review_rating
    data["review_rating"] = soup.find_all(
        "p", class_="star-rating")[0].get("class")[1]
    review_rating = soup.find_all("p", class_="star-rating")[0].get("class")[1]

    # image_url
    # data["image"] = soup.find("div", class_="item active").img["src"]
    # image = soup.find("div", class_="item active").img["src"]
    # image = "http://books.toscrape.com/" + image.replace('../', '')

    return data


def register_books_data(books_list):

    # with open('test.csv', 'w') as f:
    #     f.write("product_page_url, universal_ product_code, title, price_including_tax,number_available, product_description, category, review_rating\n")
    #     for link in books_list:
    #         print(link)

    # with open('test.csv', 'r') as f:
    #     for book in f:
    #         print(book)

    with open('test.csv', 'w') as f:
        book_url = []
        book_data = extract_book_data(book_url)
        w = csv.DictWriter(f, book_data.keys())
        w.writeheader(("product_page_url", "universal_ product_code", "title", "price_including_tax", "number_available", "product_description",
                       "category", "review_rating"))
        for book_url in books_list:
            w.writerow(books_list)

        if __name__ == "__main__":
            list_categories_url = extract_categories_url()
            print(list_categories_url)


books_list = [
    "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
]
books_data = register_books_data(books_list)
