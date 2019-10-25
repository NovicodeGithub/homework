#Novikov Daniil AI-183
# Variant 10

from random import randrange
import time
from datetime import datetime
import re

def createMatrix(V, G):
    Matrix = []

    for i in range(0, V):
        Matrix.append([])
        for j in range(0, V):
            Matrix[i].append(0)

    for i in range(0, len(G)):
        Matrix[G[i][0]][G[i][1]] = G[i][2]
        Matrix[G[i][1]][G[i][0]] = G[i][2]

    return Matrix


def prim_algorithm(V, G):
    Matrix = createMatrix(V, G)

    vertex = 0

    MST = []
    edges = []
    visited = []
    minEdge = [None, None, float('inf')]

    while len(MST) != V - 1:
        visited.append(vertex)

        for r in range(0, V):
            if Matrix[vertex][r] != 0:
                edges.append([vertex, r, Matrix[vertex][r]])

        for e in range(0, len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]

        edges.remove(minEdge)

        MST.append(minEdge)

        vertex = minEdge[1]
        minEdge = [None, None, float('inf')]

    return MST

graph = [
    [0, 1, 1],
    [0, 3, 2],
    [0, 4, 10],
    [1, 2, 6],
    [1, 5, 10],
    [2, 5, 8],
    [2, 7, 4],
    [3, 5, 5],
    [3, 6, 1],
    [4, 6, 7],
    [4, 7, 8],
    [5, 7, 2],
    [6, 7, 4]
]
print("MST of Prim's algorithm: ")
print(prim_algorithm(8, graph))


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def algorithm_of_kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("\nMST of Kruskal's algorithm: ")
        print("Vertex A   Vertex B  Weight")
        for u, v, weight in result:
            print("%5d %9d %10d" % (u, v, weight))


g = Graph(8)
g.addEdge(0, 1, 7)
g.addEdge(0, 3, 5)
g.addEdge(0, 4, 3)
g.addEdge(1, 2, 8)
g.addEdge(1, 5, 9)
g.addEdge(2, 5, 10)
g.addEdge(2, 7, 6)
g.addEdge(3, 5, 7)
g.addEdge(3, 6, 6)
g.addEdge(4, 6, 10)
g.addEdge(4, 7, 6)
g.addEdge(5, 7, 3)
g.addEdge(6, 7, 4)

g.algorithm_of_kruskal()
