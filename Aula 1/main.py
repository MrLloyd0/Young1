salario = int(input("Digite seu sálario"))

if salario <= 1200:
    print("Estagiario")
elif salario <= 2000:
    print("Junior")
elif salario <= 3000:
    print("Avançado")
elif salario <= 5000:
    print("Sênior")
else:
    print("Gerente")