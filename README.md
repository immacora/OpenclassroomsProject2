# OpenclassroomsProject2
Utilisez les bases de Python pour l'analyse de marché

Programme (scraper) développé en Python pour extraire des informations sur les livres d'une librairie en ligne, par catégorie, dans un document csv.

Prérequis :
 - Python 3.10.5 / pip
 - PyCharm
 - Requests
 - Beautiful Soup
 - re
 - lxml
 - csv


Pour utiliser le programme :

Assurez-vous d'avoir installé la version 3.10.5 de Python :
- Ouvrir le terminal et saisir python3
- Si la version est plus ancienne, mettre à jour via le Windows store (Conseillé)

Installation rapide et simplifiée :

Téléchargez les fichiers du projet dans l'IDE PyCharm via VCS et vérifiez les éléments suivants lors du clonage : 
  - Environment Virtualenv
  - Base interpreter Python310
  - Fichier requirements
  - Vérifier l'import et lancez le programme main.py 


Installation via le terminal pour Windows :

- Accédez à l’emplacement où placer vos projets : cd Users\Username\RepertoireProjects ou créez le : mkdir RepertoireProjects
- Déplacez-vous dans le répertoire : cd RepertoireProjects
- Clonez le projet : git clone https://github.com/immacora/OpenclassroomsProject2.git
- Déplacez-vous dans le répertoire : cd OpenclassroomsProject2
- Créez l’environnement virtuel du projet : python3 -m venv .venv
- Activez le projet : .venv\Scripts\activate
- Installer les modules : pip install -r requirements.txt
- Exécutez le programme : python main.py


L'exécution du programme dure environ 15 minutes.
Une fois terminé, un fichier csv sera créé pour chaque catégorie de livre dans le dossier data du projet.
Le répertoire data contient le répertoire img des fichiers images téléchargés des livres.
Les images sont nommées par leur Universal Product Code, identifiant unique qui permet de retrouver le livre dans les csv des data mais aussi sur le web.

Pour exécuter une démo (Exemple de 2 catégories : 1 paginée, 1 non paginée), exécuter le programme : python mainDemo.py