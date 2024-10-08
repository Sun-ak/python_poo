class Funcionario:
    def __init__(self, nome, salario):
        #Estamos mudando a visibilidade dos atributos de privado para protegido, dessa forma, as classes filhas poderão acessar os atributos da classe mãe
        self._nome = nome
        self._salario = salario

    def informacoes(self):
        print(f"Olá {self._nome}, seu salário atual é ${self._salario:.0f}")

#Criando classes filhas
class Engenheiro(Funcionario):#a classe engenheiro está herdando as caracteristicas da classe funcionario, que será sua classe mãe
    def bonusEngenheiro(self):
        self._salario = self._salario * 1.1 #Estamos aumento o salário em 10%

class Supervisor(Funcionario):
    def relatorioSupervisor(self):
        print(f"Relatório do funcionário {self._nome}: Salário atual é ${self._salario}")