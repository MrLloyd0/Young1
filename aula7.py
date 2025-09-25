def filme_favorito(titulo):
    print(f"Meu filme favorito e: {titulo}")

filme_favorito(input())

def menor(lista):
    menorValor = lista[0]
    for x in lista:
        if (x < menorValor):
            menorValor = x
    return menorValor

def maior(lista):
    maiorValor = lista[0]
    for x in lista:
        if (x > maiorValor):
            maiorValor = x
    return maiorValor

def menorEmaior(lista):
    print(f"Menor: {menor(lista)}")
    print(f"Maior: {maior(lista)}")

menorEmaior([33, 22, 67, 42, 14, 88])


def acai(*ingredientes, tamanho="médio", cliente):
    print(f"\nPreparando um Açaí {tamanho} com os seguintes ingredientes para o {cliente}: ")
    for n in ingredientes:
        print(f"- {n}")


acai("granola", "banana", "leite em pó", tamanho = "grande", cliente = "Victor")
acai("morango", "leite em pó", "leite condensado", cliente = "João")


def dobraLencol(lencol, gaveta):
    if lencol < gaveta:
        return 0
    else:
        return 1 + dobraLencol(lencol/2, gaveta)
    
print(dobraLencol(200, 25))