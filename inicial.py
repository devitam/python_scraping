# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:04:13 2021

@author: Mariano Devita

IMPORTANTE: en anaconda promt

pip install wwo-hist

"""

from wwo_hist import retrieve_hist_data

import os
os.chdir("D:/Documentos/Maestría/UdeSA/4. Segunda parte/2. Herramientas computacionales/3. Python scrapping/Tarea/weather")

frequency = 24
start_date = "01-JAN-2015"
end_date = "31-DEC-2015"
api_key = "698f2cf3815c4dbaa2c131633210707"
location_list = ["20625", "20650", "20688", "20740", "20871", "21040",
                 "21043", "21158", "21201", "21220", "21412", "21504",
                 "21606", "21638", "21639", "21643", "21651", "21704",
                 "21742", "21802", "21811", "21853", "21914"]

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)