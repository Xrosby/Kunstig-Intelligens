def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for state in successors_of(state):
            v = max(v, min_value(state))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for state in successors_of(state):
            v = min(v, max_value(state))
        return v

    infinity = float('inf')
    state = argmax(successors_of(state), lambda a: min_value(a))
    return state



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
        state = minmax_decision(state)
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
