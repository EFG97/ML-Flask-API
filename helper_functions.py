import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(data_all):

    #completamos con la mediana
    data_all['Age'].fillna(data_all['Age'].median(), inplace = True)

    # Completamos con la moda
    data_all['Embarked'].fillna(data_all['Embarked'].mode()[0], inplace = True)

    # Completamos con la mediana
    data_all['Fare'].fillna(data_all['Fare'].median(), inplace = True)

    # eliminamos columnas irrelevantes
    drop_column = ['PassengerId','Cabin', 'Ticket']
    data_all.drop(drop_column, axis=1, inplace = True)

    # Nuevas variables
    data_all['FamilySize'] = data_all['SibSp'] + data_all['Parch'] + 1 # tamaño familia

    data_all['IsAlone'] = 1
    data_all['IsAlone'].loc[data_all['FamilySize'] > 1] = 0 # el pasajero iba solo o no

    # Columna nueva con el "título"
    data_all['Title'] = data_all['Name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]

    # Agrupamos tarifa del billete por cuartiles 
    data_all['FareBin'] = pd.qcut(data_all['Fare'], 4)

    # Agrupamos en 5 tramos de edad iguales
    data_all['AgeBin'] = pd.cut(data_all['Age'].astype(int), 5)

    # Usamos label encoder sobre las variables
    label = LabelEncoder()
    data_all['Sex_Code'] = label.fit_transform(data_all['Sex'])
    data_all['Embarked_Code'] = label.fit_transform(data_all['Embarked'])
    data_all['Title_Code'] = label.fit_transform(data_all['Title'])
    data_all['AgeBin_Code'] = label.fit_transform(data_all['AgeBin'])
    data_all['FareBin_Code'] = label.fit_transform(data_all['FareBin'])

    return data_all