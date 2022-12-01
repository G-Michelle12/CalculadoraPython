# Crear una calculadora con las operaciones matematicas basicas


number1 = int(input("por favor digita el primer numero: "))
x = input ("por favor digita el operador")

number2 = int(input("por favor digita el segundo numero: "))

if x == "+":
  resultado = number1 + number2
elif x == "-":
  resultado = number1 - number2
elif x == "*":
  resultado = number1 * number2
elif x == "/":
  resultado = number1 / number2

print(resultado)  
