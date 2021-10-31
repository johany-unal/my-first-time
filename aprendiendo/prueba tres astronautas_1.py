def PalindromicSubstring(strParam):
  out="none"
  palindromo_encontrado=False
  l=len (strParam)
  i=0
  j=l
  maxim=0
  while i<l:
      while j>i+1 :
        #print(i,j)
        recortada=recortar_palabra(strParam,i,j)
        palindromo_encontrado=probar_palindromo(recortada)
        if palindromo_encontrado==True:
          restriccion=len(recortada)
          # print("palindromo encontrado, de ",restriccion, "caracteres")
          if restriccion > maxim and restriccion > 2:
            out=recortada
            maxim=restriccion
           

        j-=1
      i+=1
      j=l
  
  strParam = out
  return strParam

def probar_palindromo (word:str):
  palindromo=False
  p=0
  q=len(word)-1

  while p<q and word[p] == word[q]: #palabra concantidad de caracteres impar
    p+=1
    q-=1
  if p==q:
    palindromo = True

  inverted=word[::-1]        #palabra concantidad de caracteres impar
  if inverted in word:
    palindromo = True

  return palindromo

def recortar_palabra(string:str,inicio:int,final:int):
  f=inicio 
  short_word=string[inicio:final]
  # print (short_word)
  return short_word


# keep this function call here 
print(PalindromicSubstring(input()))


