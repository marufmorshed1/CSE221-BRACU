from queue import PriorityQueue
import sys

sys.stdin = open("input.txt", "r")
# sys.stdout = open("output1.txt", "w")

file = open("input.txt", "r")


def Dijkstra(Graph, source):
    Q = PriorityQueue()
    visited = [False]*len(Graph)
    dist = [999999]*len(Graph)
    dist[source] = 0
    Q.put((dist[source], source))
    while not Q.empty():
        u = Q.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        for v in Graph[u]:
            alt = dist[u] + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                Q.put((dist[v[0]], v[0]))
    print(dist)
    print (dist[len(Graph)-1])


n = int(file.readline())

for i in range(n):
    N, M = file.readline().split()
    N = int(N)
    M = int(M)
    adj_list = [[] for x in range(N+1)]

    for j in range(M):
        x = file.readline().split()
        u = int(x[0])
        v = int(x[1])
        w = int(x[2])
        adj_list[u].append((v, w))
    Dijkstra(adj_list, 1)
