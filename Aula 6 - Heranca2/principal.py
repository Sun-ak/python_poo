from pessoa import Pessoa, Aluno, Professor

p1 = Pessoa("Julio César", 27)
a1 = Aluno("Lara", 17, 513790)
pr1 = Professor("Bruno", 35, "Computação")

p1.info()

a1.info()
a1.estudar()

pr1.info()
pr1.ensinar()