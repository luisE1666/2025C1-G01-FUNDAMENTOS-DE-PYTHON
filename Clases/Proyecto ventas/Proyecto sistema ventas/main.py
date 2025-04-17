
#Autor: Luis Chacón
#Fecha: 2025-04-16
#version: 0.1
#Sistema de gestión de ventas  
import os 
from modulo import ingresarVentas, guardarVentas, analisisVentas



    


def limpiarTerminal():
    """Esta funcion limpia la pantalla de la terminal en ejecucion
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ##Menu
def menu():
    ventas = []
    while(True):
        print("\nMenu principal")
        print("1. Ingresar ventas de cursos UMCA")
        print("2. Guardar datos en un archivo CSV")
        print("3. Analizar las ventas")
        print("4. Salir\n")
        
        try:
            opcion = int(input("\n por favor ingrese una opcion: "))
            if(opcion == 1):
                print("\n---Ingreso de ventas de productos---\n")
                limpiarTerminal()
                ingresarVentas(ventas)
                #print(ventas)
            elif(opcion == 2):
                print("---Guardar archivos en CSV")
                #limpiarTerminal()
                guardarVentas(ventas)
            elif(opcion == 3):
                print("--Analisis de ventas--")
                analisisVentas()
                
            elif(opcion==4):
                print("Gracias por su preferencia")
                limpiarTerminal()
                break
        
            else:
                print("Opcion no valida")
        except:
            print("Por favor digite una entrada valida")
    
    
if __name__ == '__main__':
    print("Bienvenidos al sistema")     
menu()