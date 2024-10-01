from conta import Conta

minhaConta = Conta(321, "José José", 2000, 500)

minhaConta.relatorio()

minhaConta.setLimite(9000)
minhaConta.relatorio()

print(f"seu limite atual é {minhaConta.getLimite()}")

minhaConta.deposita(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()