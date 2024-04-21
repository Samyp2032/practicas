# Creamos el diccionario con listas vacías en su interior
usuarios = {
"nombres": [],
"identificaciones": []
}
# Definimos un tamaño para las listas del diccionario
# Lo puedes cambiar si quieres

# Leemos los datos y los agregamos a el diccionario
i=1
while True:
    continuar = str(input('Quieres meter datos? s/n: '))
    if continuar == 's':
        print("Ingrese los datos de la persona", i)
        nombre = input("Nombre: ")
        identificación = input("Identificación: ")
        # La primera lista es para los nombres
        usuarios["nombres"].append(nombre)
        # La segunda lista es para las identificaciones
        usuarios["identificaciones"].append(identificación)
        i += 1
    else:
        break
# Ahora mostremos los valores en el diccionario
n = len(usuarios["nombres"])
for i in range(n):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])