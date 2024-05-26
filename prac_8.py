#%%
import matplotlib.pyplot as plt #importamos librerias
import seaborn as sns
import numpy as np
import matplotlib
from PIL import Image

fig, axes = plt.subplots(2, 3, figsize=(30,20))# Se crea una figura con una cuadrícula de 2x3 subgráficas.

# Datos para los rendimientos de cultivos
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]# istas con los rendimientos de manzanas y naranjas en toneladas por hectárea.
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896]

# Rendimientos de Cultivos en Baja California
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o--r')#Se trazan las curvas de rendimiento para manzanas y naranjas.
axes[0,0].set_xlabel('Año')#Se establecen las etiquetas de los ejes, la leyenda y el título.
axes[0,0].set_ylabel('Rendimiento (toneladas por hectárea)')
axes[0,0].legend(['Manzanas', 'Naranjas'])
axes[0,0].set_title('Rendimientos de Cultivos en Kanto')

# Longitud del Sépalo vs. Ancho del Sépalo
flowers_df = sns.load_dataset("iris")
axes[0,1].set_title('Longitud del Sépalo vs. Ancho del Sépalo')
sns.scatterplot(x=flowers_df.sepal_length,
                y=flowers_df.sepal_width,
                hue=flowers_df.species,
                s=100,
                ax=axes[0,1])#Se crea un gráfico de dispersión de longitud vs. ancho del sépalo.
axes[0,1].set_xlabel('Longitud del Sépalo (cm)')#Se establecen las etiquetas de los ejes.
axes[0,1].set_ylabel('Ancho del Sépalo (cm)')

# Histograma de la distribución del ancho del sépalo
setosa_df = flowers_df[flowers_df.species == 'setosa']#Igualamos variables filtran los datos de flowers_df para crear tres DataFrames separados para cada especie
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
axes[0,2].set_title('Distribución del Ancho del Sépalo')
axes[0,2].hist([setosa_df.sepal_width,
                versicolor_df.sepal_width,
                virginica_df.sepal_width],
                bins=np.arange(2, 5, 0.25),
                stacked=True)#Se crea un histograma de distribución del ancho del sépalo para cada especie de flor.
axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica'])#Se establecen las etiquetas de los ejes, la leyenda y el título.
axes[0,2].set_xlabel('Ancho del Sépalo (cm)')
axes[0,2].set_ylabel('Frecuencia')

# Gráfico de barras para cuentas del restaurante
tips_df = sns.load_dataset("tips")
axes[1,0].set_title('Cuentas del Restaurante')
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0])#Se crea un gráfico de barras para las cuentas del restaurante, diferenciadas por día y sexo.
axes[1,0].set_xlabel('Día')#Se establecen las etiquetas de los ejes.
axes[1,0].set_ylabel('Cuenta Total (USD)')

# Mapa de calor para tráfico aéreo
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")#Cargamos el data set con los idices mes, anio con valor pasajeros
axes[1,1].set_title('Tráfico Aéreo')
sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1])#Se crea un mapa de calor para el tráfico aéreo.
axes[1,1].set_xlabel('Año')
axes[1,1].set_ylabel('Mes')

# Mostrar una imagen
img = Image.open('Data Science Meme.jpg')
img_array = np.array(img)
axes[1,2].set_title('Meme de Ciencia de Datos')#Se muestra una imagen de un meme de ciencia de datos.
axes[1,2].imshow(img)
axes[1,2].grid(False)
axes[1,2].set_xlabel('Eje X')#Se muestra los ejes
axes[1,2].set_ylabel('Eje Y')

# %%
