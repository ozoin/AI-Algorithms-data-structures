import math
from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


# please ignore this
def get_solver_mapping():
    return dict(
        gbfs_ec=GBFS_Euclidean,
        gbfs_mh=GBFS_Manhattan
    )


class GBFS(object):
    # TODO, Exercise 2:
    # - implement Greedy Best First Search (GBFS)
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - use a 'set()' to store nodes that were already visited
    def solve(self, problem: Problem):
        visited = set()
        pq = PriorityQueue()
        root_node = problem.get_start_node()
        goal = problem.get_end_node()
        pq.put(self.heuristic(root_node,goal), root_node)
        visited.add(root_node)
        while pq.has_elements():
            current_node = pq.get()
            if current_node not in visited:
                visited.add(current_node)
            if problem.is_end(current_node):
                return current_node
            for node in problem.successors(current_node):
                if node not in visited:
                    pq.put(self.heuristic(node,goal),node)

# this is the GBFS variant with the euclidean distance as a heuristic
# it is registered as a solver with the name 'gbfs_ec'

# please note that in an ideal world, this heuristic should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state
class GBFS_Euclidean(GBFS):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.sqrt((cy - gy) ** 2 + (cx - gx) ** 2)


# this is the GBFS variant with the manhattan distance as a heuristic
# it is registered as a solver with the name 'gbfs_mh'

# please note that in an ideal world, this heuristic should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state
class GBFS_Manhattan(GBFS):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.fabs((cy - gy)) + math.fabs(cx - gx)
