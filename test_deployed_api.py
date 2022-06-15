import requests
import pandas as pd
import numpy as np
import json

# leemos el fichero con los datos de validación
data=pd.read_csv('./input/test.csv')
# los convertimos a un diccionario 
data=data.to_dict('records')
# lo empaquetamos en un diccionario como requiere nuestra api
data_json={'data':data}

# definimos el header para nuestro request
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
}

# realizamos el get
r=requests.get(url='https://ml-titanic-api-flask.herokuapp.com/predictions',headers=headers,data=json.dumps(data_json))

# extraemos los datos de la respuesta
data=r.json()

# vemos la respuesta
print(data)