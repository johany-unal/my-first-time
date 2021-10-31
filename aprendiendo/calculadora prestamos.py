# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 09:57:12 2021

@author: joao
"""

cantidad =int(input("ingrese valor del prestamo "))
tasa_de_interes=float(input("la tasa de interes en % "))
numero_de_años =int(input("ingrese numero de años "))

valor_total=cantidad*(1+tasa_de_interes/100)**numero_de_años

print("el valor final del crédito es " +str(valor_total)+ "despues de ",numero_de_años)