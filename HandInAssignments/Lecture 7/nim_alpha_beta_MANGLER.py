def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for state in successors_of(state):
            v = max(v, min_value(state))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for state in successors_of(state):
            v = min(v, max_value(state))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a))
    return action



def is_terminal(state):
    print(state)

    for pile in state:
        if pile >= 3:
            return False
    return True



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
            index = 0
            if pile %2 == 0:
                index = int(pile / 2)
            else:
                index = int(pile/2)
            for j in range(1, index):

                list_of_successor_states = state[:]
                list_of_successor_states.remove(pile)
                list_of_successor_states.append(j)
                list_of_successor_states.append(pile-j)
                return_states.append(list_of_successor_states)


    return return_states


def display(state):
    print(state)


def main():
    state = [15]
    while not is_terminal(state):
        state[minmax_decision(state)]
    if not is_terminal(state):
        display(state)
        pile_index = input("Which pile to split? (Number in row")
        split_index = input("Where do you want to split(index of pile)")



def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
