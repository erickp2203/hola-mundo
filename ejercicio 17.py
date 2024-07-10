peso = float(input("Introduce tu peso en kilogramos: ")) #hacemos que el usuario ingrese el dato
altura = float(input("Introduce tu altura en metros: ")) #hacemos que el usuario ingrese el dato

imc = peso / (altura ** 2) #se calcula el IMC con su formula

print(f"Tu índice de masa corporal es {imc:.2f}") #imprimimos el valor de la imc con dos decimales con [:.2f]

if imc < 18.5: #aqui solo definimos si tiene bajo peso, peso normal, sobrepeso u obesidad con los valores dispuestos
  print("Tienes bajo peso.")
elif imc >= 18.5 and imc < 25:
  print("Tienes peso normal.")
elif imc >= 25 and imc < 30:
  print("Tienes sobrepeso.")
else:
  print("Tienes obesidad.")