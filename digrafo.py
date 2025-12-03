from collections import deque

class Grafo:
    def __init__(self, ponderado=False): # Possui a lista de vétices, se ele é ponderado ou não, a lista de arestas e a lista com as adjacências de cada vértice
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

    def n(self):# Retorna número de vértices
        return len(self.vertices)
    
    def m(self):# Retorna número de arestas
        return len(self.arestas)        
    
    def viz(self, vertice):# Retorna os vizinhos de um vértice
        if vertice not in self.vertices:
            return "Esse vértice não está no grafo"
        
        return self.listaAdj.get(vertice)
    
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