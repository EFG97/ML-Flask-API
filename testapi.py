import requests
import pandas as pd
import numpy as np
import json

# leemos el set de datos para el entrenamiento de la carpeta input, lo cargamos en un DataFrame de pandas
data=pd.read_csv('./input/test.csv')

# Transformamos el dataFrame a un objeto de tipo diccionario
data=data.to_dict('records')

# Empaquetamos los datos en un diccionario de acuerdo con como diseñamosla funcion de predictions en app.py
data_json={'data':data}

# definimos el header para api request
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
}

# realizamos la request
r=requests.get(url='http://127.0.0.1:5000/predictions',headers=headers,data=json.dumps(data_json))

# extraemos el json con las predicciones del modelo
data=r.json()

# vemos los datos
print(data)