import numpy as npy

#Funcion que asigna asientos a cada pasajero
def asignaAsientos(rq,cq,metodoEmbarque,ac):
    nFilas=ac.nFilas
    nPasajeros=ac.nPasajeros
    nColumnas=ac.nColumnas
    
    if(metodoEmbarque=="Aleatorio"):
        av_rows=npy.arange(0,nFilas,1)
        av_rows=npy.tile(av_rows,(nColumnas,1))
        av_rows=av_rows.T.flatten()
        av_cols=npy.arange(0,nColumnas,1)
        av_cols=npy.tile(av_cols,(nFilas,1)).flatten()
        av_asientos=npy.zeros((nPasajeros,2))
        for i in range(nPasajeros):
            av_asientos[i]=[av_rows[i],av_cols[i]]
        npy.random.shuffle(av_asientos)
        rq=av_asientos[:,0]
        cq=av_asientos[:,1]
        
    if(metodoEmbarque=="AtrasAdelante"): #150 pasajeros, 4 grupos (37 37 38 38)
        av_rows=npy.arange(0,nFilas,1)
        av_rows=npy.tile(av_rows,(nColumnas,1))
        av_rows=av_rows.T.flatten()
        av_cols=npy.arange(0,nColumnas,1)
        av_cols=npy.tile(av_cols,(nFilas,1)).flatten()
        av_asientos=npy.zeros((nPasajeros,2))
        for i in range(nPasajeros):
            av_asientos[i]=[av_rows[i],av_cols[i]]
        group1=av_asientos[:37]
        npy.random.shuffle(group1)
        group2=av_asientos[37:74]
        npy.random.shuffle(group2)
        group3=av_asientos[74:112]
        npy.random.shuffle(group3)
        group4=av_asientos[112:]
        npy.random.shuffle(group4)
        av_asientos_final=npy.concatenate((group4,group3,group2,group1))
        rq=av_asientos_final[:,0]
        cq=av_asientos_final[:,1]

    if(metodoEmbarque=="WMA"):
        ventanas_izq=npy.array([0]*nFilas)
        filas_izq=npy.arange(0,nFilas,1)
        ventanas_dch=npy.array([5]*nFilas)
        filas_dch=npy.arange(0,nFilas,1)
        ventanas=npy.concatenate((ventanas_izq,ventanas_dch))
        filas=npy.concatenate((filas_izq,filas_dch))
        asientos_ventana=npy.column_stack((filas,ventanas))
        npy.random.shuffle(asientos_ventana)
        
        medio_izq=npy.array([1]*nFilas)
        medio_dch=npy.array([4]*nFilas)
        medio=npy.concatenate((medio_izq,medio_dch))
        asientos_medio=npy.column_stack((filas,medio))
        npy.random.shuffle(asientos_medio)
        
        pasillo_izq=npy.array([2]*nFilas)
        pasillo_dch=npy.array([3]*nFilas)
        aisle=npy.concatenate((pasillo_izq,pasillo_dch))
        asientos_pasillo=npy.column_stack((filas,aisle))
        npy.random.shuffle(asientos_pasillo)
        
        av_asientos=npy.concatenate((asientos_ventana,asientos_medio,asientos_pasillo))
        rq=av_asientos[:,0]
        cq=av_asientos[:,1]

    if(metodoEmbarque == "Alterno"):
        filas_izq=npy.flip(npy.arange(0,nFilas,1))
        filas_dch=npy.flip(npy.arange(0,nFilas,1))
        filas=npy.concatenate((filas_izq,filas_dch))
        ventanas = npy.array([5]*(nFilas*2))
        for i in range(nFilas*2):
            if(i%2 == 0):
                ventanas[i] = 0
        asientos_ventana=npy.column_stack((filas,ventanas))

        medio = npy.array([4]*(nFilas*2))
        for i in range(nFilas*2):
            if(i%2 == 0):
                medio[i] = 1
        asientos_medio=npy.column_stack((filas,medio))

        pasillo = npy.array([3]*(nFilas*2))
        for i in range(nFilas*2):
            if(i%2 == 0):
                pasillo[i] = 2
        asientos_pasillo=npy.column_stack((filas,pasillo))

        av_asientos=npy.concatenate((asientos_ventana,asientos_medio,asientos_pasillo))
        rq=av_asientos[:,0]
        cq=av_asientos[:,1]

    return rq, cq
