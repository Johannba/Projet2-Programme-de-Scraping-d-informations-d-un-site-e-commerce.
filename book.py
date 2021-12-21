import requests
from bs4 import BeautifulSoup

# requet pour parser url

def extract_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def extract_book_data(url):
    """
    Récupérer la liste des infos d'un  livre
    """""
    # product_page_url
    data = {}
    soup = extract_url(url)
    # universal_ product_code (upc)
    data["product_page_url"] = url
    data["universal_product_code"] = soup.select("td")[0].text
    # title
    data["title"] = soup.select("h1")[0].text
    # price_including_tax
    data["price_including_tax"] = soup.select("td")[2].text
    # price_excluding_tax
    data["price_excluding_tax"] = soup.select("td")[3].text
    # number_available
    data["number_available"] = soup.select("td")[5].text
    # product_description
    data["product_description"] = soup.select("p")[3].text
    # category
    data["category"] = soup.select("a")[3].text
    # review_rating
    data["review_rating"] = soup.find_all(
        "p", class_="star-rating")[0].get("class")[1]
    # image_url
    image = soup.find("div", class_="item active").img["src"]
    data["image"] = image.replace('../../', "http://books.toscrape.com/")

    return data
