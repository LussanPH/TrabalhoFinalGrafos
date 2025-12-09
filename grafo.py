from collections import deque
from funcoesAuxiliares import dfs_visita
import sys

sys.setrecursionlimit(40000)#Necessário para dfs em um grafo profundo demais

class Grafo:
    def __init__(self, ponderado=False): # Possui a lista de vétices, se ele é ponderado ou não, a lista de arestas e a lista com as adjacências de cada vértice
        self.vertices = set()
        self.ponderado = ponderado
        self.arestas = {}
        self.listaAdj = {}

    
    def add(self, origem, destino, peso): # A função recebe uma lista com três índices [origem, destino, peso] se for ponderado, caso contrário só 2 índices [origem, destino]
        if not self.ponderado: # Caso não seja ponderado, adiciona valor unitário para a aresta
            peso = 1

        if origem not in self.vertices:# Adiciona a origem ao self.vertices
            self.vertices.add(origem) 

        if destino not in self.vertices:# Adiciona o destino ao self.vertices
            self.vertices.add(destino)

        if ((origem, destino) not in self.arestas) and ((destino, origem) not in self.arestas):# Adiciona a aresta com seu peso ao self.arestas
            self.arestas[(origem, destino)] = peso

        if origem not in self.listaAdj:# Adiciona a origem à lista de adjacências
            self.listaAdj[origem] = set()

        if destino not in self.listaAdj:# Adiciona o destino à lista de adjacências
            self.listaAdj[destino] = set()

        if destino not in self.listaAdj[origem]:# Adiciona a incidência do destino na origem
            self.listaAdj[origem].add(destino)

        if origem not in self.listaAdj[destino]:# Adiciona a incidência da origem no destino
            self.listaAdj[destino].add(origem)


    def n(self):# Retorna número de vértices
        return len(self.vertices)
    
    
    def m(self):# Retorna número de arestas
        return len(self.arestas)
    
    
    def viz(self, vertice):# Retorna os vizinhos de um vértice
        return self.listaAdj.get(vertice)
    
    
    def d(self, vertice):# Retorna o grau de um vértices        
        return len(self.listaAdj.get(vertice)) # type: ignore
    
    
    def w(self, origem, destino):
        if self.arestas.get((origem, destino)):
            return self.arestas.get((origem, destino))
        else:
            return self.arestas.get((destino, origem))
     

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
        vertices = {}

        for vertice in self.vertices:
            vertices[vertice] = ['branco', None, 0, 0]# cor, vértice predecessor, tempo de início da visita, tempo de fim da visita
        
        tempo = 0

        dfs_visita(vertices, v, self.listaAdj, tempo)
        
        for vertice in self.vertices:
            if vertices[vertice][0] == 'branco':
                dfs_visita(vertices, vertice, self.listaAdj, tempo)#Recursão para visitar até a camada mais profunda

        pi = [vertices[vertice][1] for vertice in self.vertices]
        ini = [vertices[vertice][2] for vertice in self.vertices]
        fim = [vertices[vertice][3] for vertice in self.vertices]

        return pi, ini, fim

    def djikstra(self, v):
        vertices = {}
        naoVisitados = self.vertices #Vérices à serem visitados

        for vertice in self.vertices:
            if vertice != v:
                vertices[vertice] = [None, float('inf')]# vértice predecessor, peso

        vertices[v] = [None, 0]

        while len(naoVisitados) != 0:
            verticeMinimo = None
            valorMinimo = float("inf")

            for vertice in naoVisitados:#procura o vétice com peso mínimo que não foi visitado
                if vertices[vertice][1] <= valorMinimo:
                    verticeMinimo = vertice
                    valorMinimo = vertices[vertice][1]

            naoVisitados.remove(verticeMinimo)#remove dos vérices a serem visitados
            print(len(naoVisitados))

            for vertice in self.listaAdj[verticeMinimo]:#Faz o relaxamento das aresta para cada vizinho que ainda não tenha sido visitado
                if vertice not in naoVisitados:
                    continue

                if self.arestas.get((verticeMinimo, vertice)):
                    aresta = (verticeMinimo, vertice)
                else:
                    aresta = (vertice, verticeMinimo)

                if vertices[vertice][1] > vertices[verticeMinimo][1] + self.arestas.get(aresta):#Processo de relaxamento da aresta
                    vertices[vertice][0] = verticeMinimo
                    vertices[vertice][1] = vertices[verticeMinimo][1] + self.arestas.get(aresta)

        d = [vertices[vertice][1] for vertice in self.vertices]
        pi = [vertices[vertice][0] for vertice in self.vertices]

        return d, pi


    def bf(self, v):  
        vertices = {}

        for vertice in self.vertices:#Inicialização de cada vértice
            vertices[vertice] = [None, float('inf')]

        vertices[v] = [None, 0]

        for _ in range(len(self.vertices) - 1):#Executa até o número de vértices - 1

            for aresta in self.arestas:#Relaxamento
                if vertices[aresta[0]][1] + self.arestas[aresta] < vertices[aresta[1]][1]:
                    vertices[aresta[1]][0] = aresta[0]
                    vertices[aresta[1]][1] = vertices[aresta[0]][1] + self.arestas[aresta]

        for aresta in self.arestas:#Verificação de ciclo negativo
            if vertices[aresta[0]][1] + self.arestas[aresta] < vertices[aresta[1]][1]:

                return "Existe ciclo negativo"
            
        d = [vertices[vertice][1] for vertice in self.vertices]
        pi = [vertices[vertice][0] for vertice in self.vertices]

        return d, pi
                     
    
    def coloracao_propria(self):
        c = [0 for _ in range(len(self.vertices))] #Cores inicializadas com vazio (0)

        for vertice in self.vertices:
            cores_usadas = []#Verifica as cores utilizadas por cada vizinho do vértice

            for vizinho in self.listaAdj[vertice]:
                if c[vizinho-1] != 0:
                    cores_usadas.append(c[vizinho-1])
            
            cor = 1

            while cor in cores_usadas:#Adiciona uma cor ao vértice dependendo dos seus vizinhos
                cor += 1

            c[vertice-1] = cor
            
        k = max(c)

        return c, k
            




