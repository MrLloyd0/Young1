
for I in range(1, 11):
    if I %2 == 0:
        print(I)

x = int(input("Digite um valor: "))
fibo = [0, 1, 1]
aux = 2
soma = 0

while aux < x:
    if x == 1:
        print(0)
        break
    elif x == 2:
        print(1)
        break
    
    soma = fibo[aux] + fibo[aux - 1]
    fibo.append(soma)
    aux += 1
else:
    print(fibo[-1])
