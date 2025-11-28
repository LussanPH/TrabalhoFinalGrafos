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

        if origemDestinoPeso[0] not in self.listaAdj:# Adiciona a origem à lista de adjacências
            self.listaAdj[origemDestinoPeso[0]] = []

        if origemDestinoPeso[1] not in self.listaAdj:# Adiciona o destino à lista de adjacências
            self.listaAdj[origemDestinoPeso[1]] = []

        if origemDestinoPeso[1] not in self.listaAdj[origemDestinoPeso[0]]:# Adiciona a incidência do destino na origem
            self.listaAdj[origemDestinoPeso[0]].append(origemDestinoPeso[1])

        if origemDestinoPeso[0] not in self.listaAdj[origemDestinoPeso[1]]:# Adiciona a incidência da origem no destino
            self.listaAdj[origemDestinoPeso[1]].append(origemDestinoPeso[0])

    def get_n(self):# Retorna número de vértices
        return len(self.vertices)
    
    def get_m(self):# Retorna número de arestas
        return len(self.arestas)
    
    def get_viz(self, vertice):# Retorna os vizinhos de um vértice
        if vertice not in self.vertices:
            return "Esse vértice não está no grafo"
        
        return self.listaAdj.get(vertice)
    
    def get_grau(self, vertice):# Retorna o grau de um vértices
        if vertice not in self.vertices:
            return "Esse vértice não está no grafo"
        
        return len(self.listaAdj.get(vertice))
        
    
