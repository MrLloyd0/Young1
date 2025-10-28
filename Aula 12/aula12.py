class Casa():

    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep
    def endrereçoCompleto(self):
        return "Endereço Completo: "+self.rua+ ", "+self.bairro+ ", "+self.cep
    
casa1 = Casa(rua="Mato grosso", bairro="Carandá", cep="987654321")
print(casa1.endrereçoCompleto)