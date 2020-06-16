from Graphs import graph
from queue import Queue


def initialize():
    Graph = graph.Graph()
    with open('input.txt', 'r') as file:
        for line in file:
            edge = line.strip().split(",")
            Graph.addEdge(edge[0], edge[1])
    return Graph


def bfs(G, source="1", destination="2"):
    Q = Queue()
    s_vertex = G._vertexSet[source]
    Q.put(s_vertex)

    while not Q.empty():
        u = Q.get()
        for v in G.getVertexNeighbours(u):
            if G._vertexSet[v].color == "white":
                G._vertexSet[v].color = "gray"
                G._vertexSet[v].distance = u.distance + 1
                Q.put(G._vertexSet[v])
        u.color = "black"
        print(u.name)


def main():
    G = initialize()
    bfs(G, source="5")


if __name__ == "__main__":
    main()
