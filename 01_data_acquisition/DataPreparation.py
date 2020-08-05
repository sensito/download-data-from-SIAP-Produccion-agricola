#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import os

from tqdm import tqdm

import urllib


# ## Get data
# 
# ---

# In[2]:


def downloaddata_1(dest_Folder, name_Statistics, dictionary_Name):
    
    url_Estadistica_Produccion_Agricola = "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_"
    url_Diccionario_Produccion_Agricola = "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Diccionario%20agr%C3%ADcola%201980%20a%202002.xlsx"
    
    extension_Estadistica = ".csv"
    extension_Diccionario = ".xlsx"
    
    nombre_Estadistica_Produccion_Agricola = dest_Folder + name_Statistics
    nombre_Diccionario_Produccion_Agricola = dest_Folder + dictionary_Name

    maximo = 2002
    minimo = 1980
    
    for key in tqdm(range(minimo, maximo + 1)):
        
        url_Produccion = url_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica
        df = pd.read_csv(url_Produccion, encoding='latin-1')
        df.to_csv(nombre_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica)
        
        if key == maximo:
            urllib.request.urlretrieve(url_Diccionario_Produccion_Agricola, nombre_Diccionario_Produccion_Agricola + extension_Diccionario)


# In[3]:


def downloaddata_2(dest_Folder, name_Statistics, dictionary_Name):    
    url_Estadistica_Produccion_Agricola = "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Cierre_agricola_mun_"
    url_Diccionario_Produccion_Agricola = "http://infosiap.siap.gob.mx/gobmx/datosAbiertos/ProduccionAgricola/Diccionario%20agr%C3%ADcola%202003%20a%202017.xlsx"
    
    extension_Estadistica = ".csv"
    extension_Diccionario = ".xlsx"
    
    nombre_Estadistica_Produccion_Agricola = dest_Folder + name_Statistics
    nombre_Diccionario_Produccion_Agricola = dest_Folder + dictionary_Name

    maximo = 2019
    minimo = 2003
    
    for key in tqdm(range(minimo, maximo + 1)):
        
        url_Produccion = url_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica
        df = pd.read_csv(url_Produccion, encoding='latin-1')
        df.to_csv(nombre_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica)
        
        if key == maximo:
            urllib.request.urlretrieve(url_Diccionario_Produccion_Agricola, nombre_Diccionario_Produccion_Agricola + extension_Diccionario)

