#!/usr/bin/env python
# coding: utf-8

# # AVANCE PRACTICA 1 EN EQUIPO
# 
# ### Objetivo 
# 
# En esta actividad nos encargaremos de limpiar los datos de nuestra Base de Datos, que como ya lo hemos comentado anteriormente es de una BD que tiene informacion de Suicidios y contamos con algunas columnas las cuales las mas importantes para nosotros son la generacion y el lugar donde han ocurrido estos mismos, ya que nuestro objetivo principal es agruparlos y ver la clasificacion que se tiene en cuestion de generaciones para que de esta manera nos ayude a nosotros a poder saber cual de estas Generaciones ha sido más propensa a esta triste situacion y poder tomar accion, creando conciencia a futuras generaciones y hacer todo lo que este en nuestras manos para tomarlo como "foco rojo" a esta misma.
# 
# Integrantes:
# 
#     Mata Martínez Missael 1672902
# 
#     Celestino Tovar Angel Gabriel 1668653
# 
#     López Sánchez Maribel 1672709
# 
# 
# 
# 
# ## Limpieza de datos
# 
# El primer paso sera importar librerias y utilizamos la libreria pandas para poder cargar archivos csv.

# In[1]:


import matplotlib as plt
import seaborn as sn
import numpy as np 
import pandas as pd 
import json
df = pd.read_csv("master.csv")


# Verificamos las dimensiones de la tabla

# In[2]:


df.shape


# Ahora visualizaremos la tabla con solamente 12 de sus filas de las 27820 que tiene

# In[4]:


df.head(12)


# A continuacion mostraremos los nombres y tipos de datos que tiene nuestra BD

# In[5]:


df.dtypes


# De estas columnas solamente necesitaremos country, sex, suicides_no y generation. Ahora cambiaremos este nombre de las columnas al español

# In[13]:


df = df.rename(columns = {'country':'Pais', 'sex':'Sexo', 'suicides_no':'NumeroDeSuicidios', 'generation':'Generacion'})
df.columns


# Ahora, eliminaremos las filas que contengan datos nulos para quitar lo que no necesitamos. Nosotros lo hemos echo asi porque sabemos que las columnas de interes (PAIS, SEXO, NUMERO DE SUICIDIOS Y GENERACION) no se encuentran con ninguna celda vacia.

# In[15]:


df = df.dropna()


# Ahora mostramos lo que hicimos

# In[16]:


df


# Ahora eliminaremos todas las columnas que tengan datos nulos. Igual que en lo anterior, ya confirmamos que en nuestras columnas de interes no habia datos nulos.

# In[17]:


df


# A continuacion eliminaremos las columnas que no necesitamos. Para solo quedarnos con Pais, Sexo, NumeroDeSuicidios y Generacion

# In[18]:


df.columns


# In[20]:


df = df.drop(['year', 'edad', 'population', 'suicides/100k pop', 'country-year', 'HDI for year',
       ' gdp_for_year ($) ', 'gdp_per_capita ($)'], axis=1)


# Ahora pasamos a mostrar la tabla sin esas columnas.

# In[21]:


df


# Ahora quisiéramos ver que generaciones son las que más números de suicidios tienen

# In[22]:


df.groupby('Generacion').sum()


# ### Preguntas de interes ###
# 
# 

# #### Cuantos grupos de hombres y mujeres mayores de 30 años se han suicidado?  ####

# #### Tomando un registro de la BD, se puede saber como afecto el suicidio de la persona? ####

# 
# ## Conclusion ##
# 
# Si bien, lo anterior aplicado fue la manera en la cual se debe a empezar a desarrollar mas el uso cognitivo sobre la investigacion de nuestra BD, tomando en cuenta la eliminacion de columnas que no utilicemos ya se por funciones desconocidas o simplemente datos que no son relevantes. 
# 
# Las preguntas fueran replanteadas mas a fondo para dar a entender con mayor facilidad el tema que se esta tratando con la informacion. Al final, fue la manera mas correcta de formularlas.

# In[ ]:




