import random


class GraphColoring:

    """
    k-Graph Coloring Problem (k-GCP)
    -----

    k-GCP is to color a graph with k colors such that any pairs of the nodes
    connected by an edge are assigned with different colors. The graph in this
    problem is randomly generated with strong connectivity using specified
    number of nodes and edges. The optimal solution is ensured to color the
    graph without violent.

    Arguments
    -----
    n_node: int
        number of nodes in the graph
    n_edge: int
        number of edges in the graph
    n_color: int
        number of colors for coloring
    """

    def __init__(
        self,
        n_node: int,
        n_edge: int,
        n_color: int = 3
    ):
        self.n_node = n_node
        self.n_edge = n_edge
        self.n_color = n_color

        if self.n_node%self.n_color:
            raise Exception(
                "Error: the number of nodes must be divisible by the number of"\
                    " colors!"
            )

        if self.n_edge < self.n_node:
            raise Exception(
                "Error: the number of edges must be larger than the number of"\
                    " nodes!"
            )

        if self.n_edge > self.n_node*(self.n_node-1)//2:
            raise Exception(
                "Error: the number of edges must be smaller than n(n-1)/2"\
                    " where n is the number of nodes!"
            )

        self.nodes = list(range(self.n_node))
        self.edges = self._get_edges()
        self.colors = list(range(self.n_color))

    def violent(self, coloring):
        """compute the violent point of the given coloring solution"""
        v = 0
        for node1, node2 in self.edges:
            color1, color2 = coloring[node1], coloring[node2]
            if color1 == color2:
                v += 1
        return v

    def _get_edges(self):
        self.edges = self._random_edges()
        while not self._is_connected():
            self.edges = self._random_edges()
        return self.edges

    def _random_edges(self):
        """generate edges randomly"""
        edges_ = []
        while len(edges_) < self.n_edge:
            node1, node2 = random.choices(self.nodes, k=2)
            if node1 > node2:
                node1, node2 = node2, node1
            if node1%self.n_color != node2%self.n_color:
                if (node1, node2) not in edges_:
                    edges_.append((node1, node2))
        return edges_

    def _is_connected(self):
        """depth first search to check the connectivity of the graph"""
        visited = []
        to_visit = [0]
        while len(to_visit) > 0:
            visited, to_visit = self._step(visited, to_visit)
        if len(visited) < self.n_node:
            return False
        elif len(visited) == self.n_node:
            return True
        else:
            raise Exception("Error: wrong traversal of the graph!")

    def _step(self, visited, to_visit):
        node = to_visit.pop()
        visited.append(node)
        for edge in self.edges:
            if node in edge:
                node1, node2 = edge
                if node1 != node:
                    neighbor = node1
                else:
                    neighbor = node2
                if neighbor not in to_visit+visited:
                    to_visit.append(neighbor)
        return visited, to_visit
