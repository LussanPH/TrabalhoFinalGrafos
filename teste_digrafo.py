from digrafo import Digrafo


def main():
    print("=== CRIANDO DÍGRAFO DE TESTE ===")
    G = Digrafo(ponderado=True)

    # Arestas do grafo (origem, destino, peso)
    arestas = [
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 1],
        [2, 4, 2],
        [3, 5, 3],
        [4, 5, 1],
        [5, 6, 2],
        [6, 3, 1],   # forma ciclo
        [6, 7, 4],
        [7, 8, 1],
        [8, 9, 2],
        [9, 10, 2],
        [10, 11, 2],
        [11, 12, 2]
    ]

    for a in arestas:
        G.add(a)

    print("\n=== INFORMAÇÕES BÁSICAS ===")
    print("Vértices:", G.vertices)
    print("Número de vértices (n):", G.n())
    print("Número de arestas (m):", G.m())

    print("\n=== TESTE DE VIZINHANÇAS ===")
    v = 3
    print(f"Outneighborhood({v}):", G.outneighborhood(v))
    print(f"Inneighborhood({v}):", G.inneighborhood(v))
    print(f"Vizinhança total viz({v}):", G.viz(v))

    print("\n=== GRAUS ===")
    print(f"outdegree({v}):", G.outdegree(v))
    print(f"indegree({v}):", G.indegree(v))
    print(f"d({v}) (grau total):", G.d(v))
    print("Menor grau do grafo (mind):", G.mind())
    print("Maior grau do grafo (maxd):", G.maxd())

    print("\n=== PESO DE UMA ARESTA ===")
    print("w(2 → 3):", G.w(2, 3))

    print("\n=== BFS A PARTIR DO VÉRTICE 1 ===")
    d_bfs, pi_bfs = G.bfs(1)
    print("Distâncias (BFS):", d_bfs)
    print("Predecessores (BFS):", pi_bfs)

    print("\n=== DFS ===")
    pi_dfs, ini, fim = G.dfs()
    print("Predecessores (DFS):", pi_dfs)
    print("Tempo de início:", ini)
    print("Tempo de término:", fim)

    print("\n=== BELLMAN-FORD A PARTIR DO VÉRTICE 1 ===")
    d_bf, pi_bf, ciclo_negativo = G.bf(1)
    if ciclo_negativo:
        print("⚠ Ciclo negativo detectado")
    else:
        print("Distâncias (BF):", d_bf)
        print("Predecessores (BF):", pi_bf)

    print("\n=== DIJKSTRA A PARTIR DO VÉRTICE 1 ===")
    d_dij, pi_dij = G.djikstra(1)
    print("Distâncias (Dijkstra):", d_dij)
    print("Predecessores (Dijkstra):", pi_dij)

    print("\n=== COLORAÇÃO PRÓPRIA ===")
    cores, k = G.coloracao_propria()
    print("Cores atribuídas:", cores)
    print("Número de cores usadas:", k)

    print("\n=== CAMINHO COM PELO MENOS 10 ARESTAS ===")
    caminho10 = G.encontrar_caminho_10_arestas()
    print("Caminho encontrado:", caminho10)

    print("\n=== CICLO COM PELO MENOS 5 ARESTAS ===")
    ciclo = G.encontrar_ciclo_com_5_arestas()
    print("Ciclo encontrado:", ciclo)

    print("\n=== VÉRTICE MAIS DISTANTE (via Dijkstra) ===")
    vd = G.vertice_mais_distante(1)
    print("Vértice mais distante:", vd)


if __name__ == "__main__":
    main()
