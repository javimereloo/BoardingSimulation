import numpy as npy

#Definimos el proceso de embarque en un bucle 
#Definimos las condiciones iniciales
def Embarque(ac):
    ac.time=0 #Inicializamos el reloj 
    ac.tiempoEspera = npy.array([0]*ac.nPasajeros)
    
    n_iter=0
    tiempo_iteración=3.6 #Tiempo en comprobar la situación de cada uno de los pasajeros (por iteración)
    suma_fuera=npy.sum(ac.colaPasajeros)
    suma_dentro=npy.sum(ac.asientos)
    
    #Definimos variables para la ilustración 
    ac.img_list=[]
    iters_per_snap=2 #Velocidad de la animación
    
    while(suma_dentro!=suma_fuera):
        #Intento meter un pasajero al avión
        if(ac.colaPasajeros.size!=0):   
            ac.colaPasillo,ac.colaPasajeros,ac.suma_tiempo=MueveAlPasillo(ac.time,ac.colaPasillo,ac.colaPasajeros,ac.suma_tiempo, ac.tiempo_espera)
        #Busco en el pasillo huecos libres (valores no negativos) 
        for passg in ac.colaPasillo:
            if(passg!=-1):
                #Almacenamos la fila del pasajero actual en el pasillo
                row=int(npy.where(ac.colaPasillo==passg)[0][0])
                #Comprobamos si se le ha asignado un movimiento al pasajero
                if(ac.moveto_time_dict[passg]!=0):
                    #Como se ha asignado un movimiento comprobamos si toca moverse
                    if(ac.time>ac.moveto_time_dict[passg]):
                        #Sí toca moverse, comprobamos si toca avanzar o sentarse 
                        if(ac.moveto_loc_dict[passg]=="a"):
                            #Toca avanzar, miramos si la posición siguiente está libre
                            if(ac.colaPasillo[row+1]==-1):
                                #Está libre, muevo al pasajero hacia adelante
                                ac.colaPasillo[row+1]=passg
                                ac.colaPasillo[row]=-1
                                #Reestablecemos el moviemiento
                                ac.moveto_loc_dict[passg]=0
                                ac.moveto_time_dict[passg]=0
                        elif(ac.moveto_loc_dict[passg]=="s"):
                            #Toca sentarse, primero localizo mi asiento
                            passg_row=int(ac.dicci_posicion[passg][0])
                            passg_col=int(ac.dicci_posicion[passg][1])
                            #Sentamos al pasajero cambiando el valor de la matriz de asientos
                            ac.asientos[passg_row,passg_col]=passg
                            #Libero el pasillo
                            ac.colaPasillo[row]=-1
                elif(ac.moveto_time_dict[passg]==0):
                    #Si no se ha asignado un movimiento compruebo la ubicación del pasajero
                    passg_row=int(ac.dicci_posicion[passg][0])
                    passg_col=int(ac.dicci_posicion[passg][1])
                    if(passg_row==row):
                        #Si la fila del pasajero es en la que se encuentra, le asignamos que se siente
                        ac.moveto_loc_dict[passg]="s"
                        #Comprobamos en que posicion se sienta: pasillo, medio o ventana
                        #En función de eso, le asignamos un tiempo de movimiento
                        if(passg_col==0): #si se sienta en ventana 
                            if(ac.asientos[passg_row,1]!=-1 and ac.asientos[passg_row,2]!=-1): #si los adyacentes están ocupados
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasilloMedio*ac.dicci_tiempo[passg]
                            elif(ac.asientos[passg_row,1]!=-1): #si el medio está ocupado 
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorMedio*ac.dicci_tiempo[passg]                                   
                            elif(ac.asientos[passg_row,2]!=-1): #si el pasillo está ocupado
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasillo*ac.dicci_tiempo[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorVacio*ac.dicci_tiempo[passg]
                        elif(passg_col==5): #si se sienta en ventana
                            if(ac.asientos[passg_row,4]!=-1 and ac.asientos[passg_row,3]!=-1):#si los adyacentes están ocupados
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasilloMedio*ac.dicci_tiempo[passg]
                            elif(ac.asientos[passg_row,4]!=-1):#si el medio está ocupado 
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorMedio*ac.dicci_tiempo[passg]                                   
                            elif(ac.asientos[passg_row,3]!=-1):#si el pasillo está ocupado
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasillo*ac.dicci_tiempo[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorVacio*ac.dicci_tiempo[passg]
                        elif(passg_col==1): #si se sienta en medio
                            if(ac.asientos[passg_row,2]!=-1): #si el pasillo está ocupado
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasillo*ac.dicci_tiempo[passg] 
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorVacio*ac.dicci_tiempo[passg]
                        elif(passg_col==4): #si se sienta en medio
                            if(ac.asientos[passg_row,3]!=-1): #si el pasillo está ocupado
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorPasillo*ac.dicci_tiempo[passg]
                            else:
                                ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorVacio*ac.dicci_tiempo[passg]
                        elif(passg_col==2 or passg_col==3):
                            ac.moveto_time_dict[passg]=ac.time+ac.multiplicadorVacio*ac.dicci_tiempo[passg]
                    elif(passg_row!=row):
                        #Si el pasajero no está en la fila en la que se sienta le asignamos que avance 
                        ac.moveto_loc_dict[passg]="a"
                        #Le asignamos un tiempo para moverse
                        ac.moveto_time_dict[passg]=ac.time+ac.dicci_tiempo[passg]

        #Animacion
        if(n_iter%iters_per_snap==0 and ac.repeat==1):
            snap=ac.asientos.copy()
            snap=npy.insert(snap,3,ac.colaPasillo,axis=1)
            ac.img_list.append(snap)
        
        #Actualizamos contadores
        ac.time+=tiempo_iteración
        n_iter+=1
        suma_dentro=npy.sum(ac.asientos)
    
    #Animación
    if(ac.repeat==1):
        snap=ac.asientos.copy()
        snap=npy.insert(snap,3,ac.colaPasillo,axis=1)
        ac.img_list.append(snap)

#Método que mueve a los pasajeros hacia dentro del nave
def MueveAlPasillo(t,colaPasillo,colaPasajeros,suma_tiempo, tiempo_espera):
    if(t>suma_tiempo[0]):
        if(colaPasillo[0]==-1):
            colaPasillo[0]=colaPasajeros[0].copy()
            tiempo_espera[colaPasajeros[0]]=t
            colaPasajeros=npy.delete(colaPasajeros,0)
            suma_tiempo=npy.delete(suma_tiempo,0)
    return colaPasillo,colaPasajeros,suma_tiempo
