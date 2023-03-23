from graph import Graph
from vertex import Vertex
from step import Step
from edge import Edge


class JKUMap(Graph):

    def __init__(self):
        super().__init__()
        v_spar = self.insert_vertex("Spar")
        v_lit = self.insert_vertex("LIT")
        v_porter = self.insert_vertex("Porter")
        v_openlab = self.insert_vertex("Open Lab")
        v_bank = self.insert_vertex("Bank")
        v_khg = self.insert_vertex("KHG")
        v_parking = self.insert_vertex("Parking")
        v_bellacasa = self.insert_vertex("Bella Casa")
        v_sp1 = self.insert_vertex("SP1")
        v_sp3 = self.insert_vertex("SP3")
        v_lui = self.insert_vertex("LUI")
        v_teichwerk = self.insert_vertex("Teichwerk")
        v_castle = self.insert_vertex("Castle")
        v_papaya = self.insert_vertex("Papaya")
        v_jkh = self.insert_vertex("JKH")
        v_library = self.insert_vertex("Library")
        v_chat = self.insert_vertex("Chat")

        self.insert_edge(v_spar, v_lit, 50)
        self.insert_edge(v_porter, v_lit, 80)
        self.insert_edge(v_porter, v_openlab, 70)
        self.insert_edge(v_bank, v_porter, 100)
        self.insert_edge(v_porter, v_spar, 103)
        self.insert_edge(v_khg, v_spar, 165)
        self.insert_edge(v_parking, v_khg, 190)
        self.insert_edge(v_khg, v_bank, 150)
        self.insert_edge(v_parking, v_bellacasa, 145)
        self.insert_edge(v_sp1, v_parking, 240)
        self.insert_edge(v_sp3, v_sp1, 130)
        self.insert_edge(v_sp1, v_lui, 175)
        self.insert_edge(v_jkh, v_papaya, 80)
        self.insert_edge(v_castle, v_papaya, 85)
        self.insert_edge(v_lui, v_teichwerk, 135)
        self.insert_edge(v_lui, v_library, 90)
        self.insert_edge(v_lui, v_chat, 240)
        self.insert_edge(v_library, v_chat, 160)
        self.insert_edge(v_chat, v_bank, 115)

    def get_steps_for_shortest_paths_from(self, from_vertex: Vertex):
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and number of steps as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.

        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the number of steps as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError("Error")
        distances = {}
        unvisited = list(self.vertices)
        for v in unvisited:
            if v == from_vertex:
                distances[v.name] = 0
            else:
                distances[v.name] = float('inf')

        while unvisited:
            current_vertex = None
            current_distance = float('inf')
            for vertex in unvisited:
                if distances[vertex.name] < current_distance:
                    current_vertex = vertex
                    current_distance = distances[vertex.name]
            if current_vertex is None:
                break
            unvisited.remove(current_vertex)
            for neighbor in self.get_adjacent_vertices(current_vertex):
                if neighbor in unvisited:
                    edge_weight = self.find_edge(current_vertex, neighbor)
                    if edge_weight:
                        new_distance = current_distance+1
                    if new_distance < distances[neighbor.name]:
                        distances[neighbor.name] = new_distance
        distances = {name: dist if dist != float(
            'inf') else -1 for name, dist in distances.items()}
        return distances

    def get_shortest_distances_from(self, from_vertex: Vertex):
        """
        This method determines the shortest paths from a given "from" vertex to all other vertices.
        The shortest distance (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.

        :param from_vertex: Start vertex
        :return
           A dictionary containing the shortest distance (or -1 if no path exists) to each vertex,
           using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.

        """
        if from_vertex is None:
            raise ValueError("Error")
        distances = {}
        unvisited = list(self.vertices)
        for v in unvisited:
            if v == from_vertex:
                distances[v.name] = 0
            else:
                distances[v.name] = float('inf')

        while unvisited:
            current_vertex = None
            current_distance = float('inf')
            for vertex in unvisited:
                if distances[vertex.name] < current_distance:
                    current_vertex = vertex
                    current_distance = distances[vertex.name]

            if current_vertex is None:
                break

            unvisited.remove(current_vertex)
            for neighbor in self.get_adjacent_vertices(current_vertex):
                if neighbor in unvisited:
                    edge_weight = self.find_edge(current_vertex, neighbor)
                    new_distance = current_distance+edge_weight.weight
                    if new_distance < distances[neighbor.name]:
                        distances[neighbor.name] = new_distance
        distances = {name: dist if dist != float(
            'inf') else -1 for name, dist in distances.items()}
        return distances

    def _dijkstra(self, cur: Vertex, visited_list, distances: dict, paths: dict):
        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.

        :param cur: Current vertex being processed
        :param visited_list: List which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """

        # This method is not mandatory, but a recommendation by us

    def get_shortest_path_from_to(self, from_vertex: Vertex, to_vertex: Vertex):
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.
        :param from_vertex: Start vertex
        :param to_vertex: Destination vertex
        :return:
        The path, with all intermediate steps, returned as an list. This list
        sequentially contains each vertex along the shortest path, together with
        the already covered distance (see example on the assignment sheet).
        Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        if from_vertex is None or to_vertex is None or from_vertex == to_vertex:
            raise ValueError("Error")
        distances = {vertex: float("inf") for vertex in self.vertices}
        distances[from_vertex] = 0
        unvisited_vertices = set(self.vertices)
        previous_vertices = {vertex: None for vertex in self.vertices}
        while unvisited_vertices:
            current_vertex = min(unvisited_vertices,
                                 key=lambda vertex: distances[vertex])
            if current_vertex == to_vertex:
                return self.get_path(previous_vertices, from_vertex, to_vertex, distances)
            unvisited_vertices.remove(current_vertex)
            for neighbor in self.get_adjacent_vertices(current_vertex):
                if neighbor == current_vertex:
                    break
                edge_weight = self.find_edge(neighbor, current_vertex)
                new_distance = distances[current_vertex]+edge_weight.weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_vertices[neighbor] = current_vertex
        if to_vertex not in previous_vertices:
            return None
        return None

    def get_path(self, previous_vertices, from_vertex, to_vertex, distances):
        path = []
        current_vertex = to_vertex
        while current_vertex is not None:
            path.insert(0, Step(current_vertex, distances[current_vertex]))
            current_vertex = previous_vertices[current_vertex]
        if len(path) == 1 and path[0].point == to_vertex:
            return None
        return path


# class TestAssignment04Student(unittest.TestCase):
#     def test_existing_shortest_path_from_SP3_to_spar(self):
#         jku_map = JKUMap()
#         # result = jku_map.get_shortest_distances_from(
#         #     jku_map.find_vertex("LUI"))
#         # print(result)

#         result = jku_map.get_steps_for_shortest_paths_from(
#             jku_map.find_vertex("LUI"))
#         print(result)
#         # result = jku_map.get_steps_for_shortest_paths_from(
#         #     jku_map.find_vertex("LUI"))
#         # print(result)


# if __name__ == '__main__':
#     unittest.main()
