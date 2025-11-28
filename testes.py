from grafo import Grafo

G = Grafo(True) 

G.add([0, 1, 2])
G.add([0, 2, 4])
G.add([1, 2, 1])
G.add([1, 3, 7])
G.add([2, 4, 3])
G.add([3, 4, 1])
G.add([4, 0, 5])

print(G.get_n())
print(G.get_m())
print(G.get_viz(0))
print(G.get_grau(0))