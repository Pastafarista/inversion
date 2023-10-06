from datetime import datetime
import os
import plotly

def obtener_grafica():

    #obtener ruta relativa
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(ruta, "precios/")

    nombre_items = []
    
    graficos = []

    # Iterate directory
    for file_path in os.listdir(ruta):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(ruta, file_path)):
            # add filename to list
            nombre_items.append(file_path.split(".")[0])
    
    colores = {
        "total": "rgba(255, 0, 0, 0.8)",
        "clutch case": "rgba(0, 0, 255, 0.8)",
        "danger zone case": "rgba(255, 255, 0, 0.8)",
        "dreams nightmares case": "rgba(255, 0, 255, 0.8)",
        "fracture case": "rgba(0, 255, 255, 0.8)",
        "gamma 2 case": "rgba(255, 100, 255, 0.8)",
        "horizon case": "rgba(255, 128, 0, 0.8)",
        "paris 2023 mirage souvenir package": "rgba(0, 255, 0, 0.8)",
        "prisma 2 case": "rgba(128, 0, 128, 0.8)",
        "prisma case": "rgba(128, 128, 0, 0.8)",
        "recoil case": "rgba(0, 128, 128, 0.8)",
        "revolution case": "rgba(128, 0, 0, 0.8)",
        "revolver case": "rgba(0, 0, 128, 0.8)",
        "snakebite case": "rgba(0, 128, 0, 0.8)",
        "spectrum 2 case": "rgba(0, 0, 0, 0.8)"
    }
    
    for nombre_item in nombre_items:
        if nombre_item in colores:
            color = colores[nombre_item]
        else:
            color = "rgba(115, 246, 104, 0.8)"
    
        ruta_datos = os.path.join(ruta, nombre_item + ".txt")
        
        # leer el archivo y convertirlo en un diccionario de precios con fechas
        archivo = open(ruta_datos, "r")
        lineas = archivo.readlines()
        archivo.close()
        
        fechas = []
        precios = []
        
        for linea in lineas:
            linea = linea.replace("\n", "")
            linea = linea.split("~")
            fechas.append(linea[0])
            precios.append(linea[1])
        
        
        x = [datetime.strptime(d.split(".")[0], '%Y-%m-%d %H:%M:%S') for d in fechas]
        y = [float("{:.2f}".format(float(p))) for p in precios]

        visible = "legendonly"
        
        if nombre_item == "total":
            visible = True

        # Crear el gráfico
        
        graficos.append(plotly.graph_objs.Scatter(
                        x = x,
                        y = y,
                        mode = "lines",
                        name = nombre_item,
                        marker = dict(color = color),
                        text = nombre_item,
                        visible = visible
        ))
    
    
    layout = dict(title = "Inversión en CS:GO",
              xaxis= dict(title= 'Fecha y Hora',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Precio',ticklen= 5,zeroline= False)
             )
    
    fig = plotly.graph_objs.Figure(data = graficos, layout = layout)
    
    chart = fig.to_html(full_html=False, default_height=500, default_width=700)

    return chart

    