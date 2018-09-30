# -*- coding: utf-8 -*-
__author__ = 'JustFastFail'

from bs4 import BeautifulSoup
import requests

URL = "https://www.decathlon.es/C-1015238-calzado"

# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('li', {'class': 'new-product-thumbnail desktop initial'})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        marca = entrada.find('h3', {'class': 'product-brand'}).getText()
        titulo = entrada.find('h3', {'class': 'product-label'}).getText()

        print('marca:', marca)
        print('titulo:',titulo)

else:
    print("Status Code %d" % status_code)

