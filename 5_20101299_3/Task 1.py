import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

file = open("input.txt", "r")
a = file.readline()

graph = {}

i = 0
while i < int(a):
    b = file.readline().split()
    print(b)
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

print(graph)