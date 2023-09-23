# dfs search way

from typing import List


class Solusion:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        if n == 1:
            return True
        graph = {}
        for edge in edges:
            parent = edge[0]
            child = edge[1]
            graph[parent] = child

        return graph


s = Solusion()
print(
    s.validPath(
        10,
        [
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        5,
        9,
    )
)
