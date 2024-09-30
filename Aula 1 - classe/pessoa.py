class Pessoa:
    #atributos
    nome = "Miguel"
    peso = "80"
    escolaridade = "Ensino Médio"

    #métodos
    def falar(self, texto):
        print(f"Tenho algo para te falar: {texto}")

#Criando objetos

pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("Boa tarde! Hoje é segunda-feira")