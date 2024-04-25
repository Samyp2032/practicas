import random

def generar_lista_aleatoria(n):
    lista_aleatoria = [random.randint(1, 100) for _ in range(n)]  # Genera n números aleatorios en el rango de 1 a 100
    return lista_aleatoria

def crear_diccionario_cuadrados(lista_aleatoria):   #creamos la funcion dicciinario al cuadrado
    diccionario_cuadrados = {}
    for i, num in enumerate(lista_aleatoria, start=1):      #Creamos un for que empieza de 1
        diccionario_cuadrados[i] = num ** 2
    return diccionario_cuadrados    #Regresa el diccionario

def main():
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))     #Pedimos el tamaño de n

    lista_aleatoria = generar_lista_aleatoria(n)
    diccionario_cuadrados = crear_diccionario_cuadrados(lista_aleatoria)
    
    print("Lista de números aleatorios:", lista_aleatoria)
    print("Diccionario de cuadrados:")
    for key, value in diccionario_cuadrados.items():    #Hacemos el valor de la llava con el cuadrado
        print(f"{key}: {value}")

main()
