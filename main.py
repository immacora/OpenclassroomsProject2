import requests
from bs4 import BeautifulSoup
import function
import csv


##Appel de la fonction qui liste les catégories du site Web Books to scrape##
category_list = function.category_list('http://books.toscrape.com/catalogue/category/books_1/index.html')


#Pour chaque catégorie
for i in range(len(category_list)):
    url_category = category_list[i]
    response = requests.get(url_category)
    #Si l'url est valide
    if response.ok:
        ##Appel de la fonction qui liste les livres d'une catégorie##
        url_books_category = function.books_category(url_category)

        # Initialise la liste des livres de la catégorie
        csv_books_category = []
        # Pour chaque livre d'une catégorie
        for i in range(len(url_books_category)):
            url_book_category = url_books_category[i]
            response = requests.get(url_book_category)
            # Si l'url du livre est valide
            if response.ok:
                ##Appel de la fonction qui récupère le dictionnaire de data d'un livre dans une liste de dictionnaires##
                dico_data_book = function.book_page_data(url_book_category)
                csv_books_category.append(dico_data_book)
                csv_name = dico_data_book['category']
            else:
                print(response)
    #Crée le csv au nom de la catégorie
    csv_name = dico_data_book['category']
    keys = csv_books_category[0].keys()
    with open(csv_name, 'w', encoding='utf-8', newline= '') as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys, delimiter= '\t')
        dict_writer.writeheader()
        dict_writer.writerows(csv_books_category)
