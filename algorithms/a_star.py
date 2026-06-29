import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        total = 0
        for indice, peca in enumerate(state.tiles):
            if peca == 0:
                continue
            objetivo = peca - 1
            linha, coluna = divmod(indice, 3)
            linha_obj, coluna_obj = divmod(objetivo, 3)
            total += abs(linha - linha_obj) + abs(coluna - coluna_obj)
        return total

    def search(self, initial: State) -> SearchResult:
        fronteira = [(self.heuristic(initial), initial)]
        visitados = set()
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            max_fronteira = max(max_fronteira, len(fronteira))
            _, atual = heapq.heappop(fronteira)

            if atual.is_goal:
                return SearchResult(atual, expandidos, gerados, max_fronteira, len(atual.path()) - 1)

            if atual in visitados:
                continue
            visitados.add(atual)
            expandidos += 1

            for filho in atual.neighbors():
                if filho not in visitados:
                    f = filho.cost + self.heuristic(filho)
                    heapq.heappush(fronteira, (f, filho))
                    gerados += 1

        return SearchResult(None, expandidos, gerados, max_fronteira, 0)
