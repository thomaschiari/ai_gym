from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State


class AspiradorPo(State):

    def __init__(self, op, robo, situacao):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = robo
        self.situacao = situacao

    def sucessors(self):
        sucessors = []
        # Acao: Direita
        sucessors.append(AspiradorPo('DIR', "DIR", self.situacao))
        # Acao: Esquerda
        sucessors.append(AspiradorPo('ESQ', "ESQ", self.situacao))
        # Acao: Limpar
        if self.posicao_robo == "DIR":
            sucessors.append(AspiradorPo('LIMPAR', "DIR", [0, self.situacao[1]]))
        else:
            sucessors.append(AspiradorPo('LIMPAR', "ESQ", [self.situacao[0], 0]))
        return sucessors

    def is_goal(self):
        if self.situacao == [0, 0] and self.posicao_robo == "DIR":
            return True
        return False

    def description(self):
        return "Aspirador de Po que deve limpar as salas. O ambiente consiste em duas salas, que podem estar sujas ou nao. O aspirador possui como acoes limpar a sala, mover-se para a esquerda ou mover-se para a direita."

    def cost(self):
        return 1

    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas
        # deve também retornar um valor que descreva aquele nodo em específico. Pois
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas:
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas:
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return self.operator


def main():
  #  print('Busca em profundidade iterativa')
    state = AspiradorPo('', "DIR", [1, 1])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()