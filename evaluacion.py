
    # Diccionario  nombres y precio de las frutas
frutas = {
        "manzana": 10,
        "platano": 20,
        "naranja": 30,
        "uva": 25,
        "pera": 10
    }

print("Estos son las frutas con sus precios: ", frutas)
    # Ciclo para realizar consultas
while True:
        # Pedir nombre de la fruta y cantidad vendida
        fruta = input("Ingrese el nombre de la fruta: ").lower()
        cantidad = int(input("Ingrese la cantidad que quiere: "))

        # Verificar si la fruta existe 
        if fruta in frutas:
            precio = frutas[fruta]
            precio_total = precio * cantidad
            print(f"El precio  de {cantidad} {fruta} es: {precio_total} pesos")
        else:
            print("La fruta ingresada no esta")

        # Preguntar si desea hacer otra consulta
        continuar = input("¿Desea otra fruta? (s/n): ").lower()
        if continuar != 's':
            break
       


