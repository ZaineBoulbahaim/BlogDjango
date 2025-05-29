# BlogDjango

## Introducció
Aquest projecte és un blog desenvolupat amb Django. L'objectiu principal és crear una aplicació web on els usuaris puguin llegir articles, gestionar autors i etiquetes, i interactuar amb el contingut. El projecte serveix com a pràctica per aprendre a treballar amb models, rutes, plantilles i proves automatitzades en Django.

## Requisits previs

- Python 3.11 o superior
- Git

## Instal·lació i execució ràpida

```bash
# Clonar el repositori i entrar a la carpeta
git clone https://github.com/ZaineBoulbahaim/BlogDjango.git
cd BlogDjango

# Crear i activar un entorn virtual
# Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell):
python -m venv venv
.\venv\Scripts\activate

# Instal·lar les dependències
pip install -r requirements.txt

# Executar les migracions
python manage.py migrate

# Executar el servidor localment
python manage.py runserver

# Després, obre el navegador i accedeix a:
http://127.0.0.1:8000/

```
## Documentació generada amb pydoc

- [Models (blog.models)](https://htmlpreview.github.io/?https://github.com/ZaineBoulbahaim/BlogDjango/blob/main/docs/models_doc.html)
- [Vistes (blog.views)](https://htmlpreview.github.io/?https://github.com/ZaineBoulbahaim/BlogDjango/blob/main/docs/views_doc.html)


---

Aquest projecte forma part del mòdul de Programació del cicle formatiu de Desenvolupament d'Aplicacions Web (DAW).