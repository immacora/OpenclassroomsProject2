import os
import requests
import function
import csv

# Choix de 2 catégories (paginée et non paginée) pour la démo
category_list = ['http://books.toscrape.com/catalogue/category/books/health_47/index.html', 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html']

# Indications utilisateur
print('Début de la démo du programme')
print('Nombre de catégories pour la démo : ' + str(len(category_list)))
print('Le programme dure 1 à 2mn, merci de patienter...')

# Crée les dossiers data et img
if not os.path.exists('data/img'):
    os.makedirs('data/img')

# Pour chaque catégorie
for i in range(len(category_list)):
    url_category = category_list[i]
    response = requests.get(url_category)
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
                with open(os.path.join('data/') + csv_name + '.csv', 'w', encoding='utf-8', newline='') as csvfile:
                    dict_writer = csv.DictWriter(csvfile, keys, delimiter='\t')
                    dict_writer.writeheader()
                    dict_writer.writerows(csv_books_category)
            else:
                print(response)
    else:
        print(response)
