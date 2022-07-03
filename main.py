import requests
from bs4 import BeautifulSoup
import function
import csv


# Initialise la matrice des data
csv_list = [['product_page_url'],
            ['universal_product_code'],
            ['titre'],
            ['price_including_tax'],
            ['price_excluding_tax'],
            ['number_available'],
            ['product_description'],
            ['category'],
            ['review_rating'],
            ['image_url'],]

##Appel de la fonction qui liste les catégories du site Web Books to scrape##
category_list = function.category_list('http://books.toscrape.com/catalogue/category/books_1/index.html')


#Récupère l' url d'une catégorie
for i in range(len(category_list)):
    url_category = category_list[i]
    response = requests.get(url_category)
    #Si l'url est valide
    if response.ok:
        ##Appel de la fonction qui liste les livres d'une catégorie##
        url_books_category = function.books_category(url_category)

        # Pour chaque livre d'une catégorie
        for i in range(len(url_books_category)):
            url_book_category = url_books_category[i]
            response = requests.get(url_book_category)
            # Si l'url du livre est valide
            if response.ok:
                ##Appel de la fonction qui récupère la liste des data d'un livre##
                list_data_page = function.book_page_data(url_book_category)

                # Pour chaque data dans la liste
                for i in range(len(list_data_page)):
                    list_data_ligne = list_data_page[i]
                    #Ajoute la ligne de data au tableau de listes
                    csv_list[i].append(list_data_ligne)


with open('donnees.csv', 'w', encoding='utf-8') as file:
    for row in csv_list:
        writer = csv.writer(file, delimiter='\t')
        for data in row:
            writer.writerow(data)

