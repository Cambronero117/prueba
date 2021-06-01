menu = 0
contraquemada = "123"
saldo = 2000
while menu !=4:
    contra = input("dijite la contraseña ")
    if contra == contraquemada:
        print()
        while menu != 4:
            print()
            menu = int(input("Dijite el numnero que se le solicita: \n[1]Retirar [2]Depositar [3]Consultar saldo [4]Salir "))
            if menu == 1:
                retiro = float(input("Dijite el monto a retirar: "))
                if retiro <= saldo:
                    saldo = saldo - retiro
                    print(f"Su retiro ha sido efectuado con exito\nSu saldo diponible es de ${saldo}")
                else:
                    print(f"Su retiro es mayor al saldo disponible")
            elif menu ==2:
                deposito = float(input("Dijite la cantidad que dease depositar "))
                saldo = saldo + deposito
                print(f"Su deposito fue efectuado con exito\n su saldo es de ${saldo}")
            elif menu ==3:
                print(f"Su saldo disponible a la fecha es: ${saldo}")
            elif menu > 4:
                print()
                print("Error usted ha dijitado un numero que no corresponde")

    else:
        print("Su contraseña es incorrecta, dijitela nuevamente")
print("Gracias por preferirnos")