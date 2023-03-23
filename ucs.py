from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


def get_solver_mapping():
    return dict(ucs=UCS)


class UCS(object):

    # - implement Uniform Cost Search (UCS), a variant of Dijkstra's Graph Search
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - store visited nodes in a 'set()'

    def solve(self, problem: Problem):
        visited = set()
        pq = PriorityQueue()
        
        root_node = problem.get_start_node()
        pq.put(root_node.cost,root_node)
        while pq.has_elements():
            current_node = pq.get()
            if current_node not in visited:
                visited.add(current_node)
            for node in problem.successors(current_node):
                if node not in visited:
                    visited.add(node)
                    pq.put(node.cost,node)
                if problem.is_end(node):
                    return node

        return None
