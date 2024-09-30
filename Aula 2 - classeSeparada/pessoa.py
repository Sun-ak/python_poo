class Pessoa:
    #Método construtor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

    #criando métodos
    def exibirDados(self):
        print(f"Olá meu hobby atual é, {self.hobby}")

    def mudarHobby(self, novoHobby):
        self.hobby = novoHobby
        print(f"Meu hobby foi mudado para {self.hobby}")
