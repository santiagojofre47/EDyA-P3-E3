import csv
from claseListaContenido import ListaEncadenada
from claseProvincia import Provincia

class Manejador:
    __lista = None

    def __init__(self):
        self.__lista = ListaEncadenada()
    
    def cargarDatos(self):
        archivo = open('SuperficieIncendios.csv', encoding='UTF-8')
        reader = csv.reader(archivo,delimiter = ';')
        band = True
        provincia = ''
        superficie = 0.0
        for fila in reader:
            if band:
                provincia = fila[3]
                superficie+=float(fila[6])
                band = False
                print(provincia)
            if provincia == fila[3]:
                if not fila[6] == '':
                    superficie+=float(fila[6])
            else:
                objeto = Provincia(provincia, superficie)
                self.__lista.insertar(objeto)
                provincia = fila[3]
               # print(provincia)
                if not fila[6] == '':
                    superficie = float(fila[6])
        archivo.close()
    
    def mostrar_datos(self):
        self.__lista.recorrer()