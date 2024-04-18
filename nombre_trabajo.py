
nombres = []
identificaciones = []

i=1
while True:
    continuar = str(input('Quieres meter datos?s,n: '))
    if continuar == 's':
            print("Ingrese los datos de la persona: ", i )
            nombre = input("Nombre: ")
            identificación = input("Identificación: ")
            nombres.append(nombre)
            identificaciones.append(identificación)
            i += 1
    else:
        break

n = len(nombres)       

for i in range(n):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])


