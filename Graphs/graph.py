# Adjacency Map implementation of Graph


class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.color = "white"
        self.parent = None
        self.adj_vertices = {}


class Graph:

    def __init__(self):
        self._vertexSet = {}

    def addVertex(self, name):
        self._vertexSet[name] = Vertex(name)

    def addEdge(self, u, v, weight=0):

        if u in self._vertexSet:
            vertex_u = self._vertexSet[u]
            vertex_u.adj_vertices[v] = weight
        else:
            self.addVertex(u)
            self._vertexSet[u].adj_vertices[v] = weight

    def getVertexNeighbours(self, u):
        list = []
        for key in u.adj_vertices:
            list.append(key)
        return list

    def getVertices(self):
        list = []
        for key in self._vertexSet:
            list.append(key)
        return list