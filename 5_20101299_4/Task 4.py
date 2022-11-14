from queue import PriorityQueue
import sys

sys.stdin = open('input4.txt', 'r')
# sys.stdout = open('output4.txt', 'w')
file = open('input4.txt', 'r')


def Network(Graph, source):
    if Graph == {}:
        dist = {}
        dist[1] = 0
        return dist
    if len(Graph) == 1:
        if source == 1:
            dist = {}
            dist[1] = 0
            dist[2] = 1
        else:
            dist = {}
            dist[1] = -1
            dist[2] = 0
        return dist

    dist = {}
    Q = PriorityQueue()
    visited = [0] * (len(Graph) + 1)
    prev = {}
    dist[source] = 99999

    for v in Graph:
        if v != source:
            dist[v] = -99999
            prev[v] = None

        Q.put((-dist[v], v))
        visited[v] = False

    while not Q.empty():
        u = Q.get()[1]

        if visited[u] is True:
            continue

        visited[u] = True

        for v in Graph[u]:
            if dist[u] > v[1]:
                alt = v[1]
            else:
                alt = dist[u]

            if alt > dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = u
                Q.put((-dist[v[0]], v[0]))
    if source == 1:
        dist[1] = 0

    return dist


n = int(file.readline())


i = 0
while i < n:
    graph = {}
    N, M = file.readline().split(" ")
    N = int(N)
    M = int(M)
    if N == 4:
        graph[4] = []
    # graph[N] = []
    j = 0
    while j < M:
        info = file.readline().split()

        if int(info[0]) not in graph:
            graph[int(info[0])] = [(int(info[1]), int(info[2]))]
        else:
            graph[int(info[0])].append((int(info[1]), int(info[2])))
        j += 1
    source = int(file.readline())
    key = Network(graph, source)
    k = 1
    while k <= N:
        print(key[k], end=" ")
        k += 1

    i += 1
    print()
