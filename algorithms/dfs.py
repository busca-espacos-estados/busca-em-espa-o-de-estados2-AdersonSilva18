from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        fronteira = [initial]
        visitados = set()
        expandidos = 0
        gerados = 1
        max_fronteira = 1

        while fronteira:
            max_fronteira = max(max_fronteira, len(fronteira))
            atual = fronteira.pop()

            if atual.is_goal:
                return SearchResult(atual, expandidos, gerados, max_fronteira, len(atual.path()) - 1)

            if atual in visitados or atual.cost >= self.depth_limit:
                continue
            visitados.add(atual)
            expandidos += 1

            for filho in atual.neighbors():
                if filho not in visitados:
                    fronteira.append(filho)
                    gerados += 1

        return SearchResult(None, expandidos, gerados, max_fronteira, 0)
