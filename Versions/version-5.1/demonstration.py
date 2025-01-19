# Importing libraries
import random
import time

# Initiating Variables
numExamples = 100
numStates = 2499561

# Defining functions
def generateRandomState():
    result = [0, 0, 0, 0]
    result[0] = random.randint(0, 50)
    result[1] = random.randint(0, 30)
    result[2] = random.randint(0, 50)
    result[3] = random.randint(0, 30)
    result = tuple(result)
    return result

def checkTerminalState(state):
    for item in state:
        if item != 0:
            return False
    return True

def findNextAction(state, p):
    if random.random() >= p:
        return random.randint(0, 3)
    else:
        maxValue = max(table[state])
        return table[state].index(maxValue)

def findNextState(state, action):
    state = list(state)
    if action == 0:
        state[0] = state[0] - 2
        state[2] = state[2] - 2
    if action == 1:
        state[0] = state[0] - 2
        state[1] = state[1] - 1
    if action == 2:
        state[2] = state[2] - 2
        state[3] = state[3] - 1
    if action == 3:
        state[1] = state[1] - 1
        state[3] = state[3] - 1
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
            action = findNextAction(state, 1)
            step = [state, action]
            path.append(step)
            state = findNextState(state, action)
    return path

def progressBar(total, progress, description):
    percent = 100 * (progress / float(total))
    bar = description + '|' + '█' * int(percent) + '-' * (100 - int(percent)) + '|' + str(round(percent, 2)) + '%'
    print(f'\r{bar}', end='\r')

# Importing Q-values
startTime = time.time()
print('[Importing Data]')
file = open('Data/data.txt', 'r')
table = {}
i = 0
for i1 in range(51):
    for i2 in range(31):
        for i3 in range(51):
            for i4 in range(31):
                progressBar(numStates-1, i, 'Importing')
                key = (i1, i2, i3, i4)
                line = file.readline()
                strings = line.split()
                value = [float(x) for x in strings]
                table[key] = value
                i += 1
endTime = time.time()
file.close()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')

# Running Examples
file = open('Data/examples.txt', 'w')
print('[Running Examples]')
startTime = time.time()
for i in range(numExamples):
    file.write(f'[Example {i+1}]\n')
    path = findShortestPath()
    progressBar(numExamples - 1, i, 'Running')
    for step in path:
        file.write(f'state: {step[0]} | action: {step[1]}\n')
    file.write('\n')
endTime = time.time()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]')
