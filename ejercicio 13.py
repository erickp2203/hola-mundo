cadena = input("Introduce una cadena: ") #hacemos que el usuario ingrese la cadena

vocales = 0 #creamos una variable igualada a 0

for caracter in cadena:    #busco el caracter en la cedena ingresada
  if caracter in "aeiouAEIOU": #ingreso como caracter a buscar las vocales en minusculas y mayusculas
    vocales += 1    #si cumple con lo anterior sumo a las vocales +1

print(f"La cadena '{cadena}' contiene {vocales} vocales.")