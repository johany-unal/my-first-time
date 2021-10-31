# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 12:51:00 2021

@author: joao
"""

def calcular_horario_llegada(h_s:int , m_s:int , s_s:int , h_d:int , m_d:int , s_d:int)->str:
    hora_salida=h_s
    minuto_salida=m_s
    segundo_salida=s_s
    duracion_horas=h_d
    duracion_minutos=m_d
    duracion_segundos=s_d


    lleva=0
    s_ll= sumar(segundo_salida,duracion_segundos,lleva)
    lleva= s_ll//60      
    s_ll=s_ll % 60

    m_ll= sumar(minuto_salida,duracion_minutos,lleva)
    lleva= m_ll//60      
    m_ll= m_ll % 60

    h_ll=sumar(hora_salida,duracion_horas,lleva)
    h_ll= h_ll % 24
    
    horario_llegada=str(h_ll)+":"+str(m_ll)+":"+str(s_ll)



    return horario_llegada

def sumar(d:int,e:int,y:int)->int:
    return d+e+y


# Programa principal
horario_llegada= calcular_horario_llegada(1,23,45,4,25,0)
print(horario_llegada)