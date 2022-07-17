import os
import requests
import function
import csv
import time

# Appel de la fonction qui liste les catégories du site Web Books to scrape
category_list = function.category_list('http://books.toscrape.com/catalogue/category/books_1/index.html')

# Indications utilisateur
print('Début du programme')
print('Nombre de catégories : '+ str(len(category_list)))
print('Le programme dure environ 15mn, merci de patienter...')


# Crée les dossiers data et img
if not os.path.exists('data/img'):
    os.makedirs('data/img')

# Pour chaque catégorie
for i in range(len(category_list)):
    url_category = category_list[i]
    response = requests.get(url_category)
    # Attendre 0.5 secondes
    time.sleep(0.5)
    # Si l'url est valide
    if response.ok:
        # Appel de la fonction qui liste les livres d'une catégorie#
        url_books_category = function.books_category(url_category)
        csv_books_category = []
        # Pour chaque livre d'une catégorie
        for j in range(len(url_books_category)):
            url_book_category = url_books_category[j]
            response = requests.get(url_book_category)
            # Si l'url du livre est valide
            if response.ok:
                # Appel de la fonction qui récupère le dictionnaire de data d'un livre dans une liste de dictionnaires
                dico_data_book = function.book_page_data(url_book_category)
                csv_books_category.append(dico_data_book)
                csv_name = dico_data_book['category']
                # Crée le csv au nom de la catégorie
                keys = csv_books_category[0].keys()
                with open(os.path.join('data/') + csv_name + '.csv', 'w', encoding='ANSI', newline='') as csvfile:
                    dict_writer = csv.DictWriter(csvfile, keys, delimiter=';')
                    dict_writer.writeheader()
                    dict_writer.writerows(csv_books_category)
            else:
                print(response)
    else:
        print(response)
