"""
Решить задачу о раскраске графа

жадный алгоритм
"""

def greedy_coloring(graph):
    colors = {}
    for node in graph:
        used = {colors[neighbor] for neighbor in graph[node] if neighbor in colors}
        color = 0
        while color in used:
            color += 1
        colors[node] = color
    return colors

graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
result1 = greedy_coloring(graph1)
print("Пример 1 (треугольник):", result1, "Количество цветов:", max(result1.values()) + 1)

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
result2 = greedy_coloring(graph2)
print("Пример 2 (квадрат с диагональю):", result2, "Количество цветов:", max(result2.values()) + 1)


