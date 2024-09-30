from Q1 import Livro

#Solicitando dados do usuário
titulo = input("Informe o título do livro: ")
autor = input("Informe o autor do livro: ")
anoPublicacao = float(input("Em que ano o livro foi publicado? "))

l1 = Livro(titulo, autor, anoPublicacao)
l1.exibirDados()
l1.verificarIdade()
