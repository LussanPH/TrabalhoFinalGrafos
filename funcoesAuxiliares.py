def dfs_visita(vertices, vertice, listaAdj, tempo):
    tempo += 1
    vertices[vertice][0] = 'cinza'#Marca o vértice com o tempo de visita
    vertices[vertice][2] = tempo

    for v in listaAdj[vertice]:#Recursão em profundidade
        if vertices[v][0] == 'branco':
            vertices[v][1] = vertice
            tempo = dfs_visita(vertices, v, listaAdj, tempo)

    vertices[vertice][0] = 'preto'#Marca o vértice com o tempo final
    tempo += 1
    vertices[vertice][3] = tempo
    return tempo
