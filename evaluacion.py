
    # Diccionario con los nombres y precios de las frutas
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
        cantidad = int(input("Ingrese la cantidad vendida: "))

        # Verificar si la fruta existe en el diccionario
        if fruta in frutas:
            precio_unitario = frutas[fruta]
            precio_total = precio_unitario * cantidad
            print(f"El precio total de {cantidad} {fruta} es: {precio_total} pesos")
        else:
            print("¡Error! La fruta ingresada no está en el diccionario.")

        # Preguntar si desea hacer otra consulta
        continuar = input("¿Desea hacer otra consulta? (s/n): ").lower()
        if continuar != 's':
            break
       


