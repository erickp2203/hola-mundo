numero = int(input("Introduce el número del que quieres ver la tabla de multiplicar: ")) #hacemos que el usuario ingrese el dato

for i in range(1, 11): #se hace un rango para multiplicar del 1 al 10
  print(f"{numero} x {i} = {numero * i}") #se imprime con la resolucion del numero ingresado * numero en el que este el rango.
