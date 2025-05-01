import pandas as pd

from carga_datos import cargar_datos
from moduloAños import escoger_año
from modulosNacimientos import distribucionSexo, distribucionEducativa, distribucionEdad, distribucionProvincia



def main(df):
    while True:
        
        print("Selecciona una opción:")
        print("1. Sexo del niño")
        print("2. Ver distribución por nivel educativo de los padres")
        print("3. Ver relación entre edad madre y padre")
        print("4. Ver distribución por provincia")
        print("5. Salir")
        
        opcion = input("Ingresa el número de la opción que desea: ")
        
        if opcion == '1':
            print("Mostrando datos por año...")
            año1,año2 = escoger_año()
            distribucionSexo(df, año1, año2)
            
        elif opcion == '2':
            print("Mostrando distribución por nivel educativo de la madre...")
            año1,año2 = escoger_año()
            distribucionEducativa(df, año1, año2)
            
        elif opcion == '3':
            print("Mostrando distribución por edades de los padres")
            año1,año2 = escoger_año()
            distribucionEdad(df, año1, año2)
            
        elif opcion == '4':
            print("Mostrando distribucion por provincias")
            año1,año2 = escoger_año()
            distribucionProvincia(df, año1, año2)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


##se cargan los datos como data frame
df = cargar_datos()

main(df)
