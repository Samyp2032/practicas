archi1=open("datos.txt","w")

archi1.write("Primer línea.\n")

archi1.write("Segunda línea.\n")

archi1.write("Tercer línea.\n")

archi1.close()

archi1=open("datos.txt","a")
archi1.write("nueva línea 1\n")
archi1.write("nueva línea 2\n")
archi1.close()
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()

archi1=open("datos.txt","w",
encoding="utf-8")
archi1.write("Primer línea.\n")
archi1.write("Segunda línea.\n")
archi1.write("Tercer línea.\n")
archi1.close()