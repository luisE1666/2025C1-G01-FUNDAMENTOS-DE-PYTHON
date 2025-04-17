import csv, os
import pandas as pd


def ingresarVentas(lista_ventas):
    while True:
        opcion = input("Desea ingresar una nueva venta (Y/N)").upper()
        
        if(opcion == "Y"):
            try:
                curso = input("Ingrese el nombre del curso: ").upper()
                cantidad = int(input("Ingrese la cantidad que desee: "))
                precio = float(input("Ingrese el precio del curso: "))
                fecha = input("Ingrese la fecha del curso (YYYY-MM-DD): ")
                cliente = input("Ingrese el nombre del cliente: ")
            except ValueError:
                print("Entradas no validas")
                continue
            
            venta = {
                "Curso":curso,
                "Cantidad": cantidad,
                "Precio": precio,
                "Fecha": fecha,
                "Cliente": cliente
            }
            
            lista_ventas.append(venta)
            
            
        else:
            print("adios")
            break
        
        
def guardarVentas(ventas):
    if not ventas:
        print("\nNo hay ventas que guardar en el CSV")
        
        
    else:
        print("Archivo a generar")
        with open("ventas.csv", 'w', newline = '', encoding= 'utf-8') as archivo:
            guardar = csv.DictWriter(archivo,fieldnames=["Curso", "Cantidad", "Precio", "Fecha", "Cliente"])
            guardar.writeheader() #pone el titulo de las preguntas
            guardar.writerows(ventas)
        print("Archivo generado")
        

def analisisVentas():
    print("Hola")
    df = pd.read_csv("ventas.csv")
    print("\n ----------------- Resumen Ventas------------------")
    
    df['Subtotal'] = df['Cantidad'] * df['Precio']
    total_ingresos = df['Subtotal'].sum()
    print(f'Total de ventas {total_ingresos}')
    
    #Curso mas vendido
    curso_top = df.groupby("Curso")["Cantidad"].sum().idxmax()
    print(f"El curso mas vendido es {curso_top}")
    
    ##Cliente que as cursos compro
    cliente_top = df.groupby("Cliente")["Cantidad"].sum().idxmax()
    print(f"\nEl cliente que mas compro es {cliente_top}")
    
    fecha_top = df.groupby("Fecha")["Cantidad"].sum().idxmax()
    cantidad_top_fecha = df.groupby("Fecha")["Cantidad"].sum().max()
    print(f"\nLa fecha con mas ventas fue {fecha_top}, con {cantidad_top_fecha} cursos vendidos")