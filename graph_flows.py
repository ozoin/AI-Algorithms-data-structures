class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for cell in row] for row in
                                       graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for cell in row] for row in graph]  # empty graph with same dimension as graph


    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink.
        Update the latest augmenting path, the residual graph and the current flow by the maximum possible amount according to your chosen path.
        The path must be chosen based on BFS.
        """
        queue = list()
        queue.append(source)
        visited = [False for _ in range(len(self.graph))]
        parent = [0 for _ in range(len(self.graph))]
        visited[source] = True
        while queue:
            element = queue.pop(0)
            for curr_el in range(len(self.graph)):
                if not visited[curr_el] and self.residual_graph[element][curr_el] > 0:
                    visited[curr_el] = True
                    queue.append(curr_el)
                    parent[curr_el] = element
        if parent[sink] == 0:
            return 0
        flow = float('inf')
        curr_el = sink
        while curr_el != source:
            element = parent[curr_el]
            flow = min(flow, self.residual_graph[element][curr_el])
            curr_el = element
        curr_el = sink
        while curr_el != source:
            element = parent[curr_el]
            self.residual_graph[element][curr_el] -= flow
            self.residual_graph[curr_el][element] += flow
            self.current_flow[element][curr_el] += flow
            curr_el = element
        self.latest_augmenting_path = [[0 for _ in range(len(self.graph))] for _ in range(len(self.graph))]
        curr_el = sink
        while curr_el != source:
            element = parent[curr_el]
            self.latest_augmenting_path[element][curr_el] = flow
            curr_el = element
        return flow

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        """
        max_flow = 0
        flow = self.ff_step(source, sink)
        while flow:
            max_flow += flow
            flow = self.ff_step(source, sink)
        return max_flow
