class personagem:
    def __init__(self, nome, idade, classe, raça, nivel,):
        self.nome = nome
        self.nivel = nivel
        self.idade = idade
        self.classe = classe
        self.raça = raça
        self.vida = 100
        self.força = 10
        self.mana = 50
        self.agilidade = 10
        self.inteligente = 20
        self.dano_de_magoa = 10

    def mostrar_status(self):
        print("==== STATUS DO SEU PERSONAGEM ====")
        print(f"classe: {self.classe}")
        print(f"idade: {self.idade}")
        print(f"nivel: {self.nivel}")
        print(f"nome: {self.nome}")
        print(f"raça: {self.raça}")
        print(f"vida: {self.vida}")
        print(f"mana: {self.mana}")
        print(f"inteligencia: {self.inteligente}")
        print(f"agilidade: {self.agilidade}")
        print(f"força: {self.força}")
        print("==============================\n")


    def atacar(self, alvo):
        dano = self.força * self.nivel
        alvo.vida -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        if alvo.vida  <= 0:
            print(f"{alvo.nome} foi derrotado")
        else:
            print(f"{alvo.nome} ainda tem {alvo.vida} de vida\n")

    def subir_de_nivel(self):
        self.nivel += 1
        self.força += 2
        self.inteligencia += 5
        self.mana += 10
        self.vida += 10
        print(f"{self.nome} subiu de nivel para {self.nivel}")

    def uso_de_magia(self, alvo):
        dano_magia = self.dano_de_magoal * self.nivel
        alvo.vida -= dano_magia
        print(f"{self.nome} soltou uma mágia que gastou 5 de mana e deu {dano_magia} de dano!")
        if alvo.vida <= 0:
            print(f"{self.nome} derrotou {alvo.nome} com sua magia!")
        else:
            print(f"{alvo.nome} ainda tem {alvo.vida} de vida")