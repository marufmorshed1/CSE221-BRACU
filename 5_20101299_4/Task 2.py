from queue import PriorityQueue
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output2.txt", "w")

file = open("input.txt", "r")


def Dijkstra(graph_list, source):
    Q = PriorityQueue()
    visited = [False]*len(graph_list)
    dist = [999999]*len(graph_list)
    prev = [0]*len(graph_list)
    dist[source] = 0
    prev[source] = source
    Q.put((dist[source], source))
    while not Q.empty():
        u = Q.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        for v in graph_list[u]:
            alt = dist[u] + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = u
                Q.put((dist[v[0]], v[0]))
    return prev


n = int(file.readline())

for i in range(n):
    N, M = file.readline().split()
    N = int(N)
    M = int(M)
    adj_list = [[] for x in range(N+1)]
    for j in range(M):
        u, v, w = [int(x) for x in file.readline().split()]
        adj_list[u].append((v,w))
    a = Dijkstra(adj_list, 1)
    b = []

    m = M
    n = N

    home = n

    if N == 1:
        b = [1]
    else:

        while a[N] != 1:
            b.append(a[N])
            N = a[N]
        b.reverse()
        b.insert(0, 1)
        b.append(home)

    for i in b:
        print(i, end=" ")
    print()