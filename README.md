# python_scraping

#### Pasos
1) Buscar zipcodes https://www.zipcodestogo.com/Maryland/ (copiar y pegar en Excel, después en Stata - líneas 3 a 11 del do file de Stata) HECHO con código de python en vez de copiar y pegar de la página.

2) Bajar datos de crimen de https://odn.data.socrata.com/dataset/National-Police-Department-Crime-Rates-by-Month-Ye/tt5s-y5fc (hecho en clase llamado crime.csv). Quedarse con los datos de 2015 y el estado MD, guardar como MD_crime.dta (líneas 14 a 22 del do file de Stata) HECHO creé mi pripia cuenta aquí.

3) Merge base zipcodes y crimen (necesito ubicar los zipcodes para bajar el weather después) HECHO. Los hice separados en carpetas de zipcodes y crime, para hacer el merge en otra carpeta.

4) Bajar shapefile https://hub.arcgis.com/datasets/maryland::maryland-physical-boundaries-county-boundaries-detailed/explore?location=38.802591%2C-77.268250%2C8.35 y abrir con Excel el archivo .dbf para obtener el ID de cada county. Agregar el ID (sacado del shapefile) para después poder hacer el merge (líneas 31 a 55 Stata) HECHO, chequeé que estuviera bien en el do.

5) linea 59 de Stata suma los crimenes por county, linea 61 me genera un zipcode por county (el zipcode mediano), línea 63 me quedo con una observación por county, por año, por mes, por tipo de crimen -> MD_crime_2015.dta HECHO

6) en la línea 68 le pido a Stata los zipcodes para poner en python para que me baje los datos de weather (usar el Inicial.py) agregando los zips, corrigiendo año y frecuency *24*. HECHO, me dio más zipcodes que en el video.

7) línea 71 a 92 genera nueva base para que cada columna sea un crimen. HECHO

8) línea 95 a 110 junta las bases de weather quedándose con el promedio de precipitaciones por mes (línea 104) y una observación por mes/county (linea 105). HECHO

9) Merge crimen,zipcodes+weather (línea 117) HECHO

10) Aunque en el video ven lineas después de la 120, necesitan eso para GeoDa, no para GIS. En GeoDa necesitan que cada variable temporal esté en una columna, en GIS ya reconoce que es un panel. Por ejemplo, para GeoDa necesitas una columna que sea theft0115 theft0215, en GIS podés decirle cuál es la variable de date y que use eso. OK

#### Consignas

Gráficos a hacer:
1) Gráfico entre precipitaciones y algún crímen per cápita. Explicar.

Para esto, abrí QGIS y subí la base de Maryland Boundaries y la creada de MD_crime_2015_wide.dta, hice los gráficos y los puse en LaTex.

2) Usar la variable BLACK para generar algo (gráfico o mapa) interesante (potencialmente interesante, puede que con estos datos no de nada).



3) Mapa que avance en el tiempo por mes de precipitaciones y de uno de los crímenes per cápita (Properties > Temporal después de haber hecho un coropletico o heatmap. Ver: https://www.qgistutorials.com/en/docs/3/animating_time_series.html. Generar variable de date con función make_date y las variables, year, month y day. Ojo que ya existe la variable date y salta error si le ponen el mismo nombre). En heatmap, poner como transparente cuando es 0 la variable. 

Se entregan 3 archivos en GitHub (Poner link en la entrega de la tarea):

LaTeX con consignas 1 y 2

GIF con consigna 3

Archivo archivo .py (Inicial.py) para bajar lo de weather para los zipcodes correspondientes.
