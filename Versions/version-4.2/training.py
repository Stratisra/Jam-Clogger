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

def findBestAction(state):
    maxValue = max(table[state])
    return table[state].index(maxValue)

def findNextState(state, action):
    state = list(state)
    if action == 0:
        state[0] = state[0] - 5#
        state[2] = state[2] - 5#
    if action == 1:
        state[0] = state[0] - 5#
        state[1] = state[1] - 5
    if action == 2:
        state[2] = state[2] - 5#
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
            action = findBestAction(state)
            step = [state, action]
            path.append(step)
            print(f'state: {state} | action: {action}')
            state = findNextState(state, action)
    return path

def calculateReward(oldState, newState):
    reward = 0
    for oldValue, newValue in zip(oldState, newState):
        reward += oldValue - newValue
    return reward * 5

def calculatePunishment(state):
    punishment = 0
    for value in state:
        punishment += value
    return punishment

# Training Session
print('[Starting Training]\n')
for episode in range(10000):
    # Generating the starting state for the episode
    state = generateRandomState()
    while not checkTerminalState(state):
        # Choosing the appropriate action
        action = findNextAction(state)
        # Performing action and transitioning to new state
        oldState = state
        state = findNextState(state, action)
        # Calculating the reward and the temporal difference
        reward = 0
        reward += calculateReward(oldState, state)
        reward -= calculatePunishment(state)
        if checkTerminalState(state):
            reward += 100
        oldValue = table[state][action]
        temporalDifference = reward + (0.9 * max(table[state])) - oldValue
        # Updating the Q-value
        newValue = oldValue + (0.9 * temporalDifference)
        table[oldState][action] = newValue

file = open('data.txt', 'w')
keys = table.keys()
for key in keys:
    for item in table[key]:
        file.write(f'{item} ')
    file.write('\n')


print('[Finished Training]\n\n')
print('[Running Examples]\n')
for i in range(10):
    print(f'[Example {i+1}]')
    findShortestPath()
    print('\n')
