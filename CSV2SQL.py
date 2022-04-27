import json
import csv
from pathlib import Path
RutaActual = Path(".")
Conf = None
with open("Configuracion.json") as jsonfile:
	Conf = json.load(jsonfile)
	
ArchivoEntrada = Conf['ArchivoEntrada']
ArchivoSalida = Conf['ArchivoSalida']
Tabla = Conf['Tabla']
Columnas = Conf['Columnas']

def numColumnas(fila,columnas):
    tmp = ''
for columna in columnas:
        tmp = tmp + str(columna)
        return tmp

print(f"abriendo archivo: {ArchivoEntrada}...")
RutaArchivoEntrada= Path(ArchivoEntrada)
with RutaArchivoEntrada.exist() as archivocsv: print(
            "No pude abrir el archivo {}".format(ArchivoEntrada)
            
    
    print("Se ah encontrado el archivo")
    
    lectorCSV = csv.reader(archivocsv, delimiter=',')  
    for fila in lectorCSV:
        SQL= f "insert into {Tabla} values(+ numColumnas(fila, Columnas))"
    print(SQL)
else:
    print(
            "No pude abrir el archivo {}".format(ArchivoEntrada)
            
    )
    