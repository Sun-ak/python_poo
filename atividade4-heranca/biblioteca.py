class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._publicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"O item {self._titulo} de {self._autor} foi publicado em {self._publicacao} possuindo, {self._numeroPagina} páginas.\n")

    def calcularIdadeItem(self):
        idade = (2024 - self._publicacao)
        if idade > 70:
            print(f"O livro {self._titulo} de {self._publicacao} com {idade} anos é um livro antigo\n")
        elif idade >= 30 and idade <= 70:
            print(f"O livro {self._titulo} de {self._publicacao} com {idade} anos é um livro recente\n")
        elif idade < 30:
            print(f"O livro {self._titulo} de {self._publicacao} com {idade} anos é um livro contemporâneo\n")

class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina <= 300:
            print(f"O livro {self._titulo} é um livro curto\n")
        else:
            print(f"O livro {self._titulo} é um livro longo\n")

class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._publicacao <= 1998:
            print(f"A {self._titulo} sendo de {self._publicacao} é uma edição especial\n")
        else:
            print(f"A {self._titulo} sendo de {self._publicacao} não é uma edição especial\n")