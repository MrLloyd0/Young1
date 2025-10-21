import math 

print(math.pow (2,3))

print(math.ceil (2.5))

print(math.trunc (2.5))


import cauculadora as cal

numA = int(input("Olá! Qual sera o primeiro numero da operação?: "))

numB = int(input("Ok! Qual será o segundo agora?: "))

oper = input("Qual sera o tipo da operação? Soma, Subtração, Divisão ou Multiplicação?: ")

if oper == "+":
    print(cal.soma(numA, numB))

elif oper == "-":
    print(cal.subtracao(numA, numB))

elif oper == "x":
    print(cal.multiplicacao(numA, numB))

elif oper == "/":
    print(cal.divisao(numA, numB))

else:
    print("Não tem isso não pae")