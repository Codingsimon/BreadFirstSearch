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
        
        newQueue = Queue()
        visited = set()
        node = problem.get_start_node()
        newQueue.put(node)
        visited.add(node)

        while newQueue.has_elements():

            p = newQueue.get() 
            if problem.is_end(s):
                return p

            for nextN in problem.successors(s):

                if nextN not in visited:
                    visited.add(nextN)
                    newQueue.put(nextN)

        return null
