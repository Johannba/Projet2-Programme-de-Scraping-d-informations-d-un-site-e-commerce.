# P2_Book_to_Scrapt_JB
# Programme de Scraping d'informations d'un site e-commerce.

Ce programme est une version beta d'un script permettant d'automatiser un système de surveillance des prix sur un site e-commerce de vente de livre : http://books.toscrape.com/. 

L'objectif est de récupérer les informations suivantes:

* product_page_url_

* universal_ product_code (upc)

* title

* price_including_tax

* price_excluding_tax

* number_available

* product_description

* category

* review_rating

* image_url


L'ensemble des données sont écrites dans un fichier CSV. Chaque CSV contient les informations des livres de la même catégorie et est classé dans un dossier unique. Dans ce même dossier, est créé un sous dossier contenant les images des couvertures de chaque livre.

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme. 

## Pré-requis 

* Python 3 installé ([Télécharger Python](https://www.python.org/downloads/)) 
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel.
Pour cela, ci dessous les étapes à suivre:

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/Johannba/Projet2-scraping```
    
    Vous devez voir (depuis votre explorateur) les fichiers suivants:
        * main.py
        * category.py
        * book.py
        * requirements.txt
    

2. **Creer un environnement virtuel.**

    Depuis windows/mac/linux: ```python3 -m venv env```
    

3. **Activer l'environnement.**
    
    Depuis windows: ```env\Scripts\activate.bat```
    
    Depuis mac/linux: ```source env/bin/activate```
    
    Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
    
    [Documentation Python](https://docs.python.org/fr/3/library/venv.html?highlight=venv)  
    
4. **Installer les paquets.**

    ```pip install -r requirements.txt```

    En executant la commande: ```pip freeze```, vous devez voir apparaitre cette liste: beautifulsoup4==4.10.0 bs4==0.0.1 certifi==2021.10.8 charset-normalizer==2.0.9 idna==3.3 requests==2.26.0 soupsieve==2.3.1 urllib3==1.26.7
    
5. **Lancement du programme**

    ```pyhton main.py```

    Des dossiers 'catégorie de livre' vont être généré à l'intérieur d'un unique dossier 'Projet2-scraping'. Dans chaque dossier 'catégorie' est produit un fichier CSV contenant l'ensemble des données des livres, ainsi que les images des couvertures relative à ces mêmes livres.


## Fabriqué avec
[Visual Studio Code] (https://code.visualstudio.com/download) - Editeur de textes


## Auteurs

**Johann Bacha** 


## Remerciements

Merci à **Ranga Gonnage** pour ses conseils, ça pédagogie et sa diplomatie. 
