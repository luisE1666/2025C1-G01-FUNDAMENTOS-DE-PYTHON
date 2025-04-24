def escoger_año():
    años = range(2014, 2024)
    añoCorrecto = False
    print("\nSelecciona una opción: ")
    print("1. Ver un año")
    print("2. Ver historial de varios años")
    while(not añoCorrecto):
        opcion = int(input("\nEscoja la opcion que desea: "))
        
        if opcion == 1:
            while(True):
                año = int(input("\nSeleccione el año (2014- 2023) "))
                if(año in años):
                    añoCorrecto = True
                    año1 = año
                    año2 = año
                    print(año2)
                    break
                else:
                    print("Opcion no validad")
        #########################
        elif opcion == 2:
            while(True):
                primerAño = int(input("Seleccione el primer año (2014 - 2022): "))
                if(primerAño in años and primerAño <= 2022):
                    año1= primerAño
                    while(True):
                        segundoAño = int(input(f"Seleccione el segundo año ({año1 + 1} - 2023): "))
                        if(año1 < segundoAño <= 2023):
                            año2 = segundoAño
                            añoCorrecto = True
                            break#sale tercer while
                        else:
                            print("Valor no correcto")
                    break#sale segundo while
                else:
                    print("Valor no correcto")
        else:
            print("Valor equivocado")
            
    return año1, año2
