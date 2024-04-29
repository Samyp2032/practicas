import random

def diccionario_cuadrados(lista_aleatoria):   #creamos la funcion dicciinario al cuadrado
    diccionario_cuadrados = {}
    for i, numeros in enumerate(lista_aleatoria):      #Creamos un for que empieza de 1
        diccionario_cuadrados[i] = numeros ** 2
    return diccionario_cuadrados    #Regresa el diccionario

def lista_aleatoria(n):
    lista_aleatoria = []
    for _ in range(n):
        lista_aleatoria.append(random.randint(1, 100))
    return lista_aleatoria

n = int(input("Cantidad de que se van a generar: "))     #Pedimos el tamaño de n

lista_aleatoria = lista_aleatoria(n)
diccionario_cuadrados = diccionario_cuadrados(lista_aleatoria)

print("Lista de números aleatorios:", lista_aleatoria)
print("Diccionario de cuadrados:")
for llave, valor in diccionario_cuadrados.items():    #Hacemos el valor de la llava con el cuadrado
    print(f"{llave}: {valor}")