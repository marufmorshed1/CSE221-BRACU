import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output3.txt", "w")

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


visited1 = []


def dfs_visit(graph, s):
    for v in graph[s]:
        if v not in visited1:
            visited1.append(v)
            dfs_visit(graph, v)


def DFS(graph, end):
    for v in [*graph]:
        if v not in visited1:
            visited1.append(v)
            dfs_visit(graph, v)


DFS(graph, "12")

for v in visited1:
    if v == "12":
        print(v, end= " ")
        break
    print(v, end=" ")