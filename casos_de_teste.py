from digrafo import Digrafo


def main():
    G = Digrafo(ponderado=True)
    G = G.carregar_arquivo("C:\Users\Gustavo\Documentos\Faculdade\Grafos\BibliotecaGrafos\TrabalhoFinalGrafos\USA-road-d.NY.gr")
    
    menor_grau = G.mind(G)
    print(f"O menor grau é: {menor_grau}")
    
    maior_grau = G.maxd(G)
    print(f"O maior grau é: {maior_grau}") 

    caminho_10 = G.encontrar_caminho_10_arestas(G)
    if caminho_10:
        print(f"c) caminho com ≥ 10 arestas: {caminho_10}")
    else:
        print("c) nao foi encontrado caminho com ≥ 10 arestas.")
    
    ciclo_5 = G.encontrar_ciclo_com_5_arestas(G)
    if ciclo_5:
        print(f"d) ciclo com ≥ 5 arestas: {ciclo_5}")
    else:
        print("d) nao foi encontrado cicllo com ≥ 5 arestas.")

    vertice_dist, distancia = G.vertice_mais_distante(G, origem=129)
    print(f"e) vertice mais distante de 129: {vertice_dist} com distancia {distancia}")

    num_cores = G.coloracao_digrafo(G)
    print(f"f) quantidade de cores na coloração propria: {num_cores}")

if __name__ == "__main__":
    main()