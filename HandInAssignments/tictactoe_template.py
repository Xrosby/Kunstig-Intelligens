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



X = 'X'
O = 'O'


def is_terminal(state):

    terminal = False

    for c in state:
        if is_number(c):
            terminal = False
        else:
            terminal = True


    possibleLines = [
        (state[0], state[1], state[2]),
        (state[3], state[4], state[5]),
        (state[6], state[7], state[8]),
        (state[0], state[3], state[6]),
        (state[1], state[4], state[7]),
        (state[2], state[5], state[8]),
        (state[0], state[4], state[8]),
        (state[2], state[4], state[6]),
    ]


    for line in possibleLines:
        if three_in_line(line):
            terminal = True



    return terminal


def is_number(c):
    return type(c) == int


def three_in_line(line):
    return line[0] == line[1] == line[2]



def utility_of(state):

    o_wins = False
    x_wins = False

    possibleLines = [
        (state[0], state[1], state[2]),
        (state[3], state[4], state[5]),
        (state[6], state[7], state[8]),
        (state[0], state[3], state[6]),
        (state[1], state[4], state[7]),
        (state[2], state[5], state[8]),
        (state[0], state[4], state[8]),
        (state[2], state[4], state[6]),
    ]


    for line in possibleLines:
        if three_in_line(line):
            result = line[0]
            if result == X:
                x_wins = True
            elif result == O:
                o_wins = True

    if o_wins:
        return -1
    elif x_wins:
        return 1

    else:
        return 0


def successors_of(state):

    print(state)


    list_of_successor_states = []

    odd_or_even = 0
    for i in state:
        if is_number(i):
            odd_or_even += 1

    x_turn = False
    o_turn = False

    if odd_or_even % 2 == 0:
        o_turn = True
    else:
        x_turn = True


    for i in range(9):

        move = state[i]
        if is_number(state[i]):

            new_state = state[:]
            if o_turn:
                new_state[move] = O
            elif x_turn:
                new_state[move] = X
            list_of_successor_states.append((move, new_state))

    print(list_of_successor_states)


    return list_of_successor_states




def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = X
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = O
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
