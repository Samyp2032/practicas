import csv
import numpy as np


def read_csv(archivo): #Creamos la funcion para leer el csv con el aparametro del archivo
    data = [] #Creamos una lista vacia para almacenar los datos
    with open(archivo) as csvfile: #Abrimos el archivo y se va a la variable csvfile
        csvreader = csv.reader(csvfile) #Aqui se va leer el csv
        for i in csvreader:
            data.append(i) #Metemos los datos en la lista
    return np.array(data) #Regresamos el arreglo con numpy de los datos de la lista


data = read_csv('Amazon Laptop Data.csv')

print("\n")
print("Datos cargados:")
print(data)
print("Las dimensiones del arreglo: \n", data.shape)
print("\n")
print("Para seguir pulsa enter")
input()


precios_reales = data[1:, 3] #Asignamos la variable con el data y el arreglo excluyendo la 1 y agarrando la 3
precios = [] #Creamos una lista vacia
for precio in precios_reales: 
    precio = float(precio.replace(',', '')) # remplazamos las comas que exitan por nada
    precios.append(precio) #Metemos lo valores a la lista
precios = np.array(precios) #Creamos el arreglo con los datos sacados de la lista
precio_promedio = np.mean(precios) #Usamos la variable mean de numpy para sacar el promedio
print("Precio promedio de los laptops:", precio_promedio)
print("\n")
print("Para seguir pulsa enter")
input()


mas_caro = np.argmax(precios) #Usamos la funcion argmax para conseguir el valor maximo
mas_economico = np.argmin(precios) #Usamos la funcion argmax para conseguir el valor minimo
laptop_mas_caro = data[mas_caro+1] #Usamos la variable y un mas 1 en el dataset para no perder ningun dato
laptop_mas_economico = data[mas_economico+1]
print("Laptop más caro:", laptop_mas_caro)
print("Laptop más económico:", laptop_mas_economico)
print("\n")
print("Para seguir pulsa enter")
input()

descuentos_porcentaje = data[1:, 2] #Asignamos la variable con el data y el arreglo excluyendo la 1 y agarrando la 2
descuentos = [] #Creamos una lista vacia
for descuento in descuentos_porcentaje:
    if descuento:
        descuento = float(descuento.replace('%', '')) # remplazamos los porcentajes que exitan por nada
        descuentos.append(descuento)

descuentos = np.array(descuentos)
descuento_promedio =round(np.mean(descuentos), 2)
print("Descuento promedio de las laptops:", descuento_promedio)
print("\n")
print("Para seguir pulsa enter")
input()

calificaciones = data[1:, 4] #Asignamos la variable con el data y el arreglo excluyendo la 1 y agarrando la 4

rating = [] #Creamos una lista vacia
for calificacion in calificaciones:
    if calificacion != 'No Ratings': #Si es indiferente a la palabra no raiting agregamos calificaciones
        rating.append(float(calificacion))
    else:
        rating.append(0) #Agregamos 0 por otra parte

rating = np.array(rating) #Asignamos una variable en la que vamos a meter lo valores
calificacion_alta = np.sum(rating > 4.5) #Usamos la funcion sum para sumar los valores arriba de calificacion 4.5
print("calificación superior a 4.5:", calificacion_alta)
print("\n")
print("Para seguir pulsa enter")
input()

suma_valores = np.sum(rating) + np.sum(descuentos) #Sumamos dos arreglos y el resultado final
print("Sumamos los arreglos raiting y descuentos: ", suma_valores)
print("\n")
print("Para seguir pulsa enter")
input()

