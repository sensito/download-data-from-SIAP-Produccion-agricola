#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np

import os

from tqdm import tqdm

import urllib


# ## Get data
# 
# ---

# In[9]:


def downloaddata(dest_Folder, url_Estadistica_Produccion_Agricola, url_Diccionario_Produccion_Agricola, option):    
    name_Statistics = "/Estadistica_de_la_Produccion_Agricola_de_"
    dictionary_Name = "/Diccionario_de_datos_para_Estadistica_de_Produccion_Agricola"
    
    extension_Estadistica = ".csv"
    extension_Diccionario = ".xlsx"
    
    nombre_Estadistica_Produccion_Agricola = dest_Folder + name_Statistics
    nombre_Diccionario_Produccion_Agricola = dest_Folder + dictionary_Name

    maximo, minimo = rango_datos(option)
    
    for key in tqdm(range(minimo, maximo + 1)):
        
        url_Produccion = url_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica
        df = pd.read_csv(url_Produccion, encoding='latin-1')
        df.to_csv(nombre_Estadistica_Produccion_Agricola + str(key) + extension_Estadistica)
        
        if key == minimo:
            urllib.request.urlretrieve(url_Diccionario_Produccion_Agricola, nombre_Diccionario_Produccion_Agricola + extension_Diccionario)


# In[10]:


def rango_datos(option):
    if option == 1:
        return 2002, 1980
    if option == 2:
        return 2019,2003

