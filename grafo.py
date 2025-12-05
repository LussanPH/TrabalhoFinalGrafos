from collections import deque
from funcoesAuxiliares import dfs_visita

class Grafo:
    def __init__(self, ponderado=False): # Possui a lista de vétices, se ele é ponderado ou não, a lista de arestas e a lista com as adjacências de cada vértice
        self.vertices = []
        self.ponderado = ponderado
        self.arestas = {}
        self.listaAdj = {}

    
    def add(self, origemDestinoPeso): # A função recebe uma lista com três índices [origem, destino, peso] se for ponderado, caso contrário só 2 índices [origem, destino]
        if not self.ponderado: # Caso não seja ponderado, adiciona valor unitário para a aresta
            origemDestinoPeso.append(1)

        if origemDestinoPeso[0] not in self.vertices:# Adiciona a origem ao self.vertices
            self.vertices.append(origemDestinoPeso[0]) 

        if origemDestinoPeso[1] not in self.vertices:# Adiciona o destino ao self.vertices
            self.vertices.append(origemDestinoPeso[1])

        if tuple(origemDestinoPeso[:2]) not in self.arestas:# Adiciona a aresta com seu peso ao self.arestas
            self.arestas[tuple(origemDestinoPeso[:2])] = origemDestinoPeso[2]

        aresta = origemDestinoPeso[:2]
        aresta.reverse()

        if tuple(aresta) not in self.arestas:# Adiciona a aresta "invertida" ao self.arestas
            self.arestas[tuple(aresta)] = origemDestinoPeso[2]

        if origemDestinoPeso[0] not in self.listaAdj:# Adiciona a origem à lista de adjacências
            self.listaAdj[origemDestinoPeso[0]] = []

        if origemDestinoPeso[1] not in self.listaAdj:# Adiciona o destino à lista de adjacências
            self.listaAdj[origemDestinoPeso[1]] = []

        if origemDestinoPeso[1] not in self.listaAdj[origemDestinoPeso[0]]:# Adiciona a incidência do destino na origem
            self.listaAdj[origemDestinoPeso[0]].append(origemDestinoPeso[1])

        if origemDestinoPeso[0] not in self.listaAdj[origemDestinoPeso[1]]:# Adiciona a incidência da origem no destino
            self.listaAdj[origemDestinoPeso[1]].append(origemDestinoPeso[0])


    def n(self):# Retorna número de vértices
        return len(self.vertices)
    
    
    def m(self):# Retorna número de arestas
        return len(self.arestas)
    
    
    def viz(self, vertice):# Retorna os vizinhos de um vértice
        if vertice not in self.vertices:
            return "Esse vértice não está no grafo"
        
        return self.listaAdj.get(vertice)
    
    
    def d(self, vertice):# Retorna o grau de um vértices
        if vertice not in self.vertices:
            return "Esse vértice não está no grafo"
        
        return len(self.listaAdj.get(vertice)) # type: ignore
    
    
    def w(self, origemDestino):
        origem = origemDestino // 10
        destino = origemDestino % 10
        origemDestino = [origem, destino]
        return self.arestas[tuple(origemDestino)] 
     

    def mind(self):
        first = True
        for v in self.listaAdj.values():
            if first:
                count = len(v)
                first = False
            elif len(v) < count:
                count = len(v)
        return count
    
    
    def maxd(self):
        count = 0
        for v in self.listaAdj.values():
            if len(v) > count:
                count = len(v)
        return count
    

    def bfs(self, v):
        if v not in self.vertices:
            raise ValueError(f"O vértice '{v}' não está no grafo.")

        vertices = {}

        for vertice in self.vertices:
            if vertice != v:
                vertices[vertice] = ['branco', float('inf'), None] # cor, camada do vértice, vértice predecessor

        vertices[v] = ['cinza', 0, None]

        fila = deque()
        fila.append(v)

        while fila:
            primeiro = fila.popleft()

            for vertice in self.listaAdj.get(primeiro, []):
                if vertices[vertice][0] == 'branco':
                    vertices[vertice][0] = 'cinza'
                    vertices[vertice][1] = vertices[primeiro][1] + 1
                    vertices[vertice][2] = primeiro
                    fila.append(vertice)

            vertices[primeiro][0] = 'preto'

        d = [vertices[vertice][1] for vertice in self.vertices]
        pi = [vertices[vertice][2] for vertice in self.vertices]

        return d, pi
    

    def dfs(self, v):
        if v not in self.vertices:
            raise ValueError(f"O vértice '{v}' não está no grafo.")

        vertices = {}

        for vertice in self.vertices:
            vertices[vertice] = ['branco', None, 0, 0]# cor, vértice predecessor, tempo de início da visita, tempo de fim da visita
        
        tempo = 0
        
        for vertice in self.vertices:
            if vertices[vertice][0] == 'branco':
                dfs_visita(vertices, vertice, self.listaAdj, tempo)

        pi = [vertices[vertice][1] for vertice in self.vertices]
        ini = [vertices[vertice][2] for vertice in self.vertices]
        fim = [vertices[vertice][3] for vertice in self.vertices]

        return pi, ini, fim

    def djikstra(self, v):
        if v not in self.vertices:
            raise ValueError(f"O vértice '{v}' não está no grafo.")

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


    def bf(self, v):
        if v not in self.vertices:
            raise ValueError(f"O vértice '{v}' não está no grafo.")
        
        vertices = {}

        for vertice in self.vertices:
            vertices[vertice] = [None, float('inf')]

        vertices[v] = [None, 0]

        for _ in range(len(self.vertices) - 1):

            for aresta in self.arestas:
                if vertices[aresta[0]][1] + self.arestas[aresta] < vertices[aresta[1]][1]:
                    vertices[aresta[1]][0] = aresta[0]
                    vertices[aresta[1]][1] = vertices[aresta[0]][1] + self.arestas[aresta]

        for aresta in self.arestas:
            if vertices[aresta[0]][1] + self.arestas[aresta] < vertices[aresta[1]][1]:

                return "Existe ciclo negativo"
            
        d = [vertices[vertice][1] for vertice in self.vertices]
        pi = [vertices[vertice][0] for vertice in self.vertices]

        return d, pi
                    
        



