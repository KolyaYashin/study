from typing import List
from typing import Tuple


def find_connected_components(pairs):
    from collections import defaultdict, deque

    # Построение графа в виде списка смежности
    graph = defaultdict(list)
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Функция для выполнения DFS
    def dfs(node, visited, component):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component.append(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    visited = set()
    components = []

    # Выполнение DFS для всех узлов
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, visited, component)
            components.append(component)

    return components



def extend_matches(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    components = find_connected_components(pairs=pairs)
    pairs = set()

    for component in components:
        for i in range(len(component)):
            for j in range(i+1, len(component)):
                if (component[i], component[j]) not in pairs and (component[j], component[i]) not in pairs:
                    if component[j] >= component[i]:
                        pairs.add((component[i], component[j]))
                    else:
                        pairs.add((component[j], component[i]))

    return sorted(pairs)



# Пример использования
matches = [(1, 2), (7, 2)]
print(extend_matches(matches))
