# Back Office Bateau Thibault
C'est une API développé en Django, par Kemo DIAITE, Yuepeng YANG et Mathieu ALBIN.

## Installation
Pour pouvoir lancer l'application il vous faut tout d'abord activer l'environnement virtuel, elle contient déjà les packages nécessaire au lancement de l'api.

```bash
source env/bin/activate
```
Ou vous pouvez créer votre propre environnement et installer les package suivants.

``bash
python3 -m venv env
source env/bin/activate
pip install django djangorestframework django-cors-headers zappa
```
Vous pouvez ensuite lancer l'api localement mais elle ne sera pas accessible en local. 
```bash
cd mySearchEngine
python manage.py runserver
```
L'api a été déployé via Zappa sur AWS Lambda vous pouvez la voir [ici](https://16fcwr67g9.execute-api.eu-west-3.amazonaws.com/backend_BT_YMK)