num1 = int(input("Dame numero 1: "))

num2 = int(input("Dame numero 2: "))

num3 = int(input("Dame numero 3: "))

if num1 == num2 or num1 == num3 or num3 == num2:
    print("Son iguales alguno de los tres son iguales")

elif num1 > num2 and num1 > num3:
    print("Numero 1 es mayor")

elif num2 > num1 and num2 > num3:
    print("Numero 2 es mayor")

else:
    print("El numero 3 es el mayor")