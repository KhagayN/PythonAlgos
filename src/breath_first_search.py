from collections import defaultdict


class Graph:
    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of graph
    def breadth_first_search(self, s):

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
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2)")
    graph.breadth_first_search(2)


if __name__ == "__main__":
    main()
