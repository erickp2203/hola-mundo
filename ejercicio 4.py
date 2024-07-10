nume1 = int(input("ingrese un numero ")) #hacemos que el usuario ingrese el dato
nume2 = int(input("ingrese un numero ")) #hacemos que el usuario ingrese el dato

print("que operacion desea realizar:\n1.suma\n2.restar\n3.multiplicar\n4.dividir") #se imprime con el \n para dar un espacio o un enter entre cada linea
resp= input("ingrese el numero ") #hacemos que el usuario ingrese la opcion que quiera hacer
if resp == "1":
  print(nume1 + nume2) #imprimimos la operacion segun la opcion escogida
elif resp == "2":
  print(nume1 - nume2) #imprimimos la operacion segun la opcion escogida
elif resp == "3":
  print(nume1 * nume2) #imprimimos la operacion segun la opcion escogida
elif resp == "4":
  print(nume1 / nume2) #imprimimos la operacion segun la opcion escogida