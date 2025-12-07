from collections import deque


class Digrafo:
    # Possui a lista de vétices, se ele é ponderado ou não, a lista de arestas e a lista com as adjacências de cada vértice
    def __init__(self, ponderado=False):
        self.vertices = []
        self.ponderado = ponderado
        self.arestas = {}
        self.listaAdj = {}

    def add(self, origemDestinoPeso):
        # Se não for ponderado, define peso 1
        if not self.ponderado:
            origemDestinoPeso.append(1)

        origem, destino, peso = origemDestinoPeso

        # Adiciona os vértices
        if origem not in self.vertices:
            self.vertices.append(origem)

        if destino not in self.vertices:
            self.vertices.append(destino)

        # Adiciona a aresta direcionada (origem -> destino)
        if (origem, destino) not in self.arestas:
            self.arestas[(origem, destino)] = peso

        # Inicializa listas de adjacência
        if origem not in self.listaAdj:
            self.listaAdj[origem] = []

        if destino not in self.listaAdj:
            self.listaAdj[destino] = []

        # Adiciona adjacência (SOMENTE origem -> destino)
        if destino not in self.listaAdj[origem]:
            self.listaAdj[origem].append(destino)

    def n(self):  # Retorna número de vértices
        return len(self.vertices)

    def m(self):  # Retorna número de arestas
        return len(self.arestas)

    def outneighborhood(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        return self.listaAdj.get(vertice, [])

    def inneighborhood(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        entrada = []

        for origem in self.listaAdj:
            if vertice in self.listaAdj[origem]:
                entrada.append(origem)

        return entrada

    def viz(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        # União das vizinhanças: in ∪ out
        return list(set(self.outneighborhood(vertice) + self.inneighborhood(vertice)))

    def outdegree(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        return len(self.listaAdj.get(vertice, []))

    def indegree(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        cont = 0
        for origem in self.listaAdj:
            if vertice in self.listaAdj[origem]:
                cont += 1

        return cont

    def d(self, vertice):
        if vertice not in self.vertices:
            raise ValueError(f"O vértice '{vertice}' não está no dígrafo.")

        return self.indegree(vertice) + self.outdegree(vertice)

    def w(self, origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            raise ValueError("Um ou ambos os vértices não estão no grafo.")

        if (origem, destino) not in self.arestas:
            raise ValueError(
                f"A aresta ({origem} -> {destino}) não existe no grafo.")

        return self.arestas[(origem, destino)]

    def mind(self):
        if not self.vertices:
            raise ValueError("O grafo não possui vértices.")

        menor = self.d(self.vertices[0])

        for v in self.vertices[1:]:
            deg = self.d(v)
            if deg < menor:
                menor = deg

        return menor

    def maxd(self):
        if not self.vertices:
            raise ValueError("O grafo não possui vértices.")

        maior = self.d(self.vertices[0])

        for v in self.vertices[1:]:
            deg = self.d(v)
            if deg > maior:
                maior = deg

        return maior

    def bfs(self, s):
        if s not in self.vertices:
            raise ValueError(f"O vértice '{s}' não está no dígrafo.")

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
        if s not in self.vertices:
            raise ValueError(f"O vértice '{s}' não está no dígrafo.")

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

    def djikstra(self, v):
        if v not in self.vertices:
            raise ValueError(f"O vértice '{v}' não está no grafo.")
         # Verifica pesos negativos
        for (_, _), peso in self.arestas.items():
            if peso < 0:
                raise ValueError("Dijkstra não permite pesos negativos")

        vertices = {}
        naoVisitados = [] #Vérices à serem visitados

        for vertice in self.vertices:
            naoVisitados.append(vertice)
            if vertice != v:
                vertices[vertice] = [None, float('inf')]# vértice predecessor, peso

        vertices[v] = [None, 0]

        while len(naoVisitados) != 0:
            verticeMinimo = naoVisitados[0]
            valorMinimo = vertices[verticeMinimo][1]

            for vertice in naoVisitados:#procura o vétice com peso mínimo que não foi visitado
                if vertices[vertice][1] <= valorMinimo:
                    verticeMinimo = vertice
                    valorMinimo = vertices[vertice][1]

            naoVisitados.remove(verticeMinimo)#remove dos vérices a serem visitados

            for vertice in self.listaAdj[verticeMinimo]:#Faz o relaxamento das aresta para cada vizinho que ainda não tenha sido visitado
                if vertice not in naoVisitados:
                    continue

                aresta = [verticeMinimo, vertice]
                if vertices[vertice][1] > vertices[verticeMinimo][1] + self.arestas[tuple(aresta)]:#Processo de relaxamento da aresta
                    vertices[vertice][0] = verticeMinimo
                    vertices[vertice][1] = vertices[verticeMinimo][1] + self.arestas[tuple(aresta)]

        d = [vertices[vertice][1] for vertice in self.vertices]
        pi = [vertices[vertice][0] for vertice in self.vertices]

        return d, pi
    
    def coloracao_propria(self):
        if not self.vertices:
            return [], 0

        cor = {v: 0 for v in self.vertices}

        for vertice in self.vertices:

            cores_usadas = set()

            for vizinho in self.viz(vertice):  # entrada + saída
                if cor[vizinho] != 0:
                    cores_usadas.add(cor[vizinho])

            nova_cor = 1
            while nova_cor in cores_usadas:
                nova_cor += 1

            cor[vertice] = nova_cor

        c = [cor[v] for v in self.vertices]
        k = max(c)

        return c, k
    
        # Encontra um caminho com pelo menos 10 arestas (11 vértices) usando BFS
    def encontrar_caminho_10_arestas(self):
        for origem in self.vertices:
            d, pi = self.bfs(origem)

            dist = dict(zip(self.vertices, d))
            pred = dict(zip(self.vertices, pi))

            destino = max(dist, key=dist.get)

            if dist[destino] >= 10:
                caminho = []
                atual = destino

                while atual is not None:
                    caminho.append(atual)
                    atual = pred[atual]

                caminho.reverse()
                return caminho[:11]

        return None


    # DFS auxiliar para detectar ciclo com no mínimo 5 arestas
    def dfs_ciclo(self, v, visitados, pilha, caminho):
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
        visitados = set()

        for v in self.vertices:
            if v not in visitados:
                ciclo = self.dfs_ciclo(v, visitados, set(), [])
                if ciclo:
                    return ciclo

        return None


    # Retorna o vértice mais distante (via Dijkstra)
    def vertice_mais_distante(self, origem=129):
        d, _ = self.djikstra(origem)

        dist = dict(zip(self.vertices, d))
        dist_validos = {v: d for v, d in dist.items() if d < float("inf")}

        if not dist_validos:
            return None

        return max(dist_validos.items(), key=lambda item: item[1])

    def carregar_arquivo(self, caminho):
        with open(caminho, 'r') as f:
            for linha in f:
                if linha.startswith("a"):
                    _, x, y, p = linha.strip().split()
                    self.add([int(x), int(y), int(p)])
        return self
    
    