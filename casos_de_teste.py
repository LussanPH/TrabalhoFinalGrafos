from digrafo import Digrafo


def main():
    try:
        G = Digrafo(ponderado = True)
        # Tenta carregar o arquivo
        G.carregar_arquivo('USA-road-d.NY.gr')
        print(f"Arquivo carregado")
    except FileNotFoundError:
        print("Erro: O arquivo do grafo não foi encontrado no caminho especificado.")
        return # Encerra se o arquivo não puder ser carregado
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o grafo: {e}")
        return
    
    print(f"Vértices: {G.n()}")
    print(f"Arestas: {G.m()}")
    menor_grau = G.mind()
    print(f"O menor grau é: {menor_grau}")
    
    # maior_grau = G.maxd()
    # print(f"O maior grau é: {maior_grau}") 

    # caminho_10 = G.encontrar_caminho_10_arestas()
    # if caminho_10:
    #     print(f"c) caminho com ≥ 10 arestas: {caminho_10}")
    # else:
    #     print("c) nao foi encontrado caminho com ≥ 10 arestas.")
    
    # ciclo_5 = G.encontrar_ciclo_com_5_arestas()
    # if ciclo_5:
    #     print(f"d) ciclo com ≥ 5 arestas: {ciclo_5}")
    # else:
    #     print("d) nao foi encontrado cicllo com ≥ 5 arestas.")

    # vertice_dist, distancia = G.vertice_mais_distante(origem=129)
    # print(f"e) vertice mais distante de 129: {vertice_dist} com distancia {distancia}")

    # cores, num_cores = G.coloracao_propria()
    # print(f"f) quantidade de cores na coloração própria: {num_cores}")
    
if __name__ == "__main__": 
    main()