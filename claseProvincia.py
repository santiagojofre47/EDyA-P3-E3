class Provincia:
    __nombre = None
    __superficie_afectada = None

    def __init__(self, nombre, superficie):
        self.__nombre  = nombre
        self.__superficie_afectada = superficie
        
    def getSuperficie(self):
        return self.__superficie_afectada
    
    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return 'Provincia: {} superficia total afectada: {} hectareas' .format(self.__nombre,self.__superficie_afectada)
        
