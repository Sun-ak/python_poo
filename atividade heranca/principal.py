from Herois_Viloes import Personagem, Heroi, Vilao

p1 = Personagem("Barry Allen", "Lendário", 100)
h1 = Heroi("Ben Stiller", "Avançado", 100, "Sombra Luminosa", 50)
v1 = Vilao("Morte Negra", "Lendário", 100, 70)

p1.receberDano(40)
p1.verificarVida()
p1.detalhes()

h1.executarHabilidade("Raio de Energia")
h1.recarregarEnergia()
h1.detalhes()
h1.chamarAliado("Sombra Espectral", "Manto das Sombras")

v1.desferirGolpe("Chama Negra")
v1.detalhes()
v1.fugir("Camuflagem Sombria")
v1.planejarArmadilha("encapsulamento negro")