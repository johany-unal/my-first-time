# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 11:36:14 2021

@author: joao
"""

def far_to_cent (x:float)->float:
    x1=x-32
    x2=x1*5/9
    return x2

def cent_to_far (x1:float)->float:
    
    x2=x1*9/5
    x=x2+32
    return x

def radianes_a_grados(g:float)->float:
        pi=3.14159
        return((360*g)/(2*pi))
    
def grados_a_radianes(g:float)->float:
        pi=3.14159
        return((2*pi*g)/(360))
    
    
def invertir_numero(numero:int)->int():
    unid=numero % 10
    numero //=10
    decenas=numero % 10
    numero //=10
    centenas=numero % 10
    numero //=10
    millares=numero % 10
     
    inverso=unid*1000 +decenas*100 +centenas*10+millares
    
    return inverso

#programa principal

#grados_f=float(input("ingrese la temperatura en faren.. "))
#grados_c=far_to_cent(grados_f)

#print("los" +str(grados_f) + "grados f equivalen a " +str(grados_c)+" grados centigrados")

#f=float(input("ingrese el angulo en grados "))
#c=grados_a_radianes(f)

#print(c)


ff=int(input("ingrese el numero a invertir     "))
c=invertir_numero(ff)

print(c)