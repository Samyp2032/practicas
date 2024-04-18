# Creamos el diccionario con listas vacías en su interior
usuarios = {
"nombres": [],
"identificaciones": []
}
# Definimos un tamaño para las listas del diccionario
# Lo puedes cambiar si quieres
tamaño = 3
# Leemos los datos y los agregamos a el diccionario
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    # La primera lista es para los nombres
    usuarios["nombres"].append(nombre)
    # La segunda lista es para las identificaciones
    usuarios["identificaciones"].append(identificación)
# Ahora mostremos los valores en el diccionario
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])