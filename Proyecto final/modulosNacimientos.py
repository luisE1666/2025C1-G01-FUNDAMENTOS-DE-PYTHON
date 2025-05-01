import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import seaborn as sns


###########################################################Impresion de graficos######################################################

#1 pie, 2 barras, 3 barras dobles, 4 area apilada, 5 barras
def graficar(tipo_grafico, datos, criterio, titulo, eje_x, eje_y, color1=None, color2=None, ax=None, etiqueta=None): # se crea una funcion generica para crear los graficos del informe
    
##########################################################Grafico barras pie##########################################################################
    if tipo_grafico == 1: ## de la funcion, si tipo_grafico es 1, se genera un grafico tipo pie

        
        wedges, texts, autotexts = ax.pie( #wedges son las porciones del pie, texts los textos fijos(labels) y autotext los que se crean por calculos
            datos, #de la funcion carga los datos que se van a graficar
            labels=criterio, #los labels seran los criterios de graficar, por ejemplo hombre y mujer
            autopct='%1.1f%%', # se solicita que el % que se imprimira tenga 1 decimal
            startangle=90, # el primer corte del grafico es verticar, a las 12h
            labeldistance=1.1 # para alejar un poco el texto, ya que en ocasiones se superpone
        )
#        ax.legend( # se crea un cuadro de con la informacion de lo que se esta graficando
 #           wedges,# se adjunta a cada porcion un nombre
  #          [f"{c}: {v}" for c, v in zip(criterio, datos)], # se crea el texto para cada uno de los wedges, usando un for
   #         title="Cantidad", # se crea el nombre del cuadro de la informacion
    #        loc="best" # se le indica a matplotlib que coloque el cuadro en la mejor posición
     #   )
        ax.set_title(titulo) # el titulo del grafico se toma de la funcion
        if len(texts)>4:#para rotar el texto en los casos que hayan muchas particiones
            for text in texts:
                text.set_fontsize(9)
                text.set_rotation(25)
        ax.axis('equal') # hace que los ejes x y y sean iguales, para mejor visualizcion al ser redondo

##########################################################Grafico lineas#####################################################################
    
    elif tipo_grafico == 2:# opcion 2 genera un grafico de lineas

        
        ax.plot(criterio, datos, marker='o', label= etiqueta) # de la funcion se toman el criterio para el nombre de datos, datos para graficar y marker para la forma del punto
        ax.set_title(titulo) #de la funcion se toman los datos para los titulos principales y de losejes
        ax.set_xlabel(eje_x)
        ax.set_ylabel(eje_y)

##########################################################Grafico barras dobles#######################################################################

    elif tipo_grafico == 3:
        

        
       
        hombres = datos[0]  # Se separan los datos, del vector que se pasan los datos
        mujeres = datos[1]

        x = np.arange(len(criterio))# con len se obtiene la cantidad de datos a graficar (ej: 12 meses), y con arange(n) se crea un vector
        # el cual es el centro donde se colocara cada par de barras
        ancho = 0.35 # ancho total de cada par de barras

        ax.bar(x - ancho/2, hombres, width=ancho, label='Hombres', color = color1) #barra del primer dato, con x - ancho/2 se le da es espacio de la izquierda
        ax.bar(x + ancho/2, mujeres, width=ancho, label='Mujeres', color = color2) #barra del segundo dato

        ax.set_title(titulo)#nombre del titulo
        ax.set_xlabel(eje_x)#nombre eje x
        ax.set_ylabel(eje_y)#nombre eje y
        ax.set_xticks(x) # se posicionan las barras en el eje x
        ax.set_xticklabels(criterio)# se reemplazan los valores de x (0, 1, etc por len) por los datos de criterio
        ax.legend() # Se muestra la leyenda para identificar las barras


##########################################################Grafico area apilada#######################################################################
    elif tipo_grafico == 4:

        datos.plot.area(ax=ax, colormap="tab10")## con plot.area se hace el grafico de area  
        ax.set_title(titulo)
        ax.set_xlabel(eje_x)
        ax.set_ylabel(eje_y)
        ax.legend(title="Nivel educativo", bbox_to_anchor=(1.05, 1), loc='upper left') ## bbox_to_anchor posiciona la caja de informacion fuera del grafico en loc


######################################################### Grafico barras ##############################################################################
        
    elif tipo_grafico == 5:

        #plt.bar(datos, criterio)#plt.bar hace el grafico de barras
        ax.bar(datos, criterio, color=color1)#se crea el grafico de barras con ax.bar
        ax.set_title(titulo)
        ax.set_xlabel(eje_x)
        ax.set_ylabel(eje_y)
        ax.set_xticks(range(len(datos)))#se asignan las etiquetas de cada barra               
        ax.set_xticklabels(datos, rotation=45) 











####################################################################################################################



def distribucionSexo(df, año1, año2):
     # se utiliza la funcion escoger_año, para que el usuario escoja el o los años a evaluar
    

    if(año1==año2): #si ambos años es el mismo, significa que se seleccionó analizar un año en particular
        df_Año_sexo = df[df["Anotrab"] == año1] #Se seleccionan los datos del año seleccionado

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6)) # se crea el subplot (fig), se le asignan dos graficos (ax1 y ax2)

        # --- Gráfico de pie ---
        conteo_sexo = df_Año_sexo["Sexo"].value_counts() # se cuentan los valores a graficar, hombre y mujer
        labels = conteo_sexo.index # se toman los nombres de conteo_sexo
        valores = conteo_sexo.values # valores son los datos que se graficarán
        graficar(1, valores, labels, "Distribución anual por sexo", "", "",ax=ax1) # se pasa a la funcion los datos para graficar

        # --- Gráfico de doble barras ---
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        # se ordenan los datos del df para que salgan segun los meses del año, no de la primera ocurrencia en la lista

        #se crean los vectores de los datos separados, filtrando por sexo, contando por mes, y si no hubieran datos, se rellenara con 0
        hombres_mes = df_Año_sexo[df_Año_sexo["Sexo"] == "Hombre"]["Mesnac"].value_counts().reindex(meses, fill_value=0).values
        mujeres_mes = df_Año_sexo[df_Año_sexo["Sexo"] == "Mujer"]["Mesnac"].value_counts().reindex(meses, fill_value=0).values
        titulo = (f"Nacimientos por mes y sexo en {año1}")

        graficar(3, [hombres_mes, mujeres_mes], meses, titulo, "Mes", "Cantidad", "skyblue", "pink", ax=ax2)

        plt.tight_layout() 
        plt.show() # se imprime el grafico
        
            
 
    else:
        años = range(año1,año2+1)
        df_Año_sexo = df[df["Anotrab"].isin(años)] # se seleccionan los datos de los años que se van a evaluar
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

        # --- Gráfico de pie ---
        conteo_total_sexo = df_Año_sexo["Sexo"].value_counts()
        labels = conteo_total_sexo.index
        valores = conteo_total_sexo.values
        titulo = (f"Distribución total por sexo ({año1} - {año2})")

        graficar(1, valores, labels, titulo , "", "", ax=ax1)

        hombres_por_año = df_Año_sexo[df_Año_sexo["Sexo"] == "Hombre"]["Anotrab"].value_counts().sort_index()
        mujeres_por_año = df_Año_sexo[df_Año_sexo["Sexo"] == "Mujer"]["Anotrab"].value_counts().sort_index()
        titulo2 = (f"Nacimientos por año y sexo ({año1} - {año2})")

        graficar(3, [hombres_por_año.values, mujeres_por_año.values], años,titulo2, "Año", "Cantidad", "skyblue", "pink", ax=ax2)
        # se usa el grafico de barras dobles para ver la comparacion entre hombres y mujeres
        plt.tight_layout()
        plt.show() # se imprime el grafico


#######################################Distribucion por nivel de educacion###############################################################

def distribucionEducativa(df, año1, año2):
    if año1 == año2:
        df_Año_educacion = df[df["Anotrab"] == año1]

        
        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Gráfico de pie: Mujeres
        conteo_madre_mujer = df_Año_educacion[df_Año_educacion["Sexo"] == "Mujer"]["Nivedmad"].value_counts()
        labels_m = conteo_madre_mujer.index
        valores_m = conteo_madre_mujer.values
        tituloM = f"Distribución educación (Madre) - Mujeres - Año {año1}"
        graficar(1, valores_m, labels_m, tituloM, "", "", ax=ax1)

        # Gráfico de pie: Hombres
        conteo_madre_hombre = df_Año_educacion[df_Año_educacion["Sexo"] == "Hombre"]["Nivedmad"].value_counts()
        labels_h = conteo_madre_hombre.index
        valores_h = conteo_madre_hombre.values
        tituloH = f"Distribución educación (Madre) - Hombres - Año {año1}"
        graficar(1, valores_h, labels_h, tituloH, "", "", ax=ax2)

        plt.tight_layout()
        plt.show()

        # --- Mapa de calor con seaborn---
        #Se hace uso de otro paquete de los que se investigó en el curso, seaborn. primero se crea una variable
        #para agrupar (groupby) por las variables, en este caso el nivel de educacion. con size() se calcula
        #los valores de las combinaciones de las variables. si no hubiera, se rellena con 0
        fig2, ax3 = plt.subplots(figsize=(10, 8))
        cruzado = df_Año_educacion.groupby(["Nivedmad", "Nivedpad"]).size().unstack(fill_value=0)

        #ya con seaborn, se utiliza la funcion heatmap, para el mapa de calor, primero se ingresan los datos
        #, con annot= True, se habilita mostrar la cantidad en la matriz, fmt = d redondea por si hubiese flotantes
        #cmap="YlGnBu", es la escala de colores, de amarillo a azul, y ax3 es el eje donde se imprimirá
        

        sns.heatmap(cruzado, annot=True, fmt="d", cmap="YlGnBu", ax=ax3)
        ax3.set_title(f"Educación de la madre vs del padre ({año1})")
        ax3.set_xlabel("Educación del padre")
        ax3.set_ylabel("Educación de la madre")
        ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')

        plt.tight_layout()
        plt.show()


    else:
        años = range(año1,año2+1)
        df_Año_educacion = df[df["Anotrab"].isin(años)]

        fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6))

        # --- Grafico de area apilada madre---
        conteoMadre = df_Año_educacion.groupby(["Anotrab", "Nivedmad"]).size().unstack(fill_value=0)
        proporcionesMadre = conteoMadre.div(conteoMadre.sum(axis=1), axis=0)
        tituloMadre =(f"Evolución educación madre ({año1} - {año2})")
        graficar(4, proporcionesMadre, None, tituloMadre, "Año", "Proporción", ax=ax1)

        # --- Grafico de area apilada padre---
        conteoPadre = df_Año_educacion.groupby(["Anotrab", "Nivedpad"]).size().unstack(fill_value=0)
        proporcionesPadre = conteoPadre.div(conteoPadre.sum(axis=1), axis=0)
        tituloPadre =(f"Evolución educación padre ({año1} - {año2})")
        graficar(4, proporcionesPadre, None, tituloPadre, "Año", "Proporción", ax=ax2)


        plt.tight_layout()
        plt.show()

        #---Mapa de calor por años---

        plt.figure(figsize=(14, 6))
        sns.heatmap(proporcionesMadre.T, annot=True, cmap="YlOrBr", cbar_kws={'label': 'Proporción'})
        plt.title(f"Mapa de calor: educación madre ({año1} - {año2})")
        plt.xlabel("Año")
        plt.ylabel("Nivel educativo madre")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # --- Mapa de calor padre ---
        plt.figure(figsize=(14, 6))
        sns.heatmap(proporcionesPadre.T, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Proporción'})
        plt.title(f"Mapa de calor: educación padre ({año1} - {año2})")
        plt.xlabel("Año")
        plt.ylabel("Nivel educativo padre")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

#######################################Distribucion por edad###############################################################

def distribucionEdad(df, año1, año2):
    #se decide utilizar las mismas caracteristicas del analisis por educacion

    if año1 == año2:
        df_Año_edad = df[df["Anotrab"] == año1]

        # ---------- PRIMERA FIGURA: PIES ----------
        fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Gráfico de pie: Mujeres
        conteo_edad_mujer = df_Año_edad[df_Año_edad["Sexo"] == "Mujer"]["edmadrec"].value_counts()
        labels_m = conteo_edad_mujer.index
        valores_m = conteo_edad_mujer.values
        tituloM = f"Distribución edad madre - Año {año1}"
        graficar(1, valores_m, labels_m, tituloM, "", "", ax=ax1)

        # Gráfico de pie: Hombres
        conteo_edad_hombre = df_Año_edad[df_Año_edad["Sexo"] == "Hombre"]["edpadrec"].value_counts()
        labels_h = conteo_edad_hombre.index
        valores_h = conteo_edad_hombre.values
        tituloH = f"Distribución edad padre - Año {año1}"
        graficar(1, valores_h, labels_h, tituloH, "", "", ax=ax2)

        plt.tight_layout()
        plt.show()

        # --- Mapa de calor con seaborn---
        fig2, ax3 = plt.subplots(figsize=(10, 8))
        cruzado = df_Año_edad.groupby(["edmadrec", "edpadrec"]).size().unstack(fill_value=0)

        sns.heatmap(cruzado, annot=True, fmt="d", cmap="YlGnBu", ax=ax3)
        ax3.set_title(f"Edad de la madre vs del padre ({año1})")
        ax3.set_xlabel("Edad del padre")
        ax3.set_ylabel("Edad de la madre")
        ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha='right')

        plt.tight_layout()
        plt.show()


    else:
        años = range(año1,año2+1)
        df_Año_edad = df[df["Anotrab"].isin(años)]

        fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6))

        # --- Grafico de area apilada madre---
        conteoMadre = df_Año_edad.groupby(["Anotrab", "edmadrec"]).size().unstack(fill_value=0)
        proporcionesMadre = conteoMadre.div(conteoMadre.sum(axis=1), axis=0)
        tituloMadre =(f"Evolución edad madre ({año1} - {año2})")
        graficar(4, proporcionesMadre, None, tituloMadre, "Año", "Proporción", ax=ax1)

        # --- Grafico de area apilada padre---
        conteoPadre = df_Año_edad.groupby(["Anotrab", "edpadrec"]).size().unstack(fill_value=0)
        proporcionesPadre = conteoPadre.div(conteoPadre.sum(axis=1), axis=0)
        tituloPadre =(f"Evolución edad padre ({año1} - {año2})")
        graficar(4, proporcionesPadre, None, tituloPadre, "Año", "Proporción", ax=ax2)


        plt.tight_layout()
        plt.show()

        #---Mapa de calor por años---

        plt.figure(figsize=(14, 6))
        sns.heatmap(proporcionesMadre.T, annot=True, cmap="YlOrBr", cbar_kws={'label': 'Proporción'})
        plt.title(f"Mapa de calor: edad de la madre ({año1} - {año2})")
        plt.xlabel("Año")
        plt.ylabel("Edad de la madre")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # --- Mapa de calor padre ---
        plt.figure(figsize=(14, 6))
        sns.heatmap(proporcionesPadre.T, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Proporción'})
        plt.title(f"Mapa de calor: edad del padre ({año1} - {año2})")
        plt.xlabel("Año")
        plt.ylabel("Edad del padre")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()



#######################################Distribucion por provincia####################################################################

def distribucionProvincia(df, año1, año2):

    
    if año1 == año2:
        df_Año_provincias = df[df["Anotrab"] == año1]
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        
        conteo_provincia_hombre = df_Año_provincias[df_Año_provincias["Sexo"] == "Hombre"]["Provocu"].value_counts()
        labels_hombre = conteo_provincia_hombre.index 
        valores_hombre = conteo_provincia_hombre.values        
        titulo_hombre =(f"Nacimientos hombres por provincia ({año1}")
        
        graficar(5, labels_hombre, valores_hombre, titulo_hombre, "Provincias", "Cantidad", "skyblue", ax=ax1)

        conteo_provincia_mujer = df_Año_provincias[df_Año_provincias["Sexo"] == "Mujer"]["Provocu"].value_counts()
        labels_mujer = conteo_provincia_mujer.index 
        valores_mujer = conteo_provincia_mujer.values        
        titulo_mujer =(f"Nacimientos mujeres por provincia ({año1}")
        
        graficar(5, labels_mujer, valores_mujer, titulo_mujer, "Provincias", "Cantidad", "pink", ax=ax2)
        
        plt.tight_layout()
        plt.show()
        #se crean dos graficos de barras, para hombres y mujeres



        
    else:


        años = range(año1, año2 + 1)

        sanJose = []
        alajuela = []
        cartago = []
        heredia = []
        puntarenas = []
        guanacaste = []
        limon = []
        #se crea un vector vacio para cada provincia, y un vector con todos los años seleccionados por el usuario
        #en el for, se recorre cada año en el vector años, y se agrega con append segun la provincia a cada vector

        for año in años:
            df_Año_provincias = df[df["Anotrab"] == año]

            sanJose.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "San José"]))
            alajuela.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Alajuela"]))
            cartago.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Cartago"]))
            heredia.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Heredia"]))
            puntarenas.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Puntarenas"]))
            guanacaste.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Guanacaste"]))
            limon.append(len(df_Año_provincias[df_Año_provincias["Provocu"] == "Limón"]))

        vectores = [sanJose, alajuela, cartago, heredia, puntarenas, guanacaste, limon]
        provincias = ["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]

        # Se crea un vector, con los vectores de cada provincia, para recorrerlo, y modificar la cantidad obtenidas
        #en el for anterior para sacar el % del crecimiento
        for provincia in vectores:
            tasas = [None]
            for i in range(1, len(provincia)):
                tasa = ((provincia[i] - provincia[i - 1])/provincia[i - 1])*100
                tasas.append(tasa)
            provincia[:] = tasas

        # Se crea el eje ax para graficar, y con un for se recorre el cada uno de los datos, vectores[i] y se almacena
        # para graficarlos en el plt.show(). Se debe de tener en cosideracion de que aunque el titulo se coloca despues
        #se debe de incluir, ya que no es valor posicional
        fig, ax = plt.subplots(figsize=(10, 6))

        for i in range(len(provincias)):
            graficar(tipo_grafico=2, datos=vectores[i], criterio=años, titulo="", eje_x="Año", eje_y="Tasa de crecimiento", ax=ax, etiqueta=provincias[i])

        ax.set_title(f"Tasa de crecimiento de nacimientos por provincia ({año1} - {año2})")
        ax.legend()
        plt.tight_layout()
        plt.show()




        
        



        
 
