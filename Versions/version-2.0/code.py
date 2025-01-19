#import libraries
import random

# Importing index values (states) from file ('index.txt')
indexFile = open('index.txt', 'r')
index = []
for line in indexFile:
    list = line.split()
    for i in range(0, len(list)):
        list[i] = int(list[i])
    index.append(list)

# Importing data (Q-values) from file ('data.txt')
dataFile = open('data.txt', 'r')
data = []
for line in dataFile:
    list = line.split()
    for i in range(0, len(list)):
        list[i] = int(list[i])
    data.append(list)

# Creating the Q-table (table)
table = {}
for indexValue, dataValue in zip(index, data):
    table[tuple(indexValue)] = dataValue

# Defining functions
def generateNewState():
    state = []
    for i in range(4):
        state.append(index[random.randint(0, 3025)][i])
    return state

def terminalState(state):
    for value in state:
        if value != 0:
            return False
    return True

def getNewAction(state):
    if random.random() >= 0.8:
        return random.randint(1, 5)
    else:
        list = table[tuple(state)]
        maxValue = max(table[tuple(state)])
        return table[tuple(state)].index(maxValue) + 1

def getNewState(state, action):
    if action == 1:
        state[0] = state[0] - 5
        state[2] = state[2] - 5
    if action == 2:
        state[0] = state[0] - 5
        state[1] = state[1] - 5
    if action == 3:
        state[2] = state[2] - 5
        state[3] = state[3] - 5
    if action == 4:
        state[1] = state[1] - 5
        state[3] = state[3] - 5
    for value in state:
        if value < 0:
            state[state.index(value)] = 0
    return state

def getShortestPath():
    state = generateNewState()
    if terminalState(state):
        return []
    else:
        path = []
        while not terminalState(state):
            action = getNewAction(state)
            step = [state, action]
            path.append(step)
            state = getNewState(state, action)
            print(f'state: {state} | action: {action}')
    return path

def calculateReward(oldState, newState):
    reward = 0
    for oldValue, newValue in zip(oldState, newState):
        reward += oldValue - newValue
    return reward * 3

def calculatePunishment(state):
    punishment = 0
    for value in state:
        punishment += value
    return punishment

# Training Session
for episode in range(1000000):
    # Generating the starting state for the episode
    state = generateNewState()
    while not terminalState(state):
        # Choosing the appropriate action
        action = getNewAction(state)
        # Performing action and transitioning to new state
        oldState = state
        state = getNewState(state, action)
        # Calculating the reward and the temporal difference
        reward = 0
        reward += calculateReward(oldState, state)
        reward -= calculatePunishment(state)
        if terminalState(state):
            reward += 100
        oldValue = table[tuple(state)][action-1]
        temporalDifference = reward + (0.9 * max(table[tuple(state)])) - oldValue
        # Updating the Q-value
        newValue = oldValue + (0.9 * temporalDifference)
        table[tuple(oldState)] = newValue

print(table)
