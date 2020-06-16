from Graphs import graph
from queue import Queue


def main():
    G = initialize()
    vertexSet = G.getVertices()
    source = input("Enter the source vertex: ")
    destination = input("Enter the destination vertex: ")


    if (source not in vertexSet):
        print("Source not present in the graph")
        exit(0)

    if (destination not in vertexSet):
        print("Destination not present in the graph")
        exit(0)

    bfs(G, source, destination)


def initialize():
    G = graph.Graph()
    with open('input.txt', 'r') as file:
        for line in file:
            edge = line.strip().split(",")
            G.addEdge(edge[0],edge[1])
    return G


def getPath(u,source):
    list = []
    while not u.name == source.name:
        list.append(u.name)
        u = u.parent
    list.append(source.name)
    list.reverse()
    result = " "
    print(result.join(list))


def bfs(G, source, destination):
    Q = Queue()
    source_vertex = G._vertexSet[source]
    Q.put(source_vertex)

    while not Q.empty():
        u = Q.get()
        if u.name == destination:
            getPath(u,source_vertex)
            break

        for v in G.getVertexNeighbours(u):
            vertex = G._vertexSet[v]
            if(vertex.color == "white"):
                vertex.color = "grey"
                vertex.distance = u.distance + 1
                vertex.parent = u
                Q.put(vertex)

        u.color = "black"


if __name__ == "__main__":
    main()