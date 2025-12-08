from collections import deque
import heapq

class Digrafo:
    """
    Classe Digrafo (grafo dirigido).
    Representa um dígrafo com:
      - lista de vértices (self.vertices)
      - conjunto auxiliar para checagem rápida de existência (self._vertices_set)
      - flag se é ponderado (self.ponderado)
      - dicionário de arestas com peso: keys são tuplas (u, v) -> peso (self.arestas)
      - lista de adjacência de saída: self.listaAdj[u] = [v1, v2, ...]
      - lista de adjacência de entrada: self.listaIN[v] = [u1, u2, ...] 
    """    
    def __init__(self, ponderado=False):
        self.vertices = []
        self._vertices_set = set() 
        self.ponderado = ponderado
        self.arestas = {}
        self.listaAdj = {}
        self.listaIN = {}

    def add_vertice(self, v):  # Adiciona vértice ao grafo

        if v not in self._vertices_set:
            self.vertices.append(v)
            self._vertices_set.add(v)
            self.listaAdj[v] = []
            self.listaIN[v] = []
    
    def add_aresta(self, u, v, peso=None): # Adiciona aresta direcionada (u -> v) com peso opcional

        if not self.ponderado or peso is None:
            peso = 1

        # Garante que os vértices existem
        self.add_vertice(u)
        self.add_vertice(v)

        # Salva a aresta com peso
        if (u, v) not in self.arestas:
            self.arestas[(u, v)] = peso

        # Salva adjacência (direcionado)
        if v not in self.listaAdj[u]:
            self.listaAdj[u].append(v)
        if u not in self.listaIN[v]:
            self.listaIN[v].append(u)
            
    def n(self):  # Retorna número de vértices
        return len(self.vertices)

    def m(self):  # Retorna número de arestas
        return len(self.arestas)

    def outneighborhood(self, vertice):  # Vizinhança de saída (lista de vértices que saem de `vertice`)
        return self.listaAdj[vertice]

    def inneighborhood(self, vertice):  # Vizinhança de entrada (lista de vértices que chegam em `vertice`)
        return self.listaIN[vertice] 

    def viz(self, vertice):
        # União das vizinhanças: in ∪ out
        return list(set(self.outneighborhood(vertice) + self.inneighborhood(vertice)))

    def outdegree(self, vertice): # Grau de saída
        return len(self.listaAdj[vertice])

    def indegree(self, vertice): # Grau de entrada
        return len(self.listaIN[vertice])

    def d(self, vertice): # Grau total (in + out)
        return self.indegree(vertice) + self.outdegree(vertice)

    def w(self, origem, destino): # Retorna peso da aresta (origem -> destino)
        if (origem, destino) not in self.arestas:
            raise ValueError(
                f"A aresta ({origem} -> {destino}) não existe no grafo.")

        return self.arestas[(origem, destino)]

    def mind(self): # Menor grau total entre todos os vértices
        return min(self.d(v) for v in self.vertices)

    def maxd(self): # Maior grau total entre todos os vértices
        return max(self.d(v) for v in self.vertices)

    def bfs(self, s):
        """
        BFS:
          - cor: marca status ("Branco" não visitado, "Cinza" descoberto, "Preto" terminado)
          - d: distância (número de arestas) de s até cada vértice
          - pi: predecessor no caminho de s => v
        Retorna duas listas (distâncias e predecessores) na ordem de self.vertices.
        """
        cor = {}
        d = {}
        pi = {}

        # Inicialização
        for v in self.vertices:
            cor[v] = "Branco"
            d[v] = float("inf")
            pi[v] = None

        cor[s] = "Cinza"
        d[s] = 0

        Q = deque()
        Q.append(s)

        # BFS
        while Q:
            u = Q.popleft()

            for v in self.listaAdj.get(u, []):  # N⁺(u)
                if cor[v] == "Branco":
                    cor[v] = "Cinza"
                    d[v] = d[u] + 1
                    pi[v] = u
                    Q.append(v)

            cor[u] = "Preto"

        # Retorna como listas respeitando a ordem dos vértices
        lista_d = [d[v] for v in self.vertices]
        lista_pi = [pi[v] for v in self.vertices]

        return lista_d, lista_pi

    def dfs(self, s=None):
        """
        DFS que marca tempos de entrada e saída (v_ini, v_fim) e predecessores (pi).
        Se s for fornecido, a DFS inicia por s (útil para varreduras iniciadas),
        mas depois garante cobertura completa do grafo (varre todos os vértices).
        Retorna listas [pi], [v_ini], [v_fim] na ordem de self.vertices.
        """
        # INICIA_DFS
        cor = {}
        pi = {}
        v_ini = {}
        v_fim = {}

        for v in self.vertices:
            cor[v] = "Branco"
            pi[v] = None
            v_ini[v] = 0
            v_fim[v] = 0

        tempo = 0

        def _dfs_visit(u):
            nonlocal tempo

            # tempo ← tempo + 1
            tempo += 1
            v_ini[u] = tempo
            cor[u] = "Cinza"

            # Para cada vértice v ∈ N⁺(u)
            for v in self.listaAdj.get(u, []):
                if cor[v] == "Branco":
                    pi[v] = u
                    _dfs_visit(v)

            # tempo ← tempo + 1
            tempo += 1
            v_fim[u] = tempo
            cor[u] = "Preto"

        # Se foi passado um vértice inicial, começa por ele
        if s is not None:
            if s not in self.vertices:
                raise ValueError(f"O vértice '{s}' não está no dígrafo.")
            if cor[s] == "Branco":
                _dfs_visit(s)

        # Depois, garante a varredura completa do grafo
        for v in self.vertices:
            if cor[v] == "Branco":
                _dfs_visit(v)

        # Retorno em listas respeitando a ordem de self.vertices
        lista_pi = [pi[v] for v in self.vertices]
        lista_ini = [v_ini[v] for v in self.vertices]
        lista_fim = [v_fim[v] for v in self.vertices]

        return lista_pi, lista_ini, lista_fim


    def bf(self, s):
        """
        Implementação do algoritmo de Bellman-Ford para caminhos mínimos
        em grafos que podem ter pesos negativos (mas detecta ciclos negativos).
        Parâmetros:
          - s: vértice origem
        Retorna:
          - lista_d: distâncias na ordem de self.vertices
          - lista_pi: predecessores na ordem de self.vertices
          - booleano indicando se há ciclo negativo (True se tiver)
        """  
        # INICIALIZA(D, s)
        d = {}
        pi = {}

        for v in self.vertices:
            d[v] = float("inf")
            pi[v] = None

        d[s] = 0

        # Para i ← 1 até n − 1
        for _ in range(len(self.vertices) - 1):

            # Para cada arco (u, v) ∈ A_D
            for (u, v), peso in self.arestas.items():

                # RELAXA(u, v)
                if d[u] != float("inf") and d[v] > d[u] + peso:
                    d[v] = d[u] + peso
                    pi[v] = u

        # Verificação de ciclo negativo
        for (u, v), peso in self.arestas.items():
            if d[u] != float("inf") and d[v] > d[u] + peso:
                return None, None, True   # Grafo com ciclo negativo

        # Retorna listas respeitando a ordem dos vértices
        lista_d = [d[v] for v in self.vertices]
        lista_pi = [pi[v] for v in self.vertices]

        return lista_d, lista_pi, False

    def djikstra(self, origem):
        """
        Implementação de Dijkstra utilizando heap (fila de prioridade).
        Observações importantes:
          - Verifica se há pesos negativos nas arestas e lança ValueError se houver,
            pois o algoritmo de Dijkstra não é válido com pesos negativos.
          - Usa heapq para manter a próxima relaxação mais promissora.
          - Mantém 'dist' e 'pred' como dicionários e no final retorna listas
            na ordem de self.vertices (consistência com outras funções).
        """
        # Verificar pesos negativos
        for peso in self.arestas.values():
            if peso < 0:
                raise ValueError("Dijkstra não permite pesos negativos")

        # Inicialização
        dist = {v: float('inf') for v in self.vertices}
        pred = {v: None for v in self.vertices}

        dist[origem] = 0
        heap = [(0, origem)]  # (distância, vértice)

        while heap:
            dist_u, u = heapq.heappop(heap)

            # Ignora se for uma entrada desatualizada
            if dist_u > dist[u]:
                continue

            # Explora vizinhos de saída
            for v in self.listaAdj[u]:

                peso = self.arestas[(u, v)]
                nova_dist = dist[u] + peso

                if nova_dist < dist[v]:
                    dist[v] = nova_dist
                    pred[v] = u
                    heapq.heappush(heap, (nova_dist, v))

        # Convertendo para listas na ordem de self.vertices (mantendo consistência)
        lista_d = [dist[v] for v in self.vertices]
        lista_pi = [pred[v] for v in self.vertices]

        return lista_d, lista_pi
    
    def coloracao_propria(self):
        """
        Implementa uma heurística gulosa simples para coloração de vértices:
          - Para cada vértice (na ordem de inserção), escolhe a menor cor inteira positiva
            que não esteja sendo usada por nenhum vizinho de saída (listaAdj).
        Retorna:
          - dicionário c: vértice -> cor (int)
          - k: número de cores usadas (valor máximo em c)
        """
        c = {v: 0 for v in self.vertices}  # cores por vértice

        for vertice in self.vertices:
            cores_usadas = set()

            for vizinho in self.listaAdj.get(vertice, []):
                if c[vizinho] != 0:
                    cores_usadas.add(c[vizinho])

            cor = 1
            while cor in cores_usadas:
                cor += 1

            c[vertice] = cor

        k = max(c.values())

        return c, k
    
    # Encontra um caminho com pelo menos 10 arestas (11 vértices) usando BFS
    def encontrar_caminho_10_arestas(self):
        """
        Objetivo: encontrar e retornar um caminho com exatamente (ou pelo menos) 10 arestas
                 (o código retorna os primeiros 11 vértices do caminho quando encontra).
        Estratégia:
          - Para cada vértice 'origem' em self.vertices:
              1. Executa BFS a partir de 'origem' (usa self.bfs)
              2. Mapeia resultados de volta para dicionários (distâncias e predecesores)
              3. Procura um destino cuja distância d >= 10 e reconstruir o caminho via pi
              4. Se o caminho reconstruído tiver 11 ou mais vértices, retorna os 11 primeiros
          - Se não encontrar nenhum caminho que satisfaça, retorna None
        """
        for origem in self.vertices:

            # CHAMADA DIRETA DO BFS
            lista_d, lista_pi = self.bfs(origem)

            # Mapeia as listas de volta para o vértice correspondente
            d = dict(zip(self.vertices, lista_d))
            pi = dict(zip(self.vertices, lista_pi))

            # Procura um vértice com pelo menos 10 arestas de distância
            for destino in self.vertices:
                if d[destino] >= 10 and d[destino] != float("inf"):

                    # Reconstrói o caminho usando pi (do BFS)
                    caminho = []
                    atual = destino
                    while atual is not None:
                        caminho.append(atual)
                        atual = pi[atual]

                    caminho.reverse()

                    # Garante exatamente 10 arestas => 11 vértices
                    if len(caminho) >= 11:
                        return caminho[:11]

        return None



    # DFS auxiliar para detectar ciclo com no mínimo 5 arestas
    def dfs_ciclo(self, v, visitados, pilha, caminho):
        """
        DFS auxiliar usado para detectar ciclos dirigidos.
        Parâmetros:
          - v: vértice atual
          - visitados: conjunto de nós já completamente visitados (marcados)
          - pilha: conjunto representando a pilha de recursão atual (nós na rota ativa)
          - caminho: lista dos vértices na rota de recursão (ordem de entrada)
        Lógica:
          - Marca v como visitado (adicionado a 'visitados' e 'pilha' e appended em 'caminho')
          - Para cada vizinho u de v:
              - Se u estiver na pilha, encontramos um ciclo. Recuperamos a sublista de 'caminho'
                a partir do índice de 'u' para o final -> esse é o ciclo detectado.
              - Se ciclo tem comprimento >= 6 vértices (ou seja, >= 5 arestas), retorna ciclo.
              - Caso contrário, se u não for visitado, recursivamente tenta encontrar ciclo a partir de u.
          - Ao sair do nó, remove-o da pilha e do caminho.
        Retorna:
          - ciclo (lista de vértices) se encontrado; caso contrário, None.
        """
        visitados.add(v)
        pilha.add(v)
        caminho.append(v)

        for u in self.listaAdj.get(v, []):
            if u in pilha:
                idx = caminho.index(u)
                ciclo = caminho[idx:]

                # 5 arestas = 6 vértices
                if len(ciclo) >= 6:
                    return ciclo

            elif u not in visitados:
                resultado = self.dfs_ciclo(u, visitados, pilha, caminho)
                if resultado:
                    return resultado

        pilha.remove(v)
        caminho.pop()
        return None


    # Função principal para encontrar um ciclo com pelo menos 5 arestas
    def encontrar_ciclo_com_5_arestas(self):
        """
        Percorre todos os vértices e usa dfs_ciclo para detectar um ciclo dirigido
        com comprimento mínimo de 6 vértices (5 arestas). Retorna o primeiro ciclo
        encontrado ou None caso não exista.
        """

        visitados = set()

        for v in self.vertices:
            if v not in visitados:
                ciclo = self.dfs_ciclo(v, visitados, set(), [])
                if ciclo:
                    return ciclo

        return None


    # Retorna o vértice mais distante (via Dijkstra)
    def vertice_mais_distante(self, origem=129):
        """
        Utiliza Dijkstra para obter distâncias a partir de 'origem' e retorna
        o par (vértice, distância) correspondente ao vértice alcançável com a
        maior distância finita.
        Observações:
          - Se todos os vértices forem inalcançáveis (dist = inf), retorna None.
          - Por padrão, origem = 129 (mas pode ser passado qualquer vértice existente).
        """
        d, _ = self.djikstra(origem)

        dist = dict(zip(self.vertices, d))
        dist_validos = {v: d for v, d in dist.items() if d < float("inf")}

        if not dist_validos:
            return None

        return max(dist_validos.items(), key=lambda item: item[1])

    def carregar_arquivo(self, caminho):
        """
        Lê um arquivo texto com linhas que começam com "a" indicando arestas.
        Exemplo de linha esperada: "a 1 2 10" (aresta 1->2 com peso 10).
        Observações e garantias:
          - Faz parse simples; está assumindo o formato correto do arquivo.
          - Converte x, y, p em inteiros antes de adicionar ao grafo.
        """
        with open(caminho, 'r') as f:
            for linha in f:
                if linha.startswith("a"):
                    _, x, y, p = linha.strip().split()
                    self.add_aresta(int(x), int(y), int(p))
        return self
    
    