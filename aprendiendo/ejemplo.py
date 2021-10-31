# -*- coding: utf-8 -*-

print("10 pulgadas son "+str(10*2.54)+ " centimetros")
print("10 pies son",(10*30.48),"centimetros y",(10*0.3048),"metros")

x1=int(input("ingrese valor de x1"))
x2=int(input("ingrese valor de x2"))
x3=int(input("ingrese valor de x3"))


moment=x1
x1=x3
x3=x2
x2=moment


print("El valor de x1 es  ", x1)

print("El valor de x1 es  ", x2)

print("El valor de x1 es  ", x3)

    