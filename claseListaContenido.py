#Clase lista encadenada por contenido
from claseNodo import Nodo
from claseProvincia import Provincia

class ListaEncadenada:
    __cab = None
    __sig = None
    __cant = 0
    
    def vacio(self):
        return (self.__cant == 0)

    def insertar(self, provincia):
        if self.vacio():
            nodo = Nodo(provincia)
            nodo.setSiguiente(self.__cab)
            self.__cab = nodo
            self.__cant+=1
        else:
            aux = self.__cab
            ant = aux
            encontro = False
            while not encontro and aux != None:
                if aux.getDato().getSuperficie() < provincia.getSuperficie():
                    encontro = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if aux == self.__cab:
                nodo = Nodo(provincia)
                nodo.setSiguiente(self.__cab)
                self.__cab = nodo
                self.__cant+=1
            else:
                nodo = Nodo(provincia)
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)
                self.__cant+=1
    
    def recorrer(self):
        aux = self.__cab
        while aux != None:
            print(aux.getDato())
            aux  = aux.getSiguiente()

    def suprimir(self, elemento):
        enconto = False  
        i = 0
        ant = self.__cab
        aux = self.__cab
        while not enconto and aux != None:
            if self.recuperar(i) == elemento:
                enconto = True
            else:
                i+=1
                ant = aux
                aux = aux.getSiguiente()
        if i == 0:
            self.__cab = self.__cab.getSiguiente()
        else:
            ant.setSiguiente(aux.getSiguiente())
        if not enconto:
            print('ERROR: elemento no encontrado')
        
            
    def buscar(self, elemento):
        val = None
        if not self.vacia():
            encontro = False
            aux = self.__cab
            i = 0
            while not encontro and aux != None:
                if self.recuperar(i) == elemento:
                    encontro = True
                    val = i
                else:
                    i+=1
                    aux = self.siguiente(i)
            if not encontro:
                print('ERROR: elemento no encontrado!')
        else:
            print('ERROR: Lista vacia!')
        return val
    
    def recuperar(self, p):
        val = None
        if not self.vacia():
            i = 0
            if p >= 0 and p <= self.__cant-1:
                encontro = False
                aux = self.__cab
                while not encontro and aux != None:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux= aux.getSiguiente()
                val = aux.getDato()
        return val
    

    
    



            
        