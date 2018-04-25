
"""
01 function alphabeta(node, depth, α, β, maximizingPlayer)
02      if depth = 0 or node is a terminal node
03          return the heuristic value of node
04      if maximizingPlayer
05          v := -∞
06          for each child of node
07              v := max(v, alphabeta(child, depth – 1, α, β, FALSE))
08              α := max(α, v)
09              if β ≤ α
10                  break (* β cut-off *)
11          return v
12      else
13          v := +∞
14          for each child of node
15              v := min(v, alphabeta(child, depth – 1, α, β, TRUE))
16              β := min(β, v)
17              if β ≤ α
18                  break (* α cut-off *)
19          return v
"""
#pseudocode from wikipedia


def alpha_beta(state):
    infinity = float("inf")

    def alpha_beta_descision(state, depth, alpha, beta, maximizing_player=True):


        if depth == 0 or is_terminal(state):
            return utility_of(state)
        v = -infinity
        if maximizing_player:
            for state in successors_of(state):
                v = max(v, alpha_beta_descision(state, depth - 1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    print("Cut off beta")
                return v
        else:
            v = infinity
            for state in successors_of(state):
                v = min(v, alpha_beta_descision(state, depth - 1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    print("Cut off alpha")
                return v


    new_state = argmax(successors_of(state), lambda a: alpha_beta_descision(state, 1000, -infinity, infinity, True))
    return new_state


"""
def minmax_decision(state, depth=0, alpha=0, beta=0):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for state in successors_of(state):
            v = max(v, minmax_decision(state, depth-1, alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                print("max")

        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for state in successors_of(state):
            v = min(v, minmax_decision(state, depth-1,alpha,beta))
            beta = min(beta, v)
            if beta <= alpha:
               print("min")

        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state
"""

def is_terminal(state):

    for pile in state:
        if pile >= 3:
            return False
    return True



def utility_of(state):
    if len(state) % 2 == 0:
        return -1
    else:
        return 1


def successors_of(state):


    return_states = []

    for pile in state:
        if pile >= 3:
            index = 0
            if pile %2 == 0:
                index = int(pile / 2)
            else:
                index = int(pile/2 + 1)

            for j in range(1, index):
                new_state = state[:]
                new_state.remove(pile)
                new_state.append(j)
                new_state.append(pile-j)
                return_states.append(new_state)


    return return_states


def display(state):
    print(state)


def main():
    state = [15]
    while not is_terminal(state):
        state = alpha_beta(state)
        if not is_terminal(state):
            display(state)
            pile_to_split = int(input("which pile do you want to split(index)?"))
            pile = state[pile_to_split]
            pile_one = int(input("What size should the first pile be?"))
            pile_two = pile -  pile_one

            state.remove(pile)
            state.append(pile_one)
            state.append(pile_two)
            display(state)




def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
