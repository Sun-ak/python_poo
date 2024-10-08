from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("John", 40000)
e1 = Engenheiro("Wick", 40000)
s1 = Supervisor("Dog", 50000)

f1.informacoes()

e1.bonusEngenheiro()
e1.informacoes()

s1.relatorioSupervisor()


