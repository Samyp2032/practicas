import pandas as pd
import numpy as np
import seaborn as sb

def aperturaCsv():
      arch ='Crash_Reporting_-_Drivers_Data.csv'
      crash_df = pd.read_csv(arch, sep=',')
      return crash_df

crash_df = aperturaCsv()  

"""
print("1.- Imprimimos todos los primeros 10 valores")
print(crash_df.head(10))
print("\n")
print("Para seguir pulsa enter")
input()

print("2.- Imprimimos todos los ultimos 10 valores")
print(crash_df.tail(10))
print("\n")
print("Para seguir pulsa enter")
input()

print("3.- Imprimimos el tamaño de nuestro dataset")
print(crash_df.shape)
print("\n")
print("Para seguir pulsa enter")
input()

print("4.- Imprimimos todas las columnas")
print(crash_df.columns.values)
print("\n")
print("Para seguir pulsa enter")
input()

print("5.- Imprimimos las filas")
print(crash_df.index.values)
print("\n")
print("Para seguir pulsa enter")
input()

print("6.- Imprimimos de la columna route type ordenamos")
print(crash_df['Route Type'].drop_duplicates().sort_values())
print("\n")
print("Para seguir pulsa enter")
input()

print("7.- Imprimimos de la columna route type ordenamos")
print(crash_df['Route Type'].drop_duplicates().sort_values())
print("\n")
print("Para seguir pulsa enter")
input()

print("8.- Imprimimos una funcion que saca los valores mas recurrentes de la columna que queremos")
def contar_valores():
    print("Algunos ejemplos: Route Type, Road Name, Collision Type, Speed Limit, Vehicle Make" )
    columna = str(input("Dame la columna: "))
    valores = crash_df[columna].value_counts()
    print(valores)

contar_valores()
print("\n")
print("Para seguir pulsa enter")
input()
"""

print("9.- Imprimimos una funcion que saca la marca que metemos y regresa los tipos de carros")
def tipos_de_carro_por_marca():
    marca = str(input("Dame la marca: ")).upper()
    tipos_de_carro = crash_df[(crash_df['Vehicle Make'] == marca) & (crash_df['Vehicle Model'].notna())]['Vehicle Model'].drop_duplicates().sort_values()
    print(list(tipos_de_carro))

tipos_de_carro_por_marca()

print("10.- Imprimimos una funcion que pide el año y el tipo y regresa todo los datos de su choque")
def tipo_de_anio():
    tipo = str(input("Dame el tipo: ")).upper()
    anios = crash_df[crash_df['Vehicle Model'] == tipo]['Vehicle Year'].astype(str).drop_duplicates().sort_values()
    print(list(anios))

tipo_de_anio()

def datos_por_anio():
    anio = str(input("Dame el año: ")).upper()
    datos = crash_df[(crash_df['Vehicle Year'] == anio)]
    print(datos)

datos_por_anio()