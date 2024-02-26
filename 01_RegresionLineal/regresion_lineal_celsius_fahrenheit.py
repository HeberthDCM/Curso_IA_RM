#Primer ejercicio de progresion lineal
import pandas as pd
import seaborn as sb

t_temperatura = pd.read_csv('01_RegresionLineal/datos.csv')
#t_temperatura.info() # informacion del conjunto de datos
t_temperatura.head()


sb.scatterplot(data=t_temperatura, x='celsius', y='fahrenheit')
input('Presione una tecka')