Valor1 = (input()).split(' ')
codigo1 = int (Valor1[0])
numPeca1 = int (Valor1[1])
valorUnitario1 = float (Valor1[2])

Valor2 = (input()).split(' ')
codigo2 = int (Valor1[0])
numPeca2 = int (Valor1[1])
valorUnitario2 = float (Valor1[2])

X = (numPeca1 * valorUnitario1) +  (numPeca2 * valorUnitario2)

print(f"VALOR À PAGAR: {X:.2f}")