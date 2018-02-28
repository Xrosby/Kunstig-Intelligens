A = 'A'
B = 'B'
C = 'C'
D = 'D'

LEFT = 'Left'
RIGHT = 'Right'
UP = 'Up'
DOWN = 'Down'
DIRTY = 'Dirty'
CLEAN = 'Clean'
SUCK = 'Suck'
CURRENT = 'Current'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': A
}


def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == DIRTY:
        return SUCK
    if loc_st[0] == A:
        return RIGHT
    if loc_st[0] == B:
        return DOWN
    if loc_st[0] == C:
        return LEFT
    if loc_st[0] == D:
        return UP

def Sensors():  # Sense Environment
    location = Environment[CURRENT]
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment[CURRENT]
    if action == SUCK:
        Environment[location] = CLEAN
    elif action == RIGHT and location == A:
        Environment[CURRENT] = B
    elif action == DOWN and location == B:
        Environment[CURRENT] = C
    elif action == LEFT and location == C:
        Environment[CURRENT] = D
    elif action == UP and location == D:
        Environment[CURRENT] = A


def run(n):  # run the agent through n steps
    print('    Current                        New')
    print('location    status  action  location    status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = REFLEX_VACUUM_AGENT(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == '__main__':
    run(20)
