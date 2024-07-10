numero = int(input("Introduce un número: "))#hacemos que el usuario ingrese el dato

if numero <= 1:#condicion porque cualquier valor < 1 no es primo
  print(f"{numero} no es un número primo.")
else:
  es_primo = True #al no cumplir la anterior condicion va a ser verdadera
  for i in range(2, int(numero**0.5) + 1): #se crea un rango desde 2 hasta la raiz cuadradada del numero ingresado + 1
    if numero % i == 0:                    #se debe calcular hasta valores menores que la raiz cuadrada para mejorar la eficiencia del programa
      es_primo = False                     #ya que los numeros mayores a la raiz cuadrados no me sirven de mucho
      break                                #por ejemplo la raiz cuadrada de 25 es 5 al ser 25 divisor de 5 no es primo y no me sirve buscar numeros mas alla de 5
  if es_primo:
    print(f"{numero} es un número primo.")
  else:
    print(f"{numero} no es un número primo.")