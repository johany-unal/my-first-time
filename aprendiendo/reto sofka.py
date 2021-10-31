# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:17:19 2021

@author: joao
"""
##se tomarán 10 carriles y se crearán 10 carros 

import random

def lanzar_dado()->int:  # nos da el numero del dado para mover el carro
    dado = random.randint(1, 6)    
    return dado

def grabar_ganador(h): # Graba el ganador en un txt externo, en orden primer lugar a la izquierda, 2 a lla derecha...
    file=open("registro_pilotos_ganadores.txt","a")
    file.write(h)
    file.write( '\t')
    file.close()
    
def salta_linea()->int:  # al final del programa se hace un salto de línea en el documento txt
    file=open("registro_ganadores.txt","a")
    file.write("\n")
    file.close()
    return 0
      
    
    
class Carro(): # Creamos la case Carro
    
    def __init__(self,conductor,numero_carril):
        self.conductor=conductor
        self.numero_carril=numero_carril
        self.distancia=0                # posicion del carro en l pista, se inicializa en 0
        self.positions=0                # posicion de llegada a la meta
        self.en_podio=False
    
        
    # metodos
    def moverse(self):
        h=100*lanzar_dado()                 # movimiento del carro en metros
        return h
        

class Pista():
    limite_distancia =100       #longitud pista en Kilometros, 100 por defecto
    cantidad_carriles =5       #cantidad de carriles, 10 por defecto
    
    
class Podio():       # guarda el nombre de los pilotos y su # de auto que ganaron la carrera
    primer_puesto= ""
    segundo_puesto= "" 
    tercer_puesto= ""

    def premiar(n,h,m): # Guarda los nombres de los ganadores de la carrera
        if(n==1):
            Podio.primer_puesto=h + "  el corredor del auto "+ str(m)
        elif(n==2):
            Podio.segundo_puesto=h + "  el corredor del auto "+ str(m)
        elif(n==3):
            Podio.tercer_puesto=h + "  el corredor del auto "+ str(m)
        else:
            h
        grabar_ganador(h)  # Graba el ganador en un txt externo
    
    def mostrar_podio(): #Muestra en la consola el podium de la carrera
        print("el primer  puesto fue ",Podio.primer_puesto)
        print("el segundo puesto fue ",Podio.segundo_puesto)
        print("el tecer  puesto fue ",Podio.tercer_puesto)
        
    
     
    
    



# Programa principal

long_pist=int(input("ingrese la longitud de la pista en km ")) # pide la longitud de la pista deseada
print("tenemos una pista de ",long_pist," kilometros")
input("para iniciar la carrera opima enter ")


pista=Pista()     # se crea el objeto pista
pista.limite_distancia=long_pist # creamos una pista con los km ingresados

# creamos 10 objetos del tipo Carro,(nobre piloto, carril)
carro_01=Carro("pedro",1)
carro_02=Carro("dora",2)
carro_03=Carro("luis",3)
carro_04=Carro("paula",4)
carro_05=Carro("adrian",5)
carro_06=Carro("patricia",6)
carro_07=Carro("alfredo",7)
carro_08=Carro("lorena",8)
carro_09=Carro("daniel",9)
carro_10=Carro("marta",10)



ganadores_completos=False # indica si ya tenemos los 3 ganadores de la carrera              
contador=0
tiros_posibles=long_pist*10 # maxima cantidad de lanzamientos posibles antes que haya un ganador, medida de seguridad para no quedar atorado en el ciclo while
podium=0                                 # lugar de llegada carrera

while( not ganadores_completos and contador <tiros_posibles ):
    
    
    carro_01.distancia=carro_01.distancia + carro_01.moverse()                # lanza el dado y mueve el carro
    print("el carro 1 se encuentra en la posicion",carro_01.distancia)
    if carro_01.distancia>=pista.limite_distancia*1000 and not carro_01.en_podio: # revisa si ya llego a la meta en este turno
        podium += 1                               # aumenta el contador de lugares del podio ocupados
        carro_01.positions=podium                 # el atibuto de posición del objwto se modifica con la posicion de llegada a la meta
        carro_01.en_podio=True                    # indica que ahora tiene un puesto en el podio
        Podio.premiar(podium,carro_01.conductor,1) # guarda la informacion del auto ganador
        
        
    carro_02.distancia=carro_02.distancia + carro_02.moverse()
    print("el carro 2 se encuentra en la posicion",carro_02.distancia)
    if carro_02.distancia>=pista.limite_distancia*1000 and not carro_02.en_podio:
        podium += 1
        carro_02.positions=podium
        carro_02.en_podio=True
        Podio.premiar(podium,carro_02.conductor,2)
        
    carro_03.distancia=carro_03.distancia + carro_03.moverse()
    print("el carro 3 se encuentra en la posicion",carro_03.distancia)
    if carro_03.distancia>=pista.limite_distancia*1000 and not carro_03.en_podio:
        podium += 1
        carro_03.positions=podium
        carro_03.en_podio=True
        Podio.premiar(podium,carro_03.conductor,3)

    carro_04.distancia=carro_04.distancia + carro_04.moverse()
    print("el carro 4 se encuentra en la posicion",carro_04.distancia)
    if carro_04.distancia>=pista.limite_distancia*1000 and not carro_04.en_podio:
        podium += 1
        carro_04.positions=podium
        carro_04.en_podio=True
        Podio.premiar(podium,carro_04.conductor,4)

    carro_05.distancia=carro_05.distancia + carro_05.moverse()
    print("el carro 5 se encuentra en la posicion",carro_05.distancia)
    if carro_05.distancia>=pista.limite_distancia*1000 and not carro_05.en_podio:
        podium += 1
        carro_05.positions=podium
        carro_05.en_podio=True
        Podio.premiar(podium,carro_05.conductor,5)   
        
    carro_06.distancia=carro_06.distancia + carro_06.moverse()
    print("el carro 6 se encuentra en la posicion",carro_06.distancia)
    if carro_06.distancia>=pista.limite_distancia*1000 and not carro_06.en_podio:
        podium += 1
        carro_06.positions=podium
        carro_06.en_podio=True
        Podio.premiar(podium,carro_06.conductor,6)
        
        
    carro_07.distancia=carro_07.distancia + carro_07.moverse()
    print("el carro 7 se encuentra en la posicion",carro_07.distancia)
    if carro_07.distancia>=pista.limite_distancia*1000 and not carro_07.en_podio:
        podium += 1
        carro_07.positions=podium
        carro_07.en_podio=True
        Podio.premiar(podium,carro_07.conductor,7)
        
    carro_08.distancia=carro_08.distancia + carro_08.moverse()
    print("el carro 8 se encuentra en la posicion",carro_08.distancia)
    if carro_08.distancia>=pista.limite_distancia*1000 and not carro_08.en_podio:
        podium += 1
        carro_08.positions=podium
        carro_08.en_podio=True
        Podio.premiar(podium,carro_08.conductor,8)

    carro_09.distancia=carro_09.distancia + carro_09.moverse()
    print("el carro 9 se encuentra en la posicion",carro_09.distancia)
    if carro_09.distancia>=pista.limite_distancia*1000 and not carro_09.en_podio:
        podium += 1
        carro_09.positions=podium
        carro_09.en_podio=True
        Podio.premiar(podium,carro_09.conductor,9)

    carro_10.distancia=carro_10.distancia + carro_10.moverse()
    print("el carro 10 se encuentra en la posicion",carro_10.distancia)
    if carro_10.distancia>=pista.limite_distancia*1000 and not carro_10.en_podio:
        podium += 1
        carro_10.positions=podium
        carro_10.en_podio=True
        Podio.premiar(podium,carro_10.conductor,10)   
        
           
        
    if podium >=3:               # cuenta cuantos carros han pasado la meta
        ganadores_completos=True #si ya está elpodio copleto (primeros 3), se sale del bucle
    
    contador += 1                # cuenta los ciclos del while
    
    print("contador= ",contador," podium= ",podium," tiros posibles",tiros_posibles)
    input("para tirar los dados de nuevo oprima enter")
        


Podio.mostrar_podio()  # muestra en consola los 3 primeros conductores y carros
salta_linea()            


