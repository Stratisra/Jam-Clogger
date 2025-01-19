#import libraries
import numpy as np
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
        return random.randint(0, 4)
    else:
        maxNum = max(table[tuple(state)])
        return table[tuple(state)].index(maxNum) + 1

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

getShortestPath()
