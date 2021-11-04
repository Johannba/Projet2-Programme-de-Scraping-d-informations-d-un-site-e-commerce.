import csv
import requests
from bs4 import BeautifulSoup
from requests.models import Response


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


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
    # return category_url
    print(category_url)


def extract_book_data(url):
    """
    Récupérer la liste des infos d'un  livre
    """
    # product_page_url
    data = {}
    product_page_url = requests.get(url)

    soup = BeautifulSoup(product_page_url.text, 'html.parser')
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


# open the file in the write mode

def register_books_data(books_list):

    with open('test.csv', 'w') as f:
        # créé le redacteur csv

        # def register_books_data(books_list):

        #     with open('test.csv', 'w') as f:
        #         # créé le redacteur csv
        #         for book_url in books_list:
        #             book_data = extract_book_data(book_url)
        #             w = csv.DictWriter(f, book_data.keys())
        #             w.writeheader()
        #             w.writerow(book_data)
        #             f.write(book_data['product_page_url'] + ";" +
        #                     book_data['universal_ product_code'] + ";" +
        #                     book_data['title'] + ";" +
        #                     book_data['price_including_tax'] + ";" +
        #                     book_data['price_excluding_tax'] + ";" +
        #                     book_data['number_available'] + ";" +
        #                     book_data['product_description'] + ";" +
        #                     book_data['category'] + ";" +
        #                     book_data['universal_ product_code'] + ";" +
        #                     book_data['review_rating'] + "/n")

        f.close
        # ecrire dans le fichier csv
        # w.writerow(book_data)


if __name__ == "__main__":
    list_categories_url = extract_categories_url()
    print(list_categories_url)

    books_list = [
        "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    ]
    books_data = register_books_data(books_list)
