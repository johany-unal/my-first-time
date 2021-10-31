# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 00:20:31 2021

@author: joao
"""

def palindromo(num:int)->bool:
    prueba=False
    if num%10 == int(num/100):
        prueba=False
    else:
        prueba=False
    return prueba

def par(num)->bool:
    num_par=False
    if num%2==0:
        num_par=True
    else:
        num_par=False

    return num_par

def clasificar_regalo(id:int)->str:
    etiqueta="nada"
    if id>999 or id<100:
        return "el numero no está en el rango"
    elif palindromo(id)==True:
        if par(id)==True:
            etiqueta="boy"
        if not par(id)== True:
            etiqueta="girl"


    else:
        if par(id)==True:
            etiqueta="man"
        if not par(id)== True:
            etiqueta="woman"

    return etiqueta


id=242
salida=clasificar_regalo(id)