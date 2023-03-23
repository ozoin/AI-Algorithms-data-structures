from vertex import Vertex
from edge import Edge
import unittest

class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices in the graph
        self.edges = []  # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

    def get_number_of_vertices(self):
        """
        :return: the number of vertices in the graph
        """
        # TODO
        return self.num_vertices

    def get_number_of_edges(self):
        """
        :return: the number of edges in the graph
        """
        # TODO
        return self.num_edges

    def get_vertices(self):
        """
        :return: list of length get_number_of_vertices() with the vertices of the graph
        """
        # TODO
        return self.vertices

    def get_edges(self):
        """
        :return: list of length get_number_of_edges() with the edges of the graph
        """
        # TODO
        return self.edges

    def insert_vertex(self, vertex_name):
        """
        Inserts a new vertex with the given name into the graph.
        Returns None if the graph already contains a vertex with the same name.
        The newly added vertex should store the index at which it has been added.

        :param vertex_name: The name of vertex to be inserted
        :return: The newly added vertex, or None if the vertex was already part of the graph
        :raises: ValueError if vertex_name is None
        """
        if not vertex_name:
            raise ValueError('Vertex name is none')
        if not self.find_vertex(vertex_name):
            vertex_len = self.num_vertices
            new_vertex = Vertex(index=vertex_len ,name=vertex_name)
            self.vertices.insert(vertex_len, new_vertex)
            self.num_vertices += 1
            return new_vertex
        else:
            return None

            
        # TODO

    def find_vertex(self, vertex_name):
        """
        Returns the respective vertex for a given name, or None if no matching vertex is found.
        :param vertex_name: the name of the vertex to find
        :return: the found vertex, or None if no matching vertex has been found.
        :raises: ValueError if vertex_name is None.
        """
        if not vertex_name:
            raise ValueError('Vertex name is none')
        for vertex in self.vertices:
            if vertex.name == vertex_name:
                return vertex
        return None
        # TODO

    def insert_edge_by_vertex_names(self, v1_name, v2_name, weight: int):
        """
        Inserts an edge between two vertices with the names v1_name and v2_name and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).
        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        if v1_name == v2_name or not v1_name or not v2_name:
            raise ValueError("Error insert edges")
        vertex_v1 = self.find_vertex(v1_name)
        vertex_v2 = self.find_vertex(v2_name)
        #FIND EDGE BY VERTEX NAMES
        if vertex_v1 and  vertex_v2 and not self.find_edge_by_vertex_names(v1_name, v2_name):
            new_edge = Edge(first_vertex=vertex_v1, second_vertex=vertex_v2, weight=weight)
            self.edges.append(new_edge)
            self.num_edges += 1
            return new_edge
        else:
            return None
        # TODO

    def insert_edge(self, v1: Vertex, v2: Vertex, weight: int):
        """
        Inserts an edge between two vertices v1 and v2 and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).
        :param v1: vertex 1
        :param v2: vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        # TODO
        if v1==v2 or not v1 or not v2:
            raise ValueError('Error')
        vertex_v1 = self.find_vertex(v1.name)
        vertex_v2 = self.find_vertex(v2.name)
        if vertex_v1 and vertex_v2 and not self.find_edge(v1,v2):
            new_edge = Edge(v1,v2,weight)
            self.edges.append(new_edge)
            self.num_edges += 1
            return new_edge
        else: 
            return None

    def find_edge_by_vertex_names(self, v1_name, v2_name):
        """
        Returns the edge if there is an edge between the vertices with the name v1_name and v2_name, otherwise None.
        In case both names are identical a ValueError shall be raised.
        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1_name equals v2_name or if v1_name or v2_name is None.
        """
        if v1_name == v2_name or not v1_name or not v2_name:
            raise ValueError("None")
        for edge in self.edges:
            if edge.first_vertex.name == v1_name and edge.second_vertex.name == v2_name:
                return edge
        return None
        # TODO

    def find_edge(self, v1: Vertex, v2: Vertex):
        """
        Returns the edge if there is an edge between the vertices v1 and v2, otherwise None.
        In case v1 equals v2 a ValueError shall be raised.
        :param v1: vertex 1
        :param v2: vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1 equals v2 or if v1 or v2 are None.
        """
        if v1==v2 or not v1 or not v2:
            raise ValueError('Error')
        for edge in self.edges:
            if (edge.first_vertex == v1 or edge.second_vertex == v1) and (edge.first_vertex == v2 or edge.second_vertex == v2):
                return edge
        return None
        
        # TODO

    def get_adjacency_matrix(self):
        """
        Returns the NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains the edge weight if there is an edge at the corresponding index position, otherwise -1.
        :return: adjacency matrix
        """
        matrix = []
        for i in range(self.get_number_of_vertices()): 
            row=[]
            for j in range(self.get_number_of_vertices()):
                row.append(-1)
            matrix.append(row)

        for edges in self.edges:
            matrix[edges.second_vertex.idx][edges.first_vertex.idx] = edges.weight
            matrix[edges.first_vertex.idx][edges.second_vertex.idx] = edges.weight
        return matrix


    def get_adjacent_vertices_by_vertex_name(self, vertex_name):
        """
        Returns a list of vertices which are adjacent to the vertex with name vertex_name based on the ordering in which
        they occur in the adjacency matrix.
        :param vertex_name: The name of the vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex with name vertex_name.
        :raises: ValueError if vertex_name is None
        """
        if not vertex_name:
            raise ValueError('Vertex is none')
        vertices = list()
        vertex_idx = self.find_vertex(vertex_name).idx
        for edge in self.get_edges():
            if vertex_idx == edge.first_vertex.idx or vertex_idx == edge.second_vertex.idx:
                vertices.append(self.vertices[edge.second_vertex.idx])
        return vertices

    def get_adjacent_vertices(self, vertex: Vertex):
        """
        Returns a list of vertices which are adjacent to the given vertex based on the ordering in which
        they occur in the adjacency matrix.
        :param vertex: The vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex.
        :raises: ValueError if vertex is None
        """
        if not vertex:
            raise ValueError('Vertex is none')
        vertices = list()
        for edge in self.get_edges():
            if vertex.idx == edge.first_vertex.idx or vertex.idx == edge.second_vertex.idx:
                vertices.append(self.vertices[edge.second_vertex.idx])
        return vertices
        # TODO
    
            
# class TestAssignment04Student(unittest.TestCase):
#         def test_insert_vertex(self):

#             expected_matrix = [
#                 [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [1, -1, -1, -1, -1, 2, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, 5, -1, -1, 6, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, 3, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, 6, -1, -1, 4, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, 7, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, 10, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, 8, 11, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, 13, -1, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, 14, -1],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, 14, -1, 16],
#                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16, -1]
#                 ]
            
            
#             g = Graph()
#             v_linz = g.insert_vertex("Linz")
#             v_stpoelten = g.insert_vertex("St.Poelten")
#             v_wien = g.insert_vertex("Wien")
#             v_innsbruck = g.insert_vertex("Innsbruck")
#             v_bregenz = g.insert_vertex("Bregenz")
#             v_eisenstadt = g.insert_vertex("Eisenstadt")
#             v_graz = g.insert_vertex("Graz")
#             v_klagenfurt = g.insert_vertex("Klagenfurt")
#             v_salzburg = g.insert_vertex("Salzburg")
#             g.insert_edge(v_linz, v_wien, 1)
#             g.insert_edge(v_wien, v_eisenstadt, 2)
#             g.insert_edge(v_wien, v_graz, 3)
#             g.insert_edge(v_graz, v_klagenfurt, 4)
#             g.insert_edge(v_bregenz, v_innsbruck, 5)
#             g.insert_edge(v_klagenfurt, v_innsbruck, 6)
#             g.insert_edge(v_salzburg, v_innsbruck, 7)
#             v_a = g.insert_vertex("A")
#             v_b = g.insert_vertex("B")
#             v_c = g.insert_vertex("C")
#             v_d = g.insert_vertex("D")
#             v_e = g.insert_vertex("E")
#             v_f = g.insert_vertex("F")
#             v_g = g.insert_vertex("G")
#             v_h = g.insert_vertex("H")
#             v_i = g.insert_vertex("I")
#             g.insert_edge(v_salzburg, v_b, 8)
#             g.insert_edge(v_klagenfurt, v_c, 9)
#             g.insert_edge(v_stpoelten, v_a, 10)
#             g.insert_edge(v_b, v_a, 11)
#             g.insert_edge(v_e, v_f, 12)
#             g.insert_edge(v_f, v_g, 13)
#             g.insert_edge(v_g, v_h, 14)
#             g.insert_edge(v_h, v_d, 15)
#             g.insert_edge(v_h, v_i, 16)

#             # #print(g.get_edges())
#             for edge in g.get_edges():
#                 print(f'({edge.first_vertex.idx},{edge.second_vertex.idx},{edge.weight})')
#             # matrix = g.get_adjacency_matrix()
#             # sb = ""
#             # print("\n[test_get_adjacency_matrix]")
#             # for i in range(0, len(matrix)):
#             #     for j in range(0, len(matrix)):
#             #         if matrix[i][j] != expected_matrix[i][j]:
#             #             sb += "\tError @ matrix position: " + str(i) + "," + str(j) + "\n"
#             v0 = g.get_adjacent_vertices(g.vertices[2])
#             print(g.vertices[2].idx)
#             print(v0)
#             self.assertEqual(1, len(v0), "err")

#             v1 = g.get_adjacent_vertices(g.vertices[1])
#             self.assertEqual(1, len(v1), "err")
#             v2 = g.get_adjacent_vertices(g.vertices[2])
#             self.assertEqual(3, len(v2), "err")
# if __name__ == '__main__':
#     unittest.main()
    
