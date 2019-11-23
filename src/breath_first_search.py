from collections import defaultdict


class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source code as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it

            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeud vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


def main():
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    graph.BFS(2)


if __name__ == "__main__":
    main()
