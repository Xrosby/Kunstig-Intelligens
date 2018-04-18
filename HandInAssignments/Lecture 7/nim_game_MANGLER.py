def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action



def is_terminal(state):

    
    pass





def utility_of(state):
    if len(state) % 2 == 0:
        return 0
    else:
        return 1


def successors_of(state):
    list_of_successor_states = []
    return_states = []

    for pile in state:
        if pile >= 3:
            i = 0
            if pile %2 == 0:
                i = (pile / 2)
            else:
                i = round(pile/2)
        for j in range (1, i):

            list_of_successor_states = state[:]
            list_of_successor_states.remove(pile)
            list_of_successor_states.append(j)
            list_of_successor_states.append(pile-j)
            return_states.append(list_of_successor_states)


    return return_states


def display(state):
    print(state)

def split(state, pile_index, split_index):


    new_piles = []
    pile_to_split = state[pile_index]

    state.remove(pile_index)

    first_pile = split_index
    second_pile = pile_to_split - split_index

    new_piles.append(first_pile)
    new_piles.append(second_pile)


    return state


def main():
    state = [15]
    while not is_terminal(state):
        state[minmax_decision(state)]
    if not is_terminal(state):
        display(state)
        pile_index = input("Which pile to split? (Number in row")
        split_index = input("Where do you want to split(index of pile)")
        state = split(state, pile_index, split_index)



    """    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)

    """
def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
