from Graphs import graph


time = 0


def main():
    G = initialize()
    vertexSet = G.getVertices()



def initialize():
    G = graph.Graph()
    with open('input.txt', 'r') as file:
        for line in file:
            edge = line.strip().split(",")
            G.addEdge(edge[0], edge[1])
    return G


def dfs(G):

    for key in G._vertexSet:
        vertex = G._vertexSet[key]

        if vertex.color == "white":
            dfs_explore(G, G._vertexSet[key])


def dfs_explore(G,v):

    v["discoveryTime"] = time
    time += 1

    for vertex in G.getVertexNeighbours():





if __name__ == "__main__":
    main()
