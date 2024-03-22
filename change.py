def change():
    expense = 23.75
    money = 100
    line = ""


    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print(line)
    print("Vuelto")
    print(line)
    print("Pesos:")
    print(int(money - expense))
    print("Centavos:")
    print(int((money - expense - int(money - expense))*100))
change()
