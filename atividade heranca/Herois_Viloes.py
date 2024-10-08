class Personagem:
    def __init__(self, nome, rank, vida):
        self._nome = nome
        self._rank = rank
        self._vida = vida

    def receberDano(self, dano):
        dano = dano
        self._vida = self._vida - dano
        print(f"O personagem {self._nome} recebeu {dano} de dano e está com {self._vida} de vida")

    def verificarVida(self):
        if self._vida == 0:
            print(f"O personagem {self._nome} morreu.")
        elif self._vida < 0:
            print(f"O personagem {self._nome} foi obliterado!")
        elif self._vida >= 1 and self._vida <= 40:
            print(f"O personagem {self._nome} se mantém de pé!")
        elif self._vida > 40 and self._vida <= 99:
            print(f"O personagem {self._nome} está pronto pra batalha!")
        elif self._vida == 100:
            print(f"O personagem {self._nome} está com força total!")

    def detalhes(self):
        print(f"O personagem {self._nome} do rank {self._rank} está atualmente com {self._vida} de vida.")
    
class Heroi(Personagem):
    def __init__(self, nome, rank, vida, identidadeSecreta, energia):
        super().__init__(nome, rank, vida)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        self._energia = self._energia - 10
        print(f"\nO herói {self._nome} usou a habilidade {tipoHabilidade} o que consumiu 10 de energia e atualmente está com {self._energia}")

    def recarregarEnergia(self):
        self._energia = self._energia + 5
        print(f"O héroi {self._nome} recuperou 5 de energia, estando agora com {self._energia}")

    def chamarAliado(self, nomeAliado, poderAliado):
        print(f"O herói {self._nome} trouxe para a batalha o aliado {nomeAliado} para ajudá-lo e ele utilizou o {poderAliado}")

class Vilao(Personagem):
    def __init__(self, nome, rank, vida, malicia):
        super().__init__(nome, rank, vida)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        self._malicia = self._malicia - 40
        print(f"\nO vilão {self._nome} atacou utilizando de sua habilidade {tipoGolpe} o que consumiu 40 pontos de malicia então o deixando com {self._malicia} de malicia")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"Sorrateiramente nos becos escuros da cidade o vilão {self._nome} vem preparando sua armailha mortal chamada {tipoArmadilha}!")

    def fugir(self, tipoFuga):
        print(f"O vilão {self._nome} conseguiu fugir utilizando a {tipoFuga}!\n")
