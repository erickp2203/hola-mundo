def palindromo(string): #definimos una funcion llamada palindromo
  string = string.lower().replace(" ", "") #transformamos la cadena ingresada a minusculas con .lower y con .replace quitamos el espacio si es que hay en la cadena
  return string == string[::-1] #revierto la cadena con [::-1]

palabra = input("ingrese el texto: ") #hacemos que el usuario ingrese la cadena

if palindromo(palabra): #ingreso la condicion que si la palabra esta en el palindromo haga lo siguiente
  print(f"{palabra} es un palindromo.")
else:                   # y lo contrario si no lo esta
  print(f"{palabra} no es un palindromo.")