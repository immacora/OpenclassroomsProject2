import os
import requests
from bs4 import BeautifulSoup
import function
import csv
import time


##Appel de la fonction qui liste les catégories du site Web Books to scrape##
category_list = function.category_list('http://books.toscrape.com/catalogue/category/books_1/index.html')

#Crée les dossiers data et img
if not os.path.exists('data/img'):
    os.makedirs('data/img')

#Pour chaque catégorie
for i in range(len(category_list)):
    url_category = category_list[i]
    response = requests.get(url_category)
    # Attendre 0.5 secondes
    time.sleep(0.5)
    #Si l'url est valide
    if response.ok:

        #Appel de la fonction qui liste les livres d'une catégorie#
        url_books_category = function.books_category(url_category)
        csv_books_category = []
        # Pour chaque livre d'une catégorie
        for i in range(len(url_books_category)):
            url_book_category = url_books_category[i]
            response = requests.get(url_book_category)
            # Si l'url du livre est valide
            if response.ok:

                #Appel de la fonction qui récupère le dictionnaire de data d'un livre dans une liste de dictionnaires##
                dico_data_book = function.book_page_data(url_book_category)
                csv_books_category.append(dico_data_book)
                csv_name = dico_data_book['category']

                # Crée le csv au nom de la catégorie
                keys = csv_books_category[0].keys()
                with open(os.path.join('data/') + csv_name + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
                    dict_writer = csv.DictWriter(csvfile, keys, delimiter='\t')
                    dict_writer.writeheader()
                    dict_writer.writerows(csv_books_category)

                # Prépare le dossier data
                upc_book_category = dico_data_book['universal_product_code']
                img_url_category = dico_data_book['image_url']
                response = requests.get(img_url_category)

                # Si le lien de l'image du livre est valide
                if response.ok:
                    img_data = requests.get(img_url_category).content
                    with open(os.path.join('data/img/') + upc_book_category + '.jpg', 'wb') as handler:
                        handler.write(img_data)
                else:
                    print(response)
            else:
                print(response)

    else:
        print(response)
