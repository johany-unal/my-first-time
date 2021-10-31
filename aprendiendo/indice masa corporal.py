# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:46:11 2021

@author: joao
"""


def calcular_BMI(peso_lb:float,altura_inch:float)->float:
    peso_kg = peso_lb * 0.45
    altura_m = altura_inch * 0.025
    BMI=(peso_kg/(altura_m**2))
    return BMI

peso= 220       # peso en libras
altura= 78     #altura en pulgadas

BMI=calcular_BMI(peso,altura)
print("su indice de masa corporal es "+str(BMI))