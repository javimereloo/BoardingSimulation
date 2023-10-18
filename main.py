import numpy as npy
import matplotlib.pyplot as plt
import aeronave as aer
import embarque

#Creamos un objeto aeronave  
ac=aer.Aeronave()

#Definimos el array que almacena el tiempo 
time_arr=[]

#El usuario define el método a ejecutar
method = input("Ingresa el método de embarque a ejecutar [AtrasAdelante, WMA, Aleatorio, Alterno]: ")
while(method != "Aleatorio" and method != "AtrasAdelante" and method != "WMA" and method != "Alterno"):
    method = input("Ingresa el método de embarque a ejecutar [AtrasAdelante, WMA, Aleatorio, Alterno]: ")

#Número de veces que se repite la ejecución 
repeticiones = input("Ingresa el número de veces que quieres ejecutar esta estrategia (Solo se generará la anumación si ejecutas 1 repetición) ")
ac.repeat=int(repeticiones)
print(f"Se ejecutará la simulación del embarque según la estrategia {method} {ac.repeat} veces")

#Ejecuta la simulación
for i in range(ac.repeat):
    ac.inicializaA320()
    ac.creaOrdenAsientos(method)
    embarque.Embarque(ac)
    time_arr.append(ac.time)
    print("El tiempo de ejecución es {0} ejecucion n°{1} ".format(time_arr[i],i))
    print("El tiempo medio de espera ha sido {0} +/ {1:.2f}".format(npy.mean(ac.tiempo_espera), npy.std(ac.tiempo_espera)))
    print("--------------------------------------------------------------------")

#Presentamos los resultados
print("The time for method {0} is {1:.2f} +/ {2:.2f}".format(method,npy.mean(time_arr),npy.std(time_arr)))

#Animation
import matplotlib.animation as anim
from matplotlib import colors

#Solo se hace la animación si se ejecuta una vez
if(ac.repeat==1):
    #Definimos los colores del gráfico (gris para vacio, amarillo para ocupado)
    cmap = colors.ListedColormap(["gray", 'gold'])
    bounds=[-1,0,300]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    #Copio la lista de capturas en una variable local 
    img_list=ac.img_list
    #Repite la matriz del asiento final 2 veces más para que sea visible en la animación durante algún tiempo
    for i in range(2):
        img_list.append(img_list[-1])
    im=[]
    
    #Creamos la figura y la subtrama 
    fig=plt.figure(figsize=(8,13))
    ax=fig.add_subplot(111)
    ax.set_xlabel(f"Parte trasera ",fontsize=20 )
    ax.set_title("Entrada de pasajeros por aquí",fontsize=20) 
    ax.text(0.02, 0.5, f"{method}", fontsize=16, transform=plt.gcf().transFigure)

    #Creamos el Gráfico con imshow
    for i in range(len(img_list)):
        image=ax.imshow(img_list[i],animated=True,cmap=cmap,norm=norm)
        ax.set_xticks(npy.arange(-0.5,7.5,1))
        ax.set_yticks(npy.arange(-0.5,24.5,1)) 
        ax.grid(color="k",linestyle="-",linewidth=2.5)  
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        im.append([image])
    
    #Guardamos la animación 
    mov=anim.ArtistAnimation(fig,im,interval=180)
    mov.save("media/Airplane_Boarding_{0}.gif".format(method))
    print(f"Puedes consultar la animación de la simulación en la carpeta media/Airplane_Boarding_{method}.gif")
    print("NotaÑ si la carpeta ./media no existe debes crearla")
