# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 23:39:44 2021

@author: joao
"""

Tarifa basica   int 5000000
temporada      if (alta y baja)
compania_aerea  if (ALAS o VOLAR)

    ALAS temporada alta +30%
    VOLAR temporada alta + 20%

    
edad         int
    ALAS menor edad -50%
    VOLAR menor de edad -50%, 60 anios +100000
    
    
estudiante   bool
    ALAS estudiante SI and mayores de edad  -10% temporada baja
    
    
def palindromo(num:int)->bool:
    prueba=False
    if num%10 == int(num/100):
        prueba=True
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