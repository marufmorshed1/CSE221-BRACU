import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output2.txt", "w")

file = open("input.txt", "r")
a = file.readline()

graph = {}

i = 0
while i < int(a):
    b = file.readline().split()
    graph[b[0]] = []
    if len(b) == 1:
        graph[b[0]] = []
    else:
        j = 1
        while j < len(b):
            x = b[j]
            graph[b[0]].append(x)
            j += 1
    i += 1


visited = []
queue = []


def BFS(visited, g, node, end):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == end:
            return
        for neighbour in g[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


BFS(visited, graph, "1", "12")