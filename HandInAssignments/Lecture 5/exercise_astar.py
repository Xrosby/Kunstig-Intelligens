
infinity = float("inf")

class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTIC = state[1]


    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_LOWEST_COST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        print(children)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def FIND_CHEAPEST_CHILD(children):
    if children[0] != None:
        lowest = children[0]

    for i in range(0, len(children)):

        if i <= len(children):
            if children[i].HEURISTIC < lowest.HEURISTIC:
                lowest = children[i]
    return lowest



def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(child)  # create node for each in state list
        s.STATE = child[0]  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors



def INSERT(node, queue):
    queue.append(node)
    return queue

def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue


def REMOVE_LOWEST_COST(queue):

    result = None
    lowest_cost = infinity
    for node in queue:
        print("NODE: ", node)
        if node.STATE[1] + node.HEURISTIC < lowest_cost:
            lowest_cost = node.STATE[1] + node.HEURISTIC
            result = node
    queue.remove(result)

    return result

def successor_fn(state):  # Lookup list of successor states

    print("STATESPACE: ", STATE_SPACE[state])
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']

A = ('A', 6)
B = ('B', 5)
C = ('C', 5)
D = ('D', 2)
F = ('F', 5)
E = ('E', 4)
I = ('I', 2)
G = ('G', 4)
H = ('H', 1)
J = ('J', 1)
K = ('K', 0)
L = ('L', 0)


"""HERE I WANT TO ADD A COST TO GO FROM ONE STATE TO ANOTHER"""
INITIAL_STATE = A
GOAL_STATE = K or L
STATE_SPACE = {A: [(B, 1), (C, 2), (D, 4)],
               B: [(F, 5), (E, 4)],
               C: [(E, 1)],
               D: [(H, 1), (I, 4), (J, 2)],
               E: [(G, 2), (H, 3)],
               F: [(G, 1)],
               G: [(K, 6)],
               H: [(K, 6), (L, 5)],
               I: [(L, 3)],
               J: [],
               L: [],
               K: []}



def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
