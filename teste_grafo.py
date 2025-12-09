from grafo import Grafo

G = Grafo(True) 

arestas = [
    [1, 2, 2],
    [1, 3, 5],
    [2, 3, 1],
    [2, 4, 2],
    [3, 5, 3],
    [4, 5, 1],
    [5, 6, 2],
    [6, 3, 1],   
    [6, 7, 4],
    [7, 8, 1],
    [8, 9, 2],
    [9, 10, 2],
    [10, 11, 2],
    [11, 12, 2]
]

for aresta in arestas:
    G.add(int(aresta[0]), int(aresta[1]), int(aresta[2]))
    
print(f"Número de vértices: {G.n()}\n")
print(f"Número de arestas: {G.m()}\n")
print(f"Vizinhos do vértice 3: {G.viz(3)}\n")
print(f"Grau do vértice 2: {G.d(2)}\n")
print(f"Peso da aresta (9, 10): {G.w(9, 10)}\n")
print(f"Verificando se a ordem das arestas não importa para o comando w: {G.w(10, 9)}\n")
print(f"Grau mínimo do grafo: {G.mind()}\n")
print(f"Grau máximo do grafo: {G.maxd()}\n")
print("BFS:")
print(f"Distâncias de cada vértice do grafo para o vértice 1: {G.bfs(1)[0]}")
print(f"Predecessores de cada vértice do grafo: {G.bfs(1)[1]}\n")
print("DFS:")
print(f"Predecessores de cada vértice do grafo: {G.dfs(1)[0]}")
print(f"Tempo de início de cada vértice do grafo: {G.dfs(1)[1]}")
print(f"Tempo de fim de cada vértice do grafo: {G.dfs(1)[2]}\n")
print("DJIKSTRA:")
print(f"Distâncias de cada vértice do grafo para o vértice 1: {G.djikstra(1)[0]}")
print(f"Predecessores de cada vértice do grafo: {G.djikstra(1)[1]}\n")
print("BELLMAN-FORD:")
print(f"Distâncias de cada vértice do grafo para o vértice 1: {G.bf(1)[0]}")
print(f"Predecessores de cada vértice do grafo: {G.bf(1)[1]}\n")
print("COLORAÇÃO PRÓPRIA:")
print(f"Cores de cada vértice do grafo: {G.coloracao_propria()[0]}")
print(f"Quantidade de cores do grafo: {G.coloracao_propria()[1]}")