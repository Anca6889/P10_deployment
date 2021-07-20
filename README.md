Langues / Languages README:  
Si le texte est écrit normalement : Français  
*If the text is written in italic : English*
____
# PUR BEURRE, FIND AND REPLACE FOOD WITH HEALTHIER PRODUCTS (French)

PUR BEURRE une application web fictive dans le cadre de ma formation
chez Openclassrooms.
Un restaurant fictif souhaite développer une application pour que ses
utilisateurs puissent trouver des substituts plus sains aux produits qu'ils
consomment. Développement suivant un cahier des charges et une charte graphique
émis par le client fictif.  
Codé en Python/Django en back & bootstrap en front, données des produits via
l'api de openfoodfact  
 
Ce projet est en Français et fonctionne avec l'API de 'https://fr.openfoodfacts.org/'
____
*PUR BEURRE is a fictitious web app as part of my training with Openclassrooms.*
*A fictitious restaurant wants to develop an app who allow the user to find*
*better substitutes thant the products they daily eat.*
*Development is following specifications of the ficitious customer.*  

*Backend of app is code with Python/Django and fronted with bootstrap.*
*The products datas are comming from the API of* 'https://fr.openfoodfacts.org/'
*App in French*  
____
## Functions:

- Chercher des produits et subtstituts alimentaire de meilleur nutriscore
- Creer un compte utilisateur, login, logout.
- Enregistrer des produits favoris
- Consulter les fiches produits sur OFF
____
- *Search products and substitutes with better nutriscore (french notation)*
- *Create an user account, login, logout* 
- *Save favorites products*
- *Check complete datas of product on OFF*

## Enjoy the app online on Heroku ;-) (WARNING: LIMITED DATABASE ≃ 900 products)

https://anca-purbeurre-8.herokuapp.com/

____
## On local Machine:

- Assurez vous d'avoir python 3 et pip installé sur votre machine
- Vous devez disposer d'une base de donnée POSTGRE SQL
- Clonez ce dépôt sur votre Machine locale
- Installez et initialisez pipenv
- Configurer votre base de données dans P8_pur_beurre\settings.py => DATABASE
- Definissez une SECRET_KEY dans vos variables d'environements
- Lancer le shell de pipenv
- Effectuer les migrations
- Lancer le téléchargement et peuplement de la base de données (Vous pouvez influer sur la quantitée de produit dans app\config\config.py sur la constante PAGE_SIZE)
- Lancer le serveur local
___
- *Make sure you have python 3 and pip installed on your machine*
- *You need a POSTGRE SQL database on your local machine*
- *Fork this repository on your local machine*
- *Install and init pipenv*
- *Setup your database in P8_pur_beurre\settings.py => DATABASE*
- *setup a SECRET_KEY in your environment variables*
- *Init the pipenv shell*
- *Do the migrations*
- *Launch the download and filling the DB (You can setup the quantity of products with setting const. PAGE_SIZE in app\config\config.py*
- *Run the local server*
____
## Commands :

Installer pipenv / *install pipenv* :
``` py -m pip install pipenv ```

Installer toutes les dépendances du projet / *Install all requirements of the project* :
``` py -m pipenv install ```

Lancer le shell pipenv / *init the pipenv shell* :
``` py -m pipenv shell ```

Configurer les migrations / *Setup the migrations* :
``` py manage.py makemigrations ```

Executer les migrations / *Execute the migrations* :
``` py manage.py migrate ```

Appel à l'API et peupler la BDD / *API call and fill the DB* :
``` py manage.py database ```

Lancer le serveur local / *Launch local server* :
``` py manage.py runserver ```
___
#### Packages used :

[packages]
django = "*"
psycopg2 = "*"
requests = "*"
flake8 = "*"
django-heroku = "*"
gunicorn = "*"
progress = "*"

[dev-packages]
selenium = "*"
coverage = "*"

[requires]
python_version = "3.9"



