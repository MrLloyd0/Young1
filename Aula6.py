ddd = {61 : 'Brasilia', 71 : 'Salvador', 11 : 'Sao Paulo', 21 : ' Rio de Janeiro', 32 : 'Juiz de Fora', 19 : 'Campinas', 27 : 'Vitoria', 31 : 'Belo Horizonte', 67 : 'Campo Grande'}

DDD = int(input('Digite um DDD válido: '))
if DDD in ddd:
    print(ddd[DDD])
else:
    print('DDD nao existente')

    n = int(input())
totalC = 0
totalCoelho = 0
totalRato = 0
totalSapo = 0

for i in range(n):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    totalC += quantia

    if tipo == 'C':
        totalCoelho += quantia
    elif tipo == 'R':
        totalRato += quantia
    elif tipo == 'S':
        totalSapo += quantia
    
if totalC > 0:
    percentualC = (totalCoelho / totalC) * 100
    percentualR = (totalRato / totalC) * 100
    percentualS = (totalSapo / totalC) * 100
else:
    percentualC = 0
    percentualR = 0
    percentualS = 0

print(f"Total: {totalC} cobaias")
print(f"Total de coelhos: {totalCoelho}")
print(f"Total de rato: {totalRato}")
print(f"Total de sapo: {totalSapo}")
print(f"Percentual de coelhos: {percentualC:.2f} %")
print(f"Percentual de ratos: {percentualR:.2f} %")
print(f"Percentual de sapos: {percentualS:.2f} %")




  