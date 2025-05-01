import pyreadstat
import pandas as pd

def cargar_datos():
    años = range(2014, 2024)##2014, 2024
    dataframes = []
    for año in años:
        archivo = f"NACI{año}.sav"
        try:
            df, meta = pyreadstat.read_sav(archivo)
            dataframes.append(df)
        except Exception as e:
            print(f"Error al cargar {archivo}: {e}")
            continue
    
    
    df = pd.concat(dataframes, ignore_index=True)


    items = ["Anotrab", "Nacio", "Sexo", "Mesnac", "Provocu", "edmadrec","edpadrec", "Nivedpad", "Nivedmad"]

    ##matrices
    ##mes
    num_a_mes = {
        1.0: "Enero", 2.0: "Febrero", 3.0: "Marzo", 4.0: "Abril",
        5.0: "Mayo", 6.0: "Junio", 7.0: "Julio", 8.0: "Agosto",
        9.0: "Septiembre", 10.0: "Octubre", 11.0: "Noviembre", 12.0: "Diciembre"
    }
    ##Sexo
    sexo_nacido = {
        1.0: "Hombre", 2.0: "Mujer"
    }

    ##Provincia
    provincia = {
        1.0: "San José", 2.0: "Alajuela", 3.0: "Cartago", 4.0: "Heredia",
        5.0: "Guanacaste", 6.0: "Puntarenas", 7.0: "Limón"
    }

    ##Edad madre
    edad_madre = {
        0.0: "Ignorada", 1.0: "Menos de 15", 2.0: "15 - 19", 3.0: "20 - 24", 4.0: "25 - 29",
        5.0: "30 - 34", 6.0: "35 - 39", 7.0: "40 - 44", 8.0: "Más de 45"
    }

    #Nivel educativo madre
    educacion_madre= {
        0.0: "Ninguno", 1.0: "Primaria incompleta", 2.0: "Primaria completa", 3.0: "Secundaria incompleta",
        4.0: "Secundaria completa", 5.0: "Universitaria incompleta", 6.0: "Universitaria completa",
        9.0: "Ignorado"
    }

    ##Edad padre
    edad_padre = {
        0.0: "Ignorada", 1.0: "Menos de 20", 2.0: "20 - 24", 3.0: "25 - 29", 4.0: "30 - 34",
        5.0: "35 - 39", 6.0: "40 - 44", 7.0: "45 - 49", 8.0: "50 y más", 9.0: "Padre no declarado"
    }

    #Nivel educativo padre
    educacion_padre= {
        0.0: "Ninguno", 1.0: "Primaria incompleta", 2.0: "Primaria completa", 3.0: "Secundaria incompleta",
        4.0: "Secundaria completa", 5.0: "Universitaria incompleta", 6.0: "Universitaria completa",
        8.0: "Padre no declarado", 9.0: "Ignorado"
    }


    df = df[items]
    df["Sexo"] = df["Sexo"].map(sexo_nacido)
    df["Mesnac"] = df["Mesnac"].map(num_a_mes)
    df["Provocu"] = df["Provocu"].map(provincia)
    df["edmadrec"] = df["edmadrec"].map(edad_madre)
    df["Nivedmad"] = df["Nivedmad"].map(educacion_madre)
    df["edpadrec"] = df["edpadrec"].map(edad_padre)
    df["Nivedpad"] = df["Nivedpad"].map(educacion_padre)


    return df





