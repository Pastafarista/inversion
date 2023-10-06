from obtener_precio_item import get_precio
import os
import time
from datetime import datetime
import pytz

ruta_carpeta = "pagina-django/precios"

cantidades = {
    "fracture-case": 14,
    "dreams-nightmares-case": 2,
    "revolution-case": 3,
    "snakebite-case": 9,
    "recoil-case": 2,
    "clutch-case": 28,
    "prisma-2-case": 15,
    "revolver-case": 1,
    "danger-zone-case": 37,
    "horizon-case": 14,
    "prisma-case": 130,
    "spectrum-2-case": 8,
    "gamma-2-case": 3,
    "paris-2023-mirage-souvenir-package": 2
}

precios = {}

def escribir_precio(nombre_item, precio_item):
    try:
        ruta = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(ruta, ruta_carpeta)
        ruta = os.path.join(ruta,nombre_item + ".txt")
        archivo = open(ruta, "a+")
        archivo.write(str(datetime.now(pytz.timezone("Europe/Madrid"))) + "~" + format(precio_item, ".2f") + "\n") 
        archivo.close()
    except:
        print("ERROR AL ABRIR EL ARCHIVO EN " + ruta)
        
def formatear_nombre(nombre_item):
    return nombre_item.replace("-", " ")

def cargar_precios():
    for nombre_item in cantidades.keys():
        
        try:
            precio_item = get_precio(nombre_item)
        except:
            print("ERROR AL ENCONTRAR EL ITEM " + nombre_item)
        
        precio_item_total = precio_item*cantidades[nombre_item]
        escribir_precio(formatear_nombre(nombre_item), precio_item_total)
        precios[nombre_item] = precio_item_total
        print("Item: " + nombre_item + " | Precio: " + format(precio_item, ".2f") + "€ | Total: " + format(precio_item_total, ".2f") + "€")
        
    escribir_precio("total", sum(precios.values()))
    
iteraciones = 0
    
while True:
    iteraciones += 1
    try:
        cargar_precios()
        print("Iteración: " + str(iteraciones) + " | Total: " + format(sum(precios.values()), ".2f") + "€")
    except:
        print("Error al cargar los precios de internet")
    print("Esperando 5 minutos...")
    time.sleep(300)
