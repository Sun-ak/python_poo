class Pessoa:
    #Criar o método construtor
    def __init__(self, nome, altura, idade):
        #Criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atributos.
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome} sua altura é {self.altura} e sua idade é {self.idade}")
    
#criando os objetos
p1 = Pessoa("Miguel",1.74,17)
p2 = Pessoa("Marirrah",1.56,16)

p1.exibirDados()
p2.exibirDados()