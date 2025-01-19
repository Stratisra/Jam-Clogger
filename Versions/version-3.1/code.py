# Importing libraries
import random

# Creating the Q-table
table = {}
for i1 in range(11):
    for i2 in range(7):
        for i3 in range(11):
            for i4 in range(7):
                key = (i1*5, i2*5, i3*5, i4*5)
                table[key] = [0, 0, 0, 0]

# Defining functions
def generateRandomState():
    result = [0, 0, 0, 0]
    result[0] = random.randint(0, 10) * 5
    result[1] = random.randint(0, 6) * 5
    result[2] = random.randint(0, 10) * 5
    result[3] = random.randint(0, 6) * 5
    result = tuple(result)
    return result

def checkTerminalState(state):
    for item in state:
        if item != 0:
            return False
    return True

def findNextAction(state):
    if random.random() >= 0.8:
        return random.randint(0, 3)
    else:
        maxValue = max(table[state])
        return table[state].index(maxValue)

def findNextState(state, action):
    state = list(state)
    if action == 0:
        state[0] = state[0] - 5
        state[2] = state[2] - 5
    if action == 1:
        state[0] = state[0] - 5
        state[1] = state[1] - 5
    if action == 2:
        state[2] = state[2] - 5
        state[3] = state[3] - 5
    if action == 3:
        state[1] = state[1] - 5
        state[3] = state[3] - 5
    for value in state:
        if value < 0:
            state[state.index(value)] = 0
    return tuple(state)

def findShortestPath():
    state = generateRandomState()
    if checkTerminalState(state):
        return []
    else:
        path = []
        while not checkTerminalState(state):
            action = findNextAction(state)
            step = [state, action]
            path.append(step)
            state = findNextState(state, action)
            print(f'state: {state} | action: {action}')
    return path

print(findShortestPath())
