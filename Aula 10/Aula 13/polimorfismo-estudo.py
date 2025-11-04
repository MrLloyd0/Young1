class animais:
    raise NotImplementedError("Essa função deve ser subscritas nas funções a baixo")

class Cachorro(animais):
   def som(self):
        return "Au au!"

class Gato(animais):
   def som(self):
        return "Miau miau!"

class Pato(animais):
   def som(self):
        return "Quak quak!"

def testar_som(objeto):
    print(objeto.voar())

h = Gato()
p = Cachorro()
j = Pato()

testar_som(h)
testar_som(p)
testar_som(j)