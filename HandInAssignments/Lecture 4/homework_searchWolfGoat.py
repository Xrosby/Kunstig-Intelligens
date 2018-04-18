class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

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
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.insert(0, node)
    return queue

'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue


#Remove first element from fringe
def REMOVE_FIRST(queue):
    node = queue.pop()
    return node;


'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    list = STATE_SPACE[state];

    for element in list:
        if (element == EWWE):
            list.remove(element)
        if (element == EEWW):
            list.remove(element)
        if (element == WWEE):
            list.remove(element)
        if (element == WEEW):
            list.remove(element)
        if (element == EWWW):
            list.remove(element)
        if (element == WEEE):
            list.remove(element)
    return list  # successor_fn( 'C' ) returns ['F', 'G']



E = 'East'
W = 'West'



#All possible states
WWWW = (W, W, W, W)
WWWE = (W, W, W, E)
WWEE = (W, W, E, E)
WEEE = (W, E, E, E)
EEEE = (E, E, E, E)
EEEW = (E, E, E, W)
EEWW = (E, E, W, W)
EWWW = (E, W, W, W)
EWEW = (E, W, E, W)
WEWE = (W, E, W, E)
WWEW = (W, W, E, W)
WEWW = (W, E, W, W)
EEWE = (E, E, W, E)
EWEE = (E, W, E ,E)
EWWE = (E, W, W, E)
WEEW = (W, E, E, W)


INITIAL_STATE = WWWW
GOAL_STATE = EEEE

STATE_SPACE = {
    WWWW:
        [EEWW, EWEW, EWWE],
    WWWE:
        [EEWE, EWEE, EEWE],
    WWEE:
        [EEEE, EWEE],
    WEEE:
        [EEEE],
    EEEE:
        [WWEE, WEWE, EWEW],
    EEEW:
        [WEEW, WWEW, EEWW],
    EEWW:
        [WWWW, WWEW, EEEW],
    EWWW:
        [WWWW],
    WEWE:
        [EEEE, EEWE],
    EWEW:
        [WWWW, WWEW],
    EWWE:
        [WWWW, WWWE],
    EWEE:
        [WWEE, WWEW, WWWE],
    EEWE:
        [WEWE, WWWE],
    WWEW:
        [EWEW, EEEW, EWEE],
    WEWW:
        [EEWW, EEEW, EEWE],
    WEEW:
        [EEEE, EEEW]

}



def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in reversed(path):
        node.display()


if __name__ == '__main__':
    run()
