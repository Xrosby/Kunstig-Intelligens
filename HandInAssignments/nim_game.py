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
    return same_elements(state)


def same_elements(iterator):
    return len(set(iterator)) <= 1


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
        for i in range(0, len(pile)):
            print(i)
            if i != pile and i != pile/2:
                list_of_successor_states.append((i, pile-i))

    return list_of_successor_states


def display(state):
    print(state)


def main():
    board = [15]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
