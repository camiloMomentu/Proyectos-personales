# Insatalacion de librerias
#!pip install sweetviz"
#!pip install sklearn


# Librerías
import pandas as pd
import matplotlib.pyplot as plt
#import sweetviz as sv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import OneHotEncoder
import getpass
import pickle

url_principal = ("C:/Users/" +
                 getpass.getuser() +
                 "/BANCO DE BOGOTA/Sanchez Sastoque, Walter Ivan - 04. Proyectos Analytics/01. Analisis predictivo de fugas de talento/1. Modelo nuevo/Modelo de fugas de Talento/")
enlace = url_principal + "Base/Training_Nuevo.csv"

datos = pd.read_csv(enlace,sep = ",", decimal=".")

# Limpieza de datos
datos_2 = datos.drop(['Cedula','Posicion','Nombres','Area Person','VP',
                      ' GPTW2020 ','Promedio EVD',"Empresa","Fecha ingreso","Fecha Nacimiento",'Área'],axis = 1)

datos_2.columns = ['genero','estado','tipo_contrato','antiguedad',
                   'edad','cargo','apellido_cargo','grupo','dific_reclutamiento',
                   'salario','brecha_salario','ausentismo','disciplinarios',
                   'pasivo_vacaciones','formacion','evd','ascensos','aumentos']


datos_2['dific_reclutamiento'] = datos_2['dific_reclutamiento'].replace({np.nan:2})
datos_2['dific_reclutamiento'] =datos_2[['dific_reclutamiento']].astype(int)
datos_2['estado'] = datos_2['estado'].replace({'Activo':0,'Retirado':1})

datos_2['salario'] = datos_2['salario'].astype(int)
datos_2['brecha_salario'] = datos_2['brecha_salario'].astype(float)
datos_2['formacion'] = datos_2['formacion'].astype(float)

# Sweetviz
# descriptivos = sv.compare_intra(datos_2, datos_2['estado']==0,['Activo','Retirado'])
# descriptivos.show_html()

# Organización de datos,
categoricos = ['genero','tipo_contrato','cargo','evd','ascensos','apellido_cargo','grupo']
dumm = datos_2.drop(categoricos, axis = 1)

'''
---------------------  get_dummies ------ error con el pipeline, mejor usar OneHotEncoder -----------------
dumm2 = pd.get_dummies(datos_2[categoricos], sparse=False)
#datos_modelo = pd.concat([dumm, dumm2], axis=1)
print(dumm2)
'''
encoder_dummies = OneHotEncoder(handle_unknown='ignore', sparse=False)
encoder_dummies.fit(datos_2[categoricos])
dumm2 = pd.DataFrame(encoder_dummies.transform(datos_2[categoricos]))
cat_cols = []
[[cat_cols.append(categoricos[i] + "_" + j) for j in encoder_dummies.categories_[i]] for i in range(len(categoricos))]
dumm2.columns = cat_cols

print("Tamaño Dataset Final:", dumm2.shape)

datos_modelo = pd.concat([dumm, dumm2], axis=1)

for col in ['salario','brecha_salario','formacion']:
    datos_modelo[col] = (datos_modelo[col]-datos_modelo[col].mean())/np.std(datos_modelo[col])

X = datos_modelo.drop(['estado'], axis =1)
y = datos_modelo['estado']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3)#, stratify = y)"

# Modelo
modelo_rf = RandomForestClassifier()
modelo_rf.fit(X_train, Y_train)
Y_pred2 = modelo_rf.predict(X_test)


# Validaciones
cro_val = cross_val_score(modelo_rf,X,y,cv= 40, scoring= 'accuracy')
cro_val2 = cross_val_score(modelo_rf,X,y,cv= 40, scoring= 'f1_macro')

val = [cro_val.mean(),cro_val2.mean()]
names = ["Accuracy","F1 score"]
valores = pd.DataFrame(val,names)
valores.columns = ["Puntaje"]

# Pesos del modelo
columnas = X.columns
pesos_var = modelo_rf.feature_importances_
pesos_modelo = pd.DataFrame(pesos_var,columnas)
pesos_modelo.columns = ['Peso del modelo']
pesos_modelo_top = pesos_modelo.sort_values(by='Peso del modelo',ascending=False)[:20]

# Exportar bases
prob = []
for i in range(len(modelo_rf.predict_proba(X))):
    prob.append(modelo_rf.predict_proba(X)[i][1])

datos['probabilidad'] = prob
datos['clasificacion'] = modelo_rf.predict(X)
validaciones = pd.concat([pesos_modelo_top,valores], axis = 1)

datos.to_excel(url_principal + "Resultados/Training_Probabilidades de fuga de talento.xlsx")
validaciones.to_excel(url_principal + "Resultados/Training_Validaciones del modelo.xlsx")

pickle.dump(modelo_rf, open(url_principal + "Script/modelo_rf.cfg","wb"))
pickle.dump(encoder_dummies, open(url_principal + "Script/encoder_dummies.cfg","wb"))
