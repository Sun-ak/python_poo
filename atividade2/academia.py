class Aluno:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibirDados(self):
        print(f"Olá! {self.nome} de {self.idade} anos sua altura é {self.altura} e seu peso é {self.peso:.0f}Kg")

    def calcularImc(self):
        Imc = self.peso / (self.altura ** 2)
        print(f"Seu imc atual é {Imc:.2f}")
