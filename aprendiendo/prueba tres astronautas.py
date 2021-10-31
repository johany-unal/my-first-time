# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 07:54:12 2021

@author: joao
"""

def PalindromicSubstring(strParam):
  out="none"
  l=len (strParam)

  for i in range(0,l):
    char =strParam[i]   # toma una letra
    
    for j in range(l,i+1): # recorre el string comparando la letra, desde el final
      char_x = strParam[j]
      equal=False
      equal=letras_iguales(char,char_x)
      if equal == True:
        long_string= j-i #largo de la cadena que es posiblemente palindroma
        if long_string == 1:  # las letras están seguidas 
          out="none"
        else:
          l_s(long_string/2)-1 # el numero de veces que pueden estar repetidas
          p=False # inicializamos p en false
          for k in range(0,l_s): #compara las letras en el intervalo del posible palindromo
            p=letras_iguales(strParam[i+k],strParam[i+l_s-k])
            if p==False:
              k=l_s    # Acaba el for
            elif p: # tenemos palindromo 
              out=""
              for m in range(0,long_string): # compara las letras en el intervalo del posible palindromo
                out=out + strParam[i+m]    # concatenamos letra por letra 
  strParam=out

  # code goes here
  return strParam








def letras_iguales(char_1:str,char_2:str): # compara 2 letras, iguales=True; diferentes=False
  if char_1==char_2:
    return True
  else :
    return False

# keep this function call here 
print(PalindromicSubstring(input()))




palindromo_encontrado