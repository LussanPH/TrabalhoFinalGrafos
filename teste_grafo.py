from grafo import Grafo

G = Grafo(True) 

with open("USA-road-d.NY.gr", 'r') as f:
    for linha in f:
        lista = linha.split()
        G.add(int(lista[1]), int(lista[2]), int(lista[3]))

    print(G.n())
    print(G.m())
    print(G.viz(1000))
    print(G.d(1000))
    print(G.w(1000, 1003))
    print(G.w(1003, 1000))
    print(G.mind())
    print(G.maxd())
    #print(G.bfs(1))
    #print(G.dfs(100)[1])
    #print(G.djikstra(1))
    #print(G.bf(1))
    print(G.coloracao_propria())