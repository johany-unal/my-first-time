# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:31:25 2021

@author: joao
"""
import math


def semiperimetro(x1:float,x2:float,x3:float)->float:
    s=(x1+x2+x3)/2
    return s

def area_triangulo(s1:float,s2:float,s3:float)->float:
    s=semiperimetro(s1,s2,s3)
    area = math.sqrt( s * (s-s1) * (s-s2) * (s-s3) )
    return area


s1= float(input("ingrese la longitud del primer lado  " ))
s2= float(input("ingrese la longitud del segundo lado  " ))
s3= float(input("ingrese la longitud del tercer lado  " ))
area_final=area_triangulo(s1,s2,s3)
print("el area del triangulo es ", area_final)