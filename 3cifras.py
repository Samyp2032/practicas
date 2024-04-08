num = int(input("Dame un numero: "))

if num <= 9 and num >= 0:
    print("El numero tiene una cifra")

else: 
    if num >=10 and num <=99:
        print("El numero tiene 2 cifras")

    else: 
        if num >=100 and num <=999:
            print("El numero tiene 3 cifras")
        
        else:
            print("El numero es de 4 cifras o es negativo no es posible ERROR")
