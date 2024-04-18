# Creamos la tabla con listas vacías al comienzo
usuarios = [[], []]
# Definimos un tamaño para las listas de la tabla
# Lo puedes cambiar si quieres
tamaño = 3
# Leemos los datos y los agregamos a la tabla
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    # La primera lista es para los nombres
    usuarios[0].append(nombre)
    # La segunda lista es para las identificaciones
    usuarios[1].append(identificación)
    # Ahora mostremos los valores en la tabla
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios[0][i])
    print("Identificación:", usuarios[1][i])