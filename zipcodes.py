# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 10:11:09 2021

@author: Mariano
"""

"""

#### Primeros pasos

- instalar BeautifulSoup

Para eso, escribir en anaconda prompt pip install beautifulsoup4

- instalar requests

Para eso, escribir en anaconda prompt pip install requests

- instalar lxml parser

Para eso, escribir en anaconda prompt pip install lxml

Tener en claro que el objetivo es pasar de una tabla en HTML a un DataFrame
que se puede exportar a un csv.

"""

# Llamo requests y BeautifulSoup que los instalé previamente.
import requests
from bs4 import BeautifulSoup

#Importo pandas para ir visualizando lo que estoy haciendo y también me 
#va a servir después para exportar a csv.
import pandas as pd


#Defino un string llamado url y luego uso requests.get que cuando le digo 
#cuál es la URL, va al servidor en donde está alojada la página
#y trata de compiar el HTML.
url = 'https://www.zipcodestogo.com/Maryland/'

#La sintaxis básica es page = requests.get(url). Al ejecutar page, debería
#dar como output <Response [200]>, pero daba <Response [406]>. Si daba
#<Response [404]>, la página no está más. Aparentemente, <Response [406]>
#significa que el servidor no da permiso para copiar el código. Para eso
#está User-Agent. Por defualt el User-Agent de python es 
#python-requests/2.21.0, que es probable que haya sido
#bloqueado por la compañía que hace el hosting. Al cambiar User-Agent,
#page da <Response [200]>
page = requests.get(url, headers = {"User-Agent": "XY"})
#page

#Hasta ahora sólo he copiado la página en una variable que llamé page.
#Lo que quiero ahora es sacar de esa variable el texto del HTML y guardarlo
#en una variable llamada soup. Si corro soup, me da el HTML completo de la
#página.
soup = BeautifulSoup(page.text, "lxml")
#soup

#Hasta acá, definí la página (url), la copié (page) y la pegué (soup).

#Ahora quiero sacar la información de soup. Antes que nada, en el navegador
#inspecciono la página para saber exactamente cuál es y cómo es la tabla.
#En este caso la tabla que quiero tiene como class a inner_table.
#Entonces puedo identificarla con esa class.

#Para eso, soup.find va a encontrar en soup, lo que le pida, que es una table
#con class = "inner_table".
table_data = soup.find("table", {"class" : "inner_table"})

#Con eso, "descartamos" toda la parte del código que no es tabla (en realidad,
#sigue estando en soup, pero sólo nos queremos quedar con la tabla).

#Teniendo en cuenta que el objetivo es armar una base de datos, voy a definir
#el encabezado de esa base con el encabezado de la tabla en la página.

#Como la tabla no tiene header, es decir, no tiene la etiqueta theader,
#sino que la primera fila lo es,  no puedo definir al encabezado buscando las
#etiquetas soup.find_all("th"). Pero en esta página, la primera fila tiene
#inline styling con style = "background-color: #F5F5F5;" entonces puedo sacar
#esa first row igual que antes con soup.find para poder armar el encabezado.
first_row = soup.find("tr", {"style" : "background-color: #F5F5F5;"})

#Hasta acá, definí la página (url), la copié (page), la pegué (soup), le pedí
#que se quede con el pedazo de código de HTML donde está la tabla (table_data)
#y le pedí que se quede con el pedazo de código de la primera fila de la
# tabla (first_row).

#Una vez que tengo el pedazo de código, vuelvo a usar .text, para que se quede
#con el texto de la primera fila y descarte las etiquetas y las otras partes
#del código HTML.
title = first_row.text
#title

#El resultado de title es una string con los encabezados de la base que hay
#que separar. Lo mejor es imprimir title para ver cómo es el string.
zip_code = title[1:9]
city = title[10:14]
county = title[15:21]
zip_code_map = title[22:len(title)-1]

#En una variable aparte defino los encabezados como una lista que contiene los
#strings del nombre de cada encabezado.
headers = [zip_code, city, county, zip_code_map]

#Y ahora puedo armar la base con la lista que creé antes como encabezado.
df = pd.DataFrame(columns = headers)

#Ahora quiero lo datos de la tabla. Entoces, para cada i entre todas las
#filas de la tabla (tag "tr"), quiero que me encuentres todas las
#columnas(tag "td"), que descartes todo lo que es código y me dejes
#el texto de la fila. Luego, añadí esas filas al dataframe.

#Empieza a iterar desde 2 porque la primera fila es el header. Si lo pongo a 
#iterar desde 1, la primera fila que me va a exportar es el header y la voy a
#tener que borrar.
for i in table_data.find_all('tr')[2:]:
        row_data = i.find_all('td')
        row = [tr.text for tr in row_data]
        df.loc[len(df)] = row

#En caso que iteremos con index desde 1, se puede usar df = df.iloc[1: , :]
#para tirar la primera observación que es el header.

#Como la columna Zip Code Map no me interesa, y de hecho lo único que baja es
#View Map o algo así, descarto esa columna.
del df["Zip Code Map"]

#Exporta la tabla como csv. Para exportar con separador ;, sep = ";".
df.to_csv("zipcodes.csv", index = False)