A = 'A'
B = 'B'


SUCK = 'Suck'
DIRTY = 'Dirty'
CLEAN = 'Clean'
CURRENT = 'Current'
RIGHT = 'Right'
DOWN = 'Down'
LEFT = 'Left'
UP = 'Up'
NOOP = 'NoOp'



state = {}
action = None
model = {A: None, B: None}  # Initially ignorant

RULE_ACTION = {
    1: SUCK,
    2: RIGHT,
    3: LEFT,
    4: NOOP

}

rules = {
    (A, DIRTY): 1,
    (A, CLEAN): 2,
    (B, DIRTY): 1,
    (B, CLEAN): 3,
    (A, B, CLEAN): 4
}
# Ex. rule (if location == A && Dirty then rule 1)

Environment = {
    A: DIRTY,
    B: DIRTY,
    CURRENT: A
}


def INTERPRET_INPUT(input):  # No interpretation
    return input


def RULE_MATCH(state, rules):  # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule


def UPDATE_STATE(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == CLEAN:
        state = (A, B, CLEAN)
        # Model consulted only for A and B Clean
    model[location] = status  # Update the model state
    return state


def REFLEX_AGENT_WITH_STATE(percept):
    global state, action
    state = UPDATE_STATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = RULE_ACTION[rule]
    return action


def Sensors():  # Sense Environment
    location = Environment[CURRENT]
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment[CURRENT]
    if action == SUCK:
        Environment[location] = CLEAN
    elif action == RIGHT and location == A:
        Environment[CURRENT] = B
    elif action == LEFT and location == B:
        Environment[CURRENT] = A


def run(n):  # run the agent through n steps
    print('    Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_AGENT_WITH_STATE(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == '__main__':
    run(20)
