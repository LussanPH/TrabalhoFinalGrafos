from grafo import Grafo

G = Grafo(True) 
"""
G.add([0, 1, 2])
G.add([1, 0, 2])
G.add([0, 2, 4])
G.add([1, 2, 1])
G.add([1, 3, 7])
G.add([2, 4, 3])
G.add([3, 4, 1])
G.add([4, 0, 5])

print(G.n())
print(G.m())
print(G.viz(0))
print(G.d(0))
print(G.w(1,3))
print(G.mind())
print(G.maxd())
print(G.bfs(0))
print(G.dfs(0))
print(G.djikstra(0))
print(G.bf(0))
print(G.coloracao_propria())
"""

with open("USA-road-d.NY.gr", 'r') as f:
    for linha in f:
        lista = linha.split()
        G.add([lista[1], lista[2], lista[3]])

    print(G.vertices)