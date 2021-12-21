from category import folder_category
from book import extract_url

URL = "http://books.toscrape.com"

# Recupérés tous les liens de toutes les  categories


def full_category(url):
    all_category = []
    soup = extract_url(url)
    all_ul = soup.find('div', class_="side_categories").find(
        'ul').find_all('li')[1:]
    for category_url in all_ul:
        href = category_url.find("a")["href"]
        url = URL+("/")+href
        all_category.append(url)
    return all_category

# Boucles tous les liens des categorie et creer le fichier complet de tous les livres

def main(url):
    all_products = []
    list_url = full_category(url)
    for url in list_url:
        folder_category(url)


main(URL)
