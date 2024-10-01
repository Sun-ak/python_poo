from academia import Aluno

#Solicitando dados do usuário
for item in range (0,2):
    nome = input("Informe seu nome: ")
    idade = input("Informe sua idade: ")
    altura = float(input("Informe sua altura? "))
    peso = int(input("Informe seu peso? "))

    a1 = Aluno(nome, idade, altura, peso)
    a1.exibirDados()
    a1.calcularImc()
