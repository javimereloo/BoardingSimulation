import numpy as npy
import asignasiento as AS

class Aeronave():
    def __init__(self):
        pass

    def inicializaA320(self):
        #Defino las características de la aeronave
        self.nFilas=25
        self.nColumnas=6
    
        #Calcula el número de pasajeros
        self.nPasajeros=self.nFilas*self.nColumnas
        
        #Creamos la matriz de asientos 
        self.asientos=npy.zeros((self.nFilas,self.nColumnas))
        self.asientos[:,:]=-1
    
        #Creamos el pasillo como un array vacío
        self.colaPasillo=npy.zeros(self.nFilas)
        self.colaPasillo[:]=-1
        
        #Creamos la cola de pasajeros que esperan fuera del avión
        self.colaPasajeros=[int(i) for i in range(self.nPasajeros)]
        self.colaPasajeros=npy.array(self.colaPasajeros)
        
        #Creamos las estructuras para el número de asiento asignado
        self.colaFilaInicio=npy.zeros(self.nPasajeros)
        self.colaColumnaInicio=npy.zeros(self.nPasajeros)
        
        #Creamos los acomuladores estadísticos
        self.tiempo_espera = npy.zeros(self.nPasajeros)

        #Defino multiplicadores
        self.multiplicadorVacio=1+2
        self.multiplicadorPasillo=4+2
        self.multiplicadorMedio=5+2
        self.multiplicadorPasilloMedio=7+2
        
        #Creamos los arrays de movimiento
        moveto_loc=npy.zeros(self.nPasajeros)
        moveto_time=npy.zeros(self.nPasajeros)

        #Creamos el diccionario que recogerá el movimiento asignado de cada pasajero
        self.moveto_loc_dict={i:j for i in self.colaPasajeros for j in moveto_loc}
        #Creamos el diccionario que recogerá el tiempo que tardará en sentarse cada pasajero 
        self.moveto_time_dict={i:j for i in self.colaPasajeros for j in moveto_time}
        
    def creaOrdenAsientos(self,metodoEmbarque):
        #Asignamos el orden de entrada en función de la estrategia
        self.row_q,self.col_q=AS.asignaAsientos(self.colaFilaInicio,self.colaColumnaInicio,metodoEmbarque,self)
        
        #Creamos los diccionarios de asiento y tiempo
        self.dicci_posicion={}
        self.dicci_tiempo={}
        
        #Creamos el array para los tiempos que tarda en moverse cada persona
        mediaTiempo=2.
        desviacionTipicaTiempo=0.3
        self.tiempoMovimiento=npy.random.normal(loc=mediaTiempo,scale=desviacionTipicaTiempo,size=self.nPasajeros)

        #Declaramos el array que contine el par (fila,col) de cada pasajero
        numAsiento=npy.column_stack((self.row_q,self.col_q))
        for i in range(self.nPasajeros):
            self.dicci_posicion[i]=numAsiento[i]

        for i in range(self.nPasajeros):
            self.dicci_tiempo[i]=self.tiempoMovimiento[i]

        #Creamos la suma de tiempos
        self.suma_tiempo=npy.zeros(self.nPasajeros)
        for i in range(self.nPasajeros):
            self.suma_tiempo[i]=sum(self.tiempoMovimiento[:i+1])