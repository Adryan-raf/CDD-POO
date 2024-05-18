class Pessoa:
    def _init_(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def comer(self):
        if self.falando == True:
            print(f"{self.nome} não pode comer, pois está falando.")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer, pois está dormindo.")
        else:
            self.comendo = True
            print(f"{self.nome} está comendo.")

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar, pois está comendo.")
        elif self.dormindo == True:
            print(f"{self.nome} está falando enquanto dorme.")
        else:
            self.falando = True
            print(f"{self.nome} está falando.")

    def dormir(self):
        if self.falando == True:
            print(f"{self.nome} não pode dormir, pois está falando.")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir, pois está comendo.")
        else:
            self.dormindo = True
            print(f"{self.nome} está dormindo.")
