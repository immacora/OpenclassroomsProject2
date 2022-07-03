import requests
from bs4 import BeautifulSoup
import re


##Retourne la liste des catégories du site Web Books to scrape##
def category_list(url):
    response = requests.get(url)
    category_url = []
    # Si l'url est valide
    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')
        # Récupérer les href de tous les liens contenant le mot 'books'
        for a in soup.findAll('a'):
            if 'books' in a['href']:
                link = a.get('href')
                link = link.replace('..', 'http://books.toscrape.com/catalogue/category')
                category_url.append(link)
        return category_url
    else:
        return response


##Récupérer les href de tous les livres d'une catégorie##A FINIR
def books_category(url):
    response = requests.get(url)
    url_books_category = []

    # Si l'url est valide
    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')
        next_btn = soup.find('li', class_='next')

        # Si le bouton next n'existe pas
        if next_btn is None:
            links = soup.find('ol').findAll('a')
            print(links)
            # Récupérer tous les liens 'a' de la liste 'ol'
            for a in links:
                link = a.get('href')
                link = link.replace('../../..', 'http://books.toscrape.com/catalogue')
                # trier les doublons
                if link not in url_books_category:
                    url_books_category.append(link)
            return url_books_category

        # Si le bouton next existe
        else:
            url_pages_categorie = []
            nb_pages = soup.find('li', class_='current').text
            nb_pages = int(re.search('of (.+?)', nb_pages).group(1))

            print(nb_pages)
            print(url)
            # Créer la liste des url des pages de la catégorie
            for i in range(nb_pages):
                url_page_categorie = url.replace('index', "page-" + str(i + 1))
                response = requests.get(url_page_categorie)
                # Si l'url est valide
                if response.ok:
                    soup = BeautifulSoup(response.content, 'lxml')
                    links = soup.find('ol').findAll('a')
                    # Récupérer tous les liens 'a' de la liste 'ol'
                    for a in links:
                        link = a.get('href')
                        link = link.replace('../../..', 'http://books.toscrape.com/catalogue')
                        #trier les doublons
                        if link not in url_books_category:
                            url_books_category.append(link)

            return url_books_category

    else:
        return response

##Retourne les données formatées de la page dans une liste de listes##
def book_page_data(url):
    response = requests.get(url)

    # Si l'url est valide
    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')

        product_page_url = url
        titre = soup.find('h1').text
        product_description = soup.select_one('article > p').text.replace(' ...more', '')
        category = soup.select_one('li:nth-of-type(3)').find('a').text
        review_rating = soup.find('p', class_='star-rating').get('class').pop()
        image_url = soup.find('img').get('src').replace('../..', 'http://books.toscrape.com')

        table = soup.find_all('td')
        universal_product_code = table[0].text
        price_including_tax = table[2].text
        price_excluding_tax = table[3].text
        number_available = table[5].text.removeprefix('In stock (').removesuffix(' available)')

        list_page_data = [
            [product_page_url],
            [universal_product_code],
            [titre],
            [price_including_tax],
            [price_excluding_tax],
            [number_available],
            [product_description],
            [category],
            [review_rating],
            [image_url],
        ]

        return list_page_data

    else:
        return response
