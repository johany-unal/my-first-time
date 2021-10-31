# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:01:29 2021

@author: joao
"""

def calcular_edad(dia_nacio:int,mes_nacio:int,anio_nacio:int,dia_actual:int,mes_actual:int,anio_actual:int)->str:
    cantidad_dias_nacer=((anio_nacio)*12*30)+((mes_nacio)*30)+(dia_nacio)  #cantidad dias desde año 0
    cantidad_dias_hoy=((anio_actual)*12*30)+((mes_actual)*30)+(dia_actual) #cantidad dias desde año 0
    age=cantidad_dias_hoy-cantidad_dias_nacer
    anios=age//(12*30)
    age=age%360
    meses=age//30
    age=age%30
    dias=age

    edad=str(anios)+":"+str(meses)+":"+str(dias)


    return edad

y=calcular_edad(20,10,1986,20,10,1987)