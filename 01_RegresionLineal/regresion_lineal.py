#pruebas
import pandas as pd
import seaborn as sb


datos_persona = pd.read_csv('alturas-pesos.csv')
sb.scatterplot(x='Peso', y='Altura', data = datos_persona)