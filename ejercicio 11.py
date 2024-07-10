num = int(input("ingrese un numero: ")) #hacemos que el usuario ingrese el dato

sum = 0 #creamos una variable igualada a 0

for i in range(1, num + 1): #creamos un rango de 1 hasta el numero ingresado sumandole 1
  sum = sum + i          # y sumamos a la variable el valor del sum mas el del rango en el que este y guardamos en sum con +=

print("La suma de todos los numeros naturales hasta", num, "es", sum)