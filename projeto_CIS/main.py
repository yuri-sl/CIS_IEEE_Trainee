from ambiente import Ambiente
from agente import Agente
import matplotlib.pyplot as plt

env = Ambiente(tamanho=10)
agent = Agente(tamanho=10)

episodios = 500
recompensas_por_ep = []

for ep in range(episodios):
    estado = env.reset()
    total_recompensa = 0

    for _ in range(100):
        acao = agent.escolher_acao(estado)
        novo_estado, recompensa, terminado = env.step(acao)
        agent.atualizar(estado, acao, recompensa, novo_estado)
        estado = novo_estado
        total_recompensa += recompensa
        if terminado:
            break

    recompensas_por_ep.append(total_recompensa)

plt.plot(recompensas_por_ep)
plt.title("Recompensa por Episódio")
plt.xlabel("Episódio")
plt.ylabel("Recompensa Total")
plt.grid(True)
plt.show()
