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

    distinct_element = False


    current_element = int(state[0])
    skipped_elements = 0
    skipped_elementIndex = 0

    for i in range(1, len(state)):
        if state[i] == current_element:
            current_element = state[i]
        else:
            skipped_elements += 1
            skipped_elementIndex = i


    state.remove(skipped_elementIndex)



    if skipped_elements == 1 and state[0] == 1:
        distinct_element = True



    return distinct_element




def utility_of(state):
    if len(state) % 2 == 0:
        return 0
    else:
        return 1


def successors_of(state):
    list_of_successor_states = []
    print("State", state)


    """
    REWRITE MINMAX DESCISION TO FIX THIS
    """

    for pile in state:
        for i in range(0, pile):
            print(i)
            if i != pile and i != pile/2:
                list_of_successor_states.append((i, pile-i))

    return list_of_successor_states


def display(state):
    print(state)


def main():
    board = [15, 1]
    while not is_terminal(board):
        board[minmax_decision(board)] = 2
    if not is_terminal(board):
        display(board)
        board[(int(input("Your nove? ")))] = 2


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
