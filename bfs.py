from .. problem import Problem
from .. datastructures.queue import Queue


# please ignore this
def get_solver_mapping():
    return dict(bfs=BFS)


class BFS(object):
    # TODO, exercise 1:

    # - implement Breadth First Search (BFS)
    # - use 'problem.get_start_node()' to get the node with the start state
    # - use 'problem.is_end(node)' to check whether 'node' is the node with the end state
    # - use a set() to store already visited nodes
    # - use the 'queue' datastructure that is already imported as the 'fringe'/ the 'frontier'
    # - use 'problem.successors(node)' to get a list of nodes containing successor states
    def solve(self, problem: Problem):
        queue = Queue()
        visited = set()
        start_node = problem.get_start_node()
        visited.add(start_node)
        queue.put(start_node)
        while queue.has_elements():
            current_node = queue.get()
            if current_node not in visited:
                visited.add(current_node)
            for node in problem.successors(current_node):
                if node not in visited:
                    visited.add(node)
                    queue.put(node)
                if problem.is_end(node):
                    return node                  
        return None
