def bellman_ford(graph, start):
    vertices = set(u for u, v, w in graph).union(v for u, v, w in graph)
    n = len(vertices)
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            return "Граф содержит отрицательный цикл"

    return distances


# Тесты
print("Запуск тестов...\n")

# Тест 1: Граф с положительными весами
graph1 = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 3, 3)
]
result1 = bellman_ford(graph1, 0)
expected1 = {0: 0, 1: 2, 2: 3, 3: 6}
print(f"{expected1}\n {result1}")

# Тест 2: Граф с отрицательными весами, но без циклов
graph2 = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]
result2 = bellman_ford(graph2, 0)
expected2 = {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
print(f"{expected2}\n {result2}")

# Тест 3: Граф с отрицательным циклом
graph3 = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 0, -1)
]
result3 = bellman_ford(graph3, 0)
expected3 = "Граф содержит отрицательный цикл"
print(f"{expected3}\n {result3}")

# Тест 4: Разреженный граф
graph4 = [
    (0, 1, 5),
    (1, 2, 3)
]
result4 = bellman_ford(graph4, 0)
expected4 = {0: 0, 1: 5, 2: 8}
print(f"{expected4}\n {result4}")
