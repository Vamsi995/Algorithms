from Graphs import graph
from queue import Queue

def initialize():
    G = graph.Graph()

    with open('input.txt', 'r') as file:
        for line in file:
            edge = line.strip().split(",")
            G.addEdge(edge[0], edge[1])

    return G

def bfs(G, source, destination):
    Q = Queue()
    Q.put(G._vertexSet[source])

    while not Q.empty():
        u = Q.get()
        if u.name == destination:
            print(u.distance)
            break

        for v in G.getVertexNeighbours(u):
            vertex = G._vertexSet[v]
            if vertex.color == "white":
                vertex.color = "grey"
                vertex.distance = u.distance + 1;
                Q.put(vertex)



def main():
    source = input("Enter the source vertex: ")
    destination = input("Enter the destination vertex: ")
    G = initialize()
    bfs(G, source, destination)

if __name__ == "__main__":
    main()
