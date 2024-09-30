class Livro:

    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def verificarIdade(self):
        if self.anoPublicacao <= 1974:
            print("ESTE LIVRO É UM CLÁSSICO")
        else:
            print("ESTE LIVRO AINDA NÃO É UM CLÁSSICO")

    def exibirDados(self):
        print(f"O livro {self.titulo} do autor {self.autor} foi publicado em {self.anoPublicacao}")
