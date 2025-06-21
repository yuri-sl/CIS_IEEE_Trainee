import numpy as np

class Ambiente:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.estado_inicial = (0, 0)
        self.objetivo = (tamanho - 1, tamanho - 1)
        self.armadilhas = [(3, 3), (4, 4), (5, 5)]
        self.reset()

    def reset(self):
        self.agente_pos = self.estado_inicial
        return self.agente_pos

    def estado_valido(self, pos):
        x, y = pos
        return 0 <= x < self.tamanho and 0 <= y < self.tamanho

    def step(self, acao):
        x, y = self.agente_pos
        movimentos = {
            0: (-1, 0),  # cima
            1: (1, 0),   # baixo
            2: (0, -1),  # esquerda
            3: (0, 1),   # direita
        }
        dx, dy = movimentos[acao]
        nova_pos = (x + dx, y + dy)

        if self.estado_valido(nova_pos):
            self.agente_pos = nova_pos

        recompensa = -1
        terminado = False

        if self.agente_pos in self.armadilhas:
            recompensa = -10
            terminado = True
        elif self.agente_pos == self.objetivo:
            recompensa = 10
            terminado = True

        return self.agente_pos, recompensa, terminado
