class Cachorro:
    def __init__(self, raca, nome, idade):
        self.late = False
        self.acordado = True
        self.dorme = False
        self.come = False
        self.raca = raca
        self.nome = nome
        self.idade = idade

    def raca(self):
         print(f"Minha raça é: {self.raça}")


    def come(self):
        if self.come:
         self.come = True
         print("O cachorro está comendo! Não o atrapalhe.")
        else:
            print("O cahorro já comeu, ele está satsfeito agora!")

    def late(self):
        if not self.late:
            self.late = True
            print("O cachorro deu uma latida!")

        else:
            print("o cachorro está latindo")

    def dorme(self):
        if self.acordado:
            self.acordado = True
            print("O cahorro está acordado ainda, jájá ele irá dormir talvez.")

        else:
            print("O cachorro irá dormir")

cachorro1 = Cachorro("Pinscher", "Rosana", "14")
cachorro2 = Cachorro("Pastor-Alemão", "Elbert", "23")