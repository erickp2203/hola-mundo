numero = int(input("Introduce el número del que quieres calcular el factorial: ")) #hacemos que el usuario ingrese el dato

factorial = 1 #creamos una variable igualada a 1

for i in range(1, numero + 1): #creamos un rango de 1 hasta el numero ingresado sumandole 1
  factorial *= i    # y multiplicamos por el valor de i a la variable con +=

print(f"El factorial de {numero} es {factorial}")