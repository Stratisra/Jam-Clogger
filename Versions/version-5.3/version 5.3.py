# Importing libraries
import random
import time

# Initiating Variables
numEpisodes = 400000000
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

def findNextAction(state, e):
    if random.random() >= e:
        return random.randint(0, 19)
    else:
        maxValue = max(table[state])
        return table[state].index(maxValue)

def findNextState(state, action):
    state = list(state)
    if action < 5:
        action = (action + 1) * 2
        multiplier = 1 + (action / 10)
        state[0] = state[0] - int(action * multiplier * 2)
        state[2] = state[2] - int(action * multiplier * 2)
    elif action < 10:
        action -= 4
        action = action * 2
        multiplier = 1 + (action / 10)
        state[0] = state[0] - int(action * multiplier * 2)
        state[1] = state[1] - int(action * multiplier)
    elif action < 15:
        action -= 9
        action = action * 2
        multiplier = 1 + (action / 10)
        state[2] = state[2] - int(action * multiplier * 2)
        state[3] = state[3] - int(action * multiplier)
    elif action < 20:
        action -= 14
        action = action * 2
        multiplier = 1 + (action / 10)
        state[1] = state[1] - int(action * multiplier)
        state[3] = state[3] - int(action * multiplier)
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

def calculateReward(oldState, newState):
    reward = 0
    for oldValue, newValue in zip(oldState, newState):
        reward += oldValue - newValue
    return reward * 5

def calculatePunishment(state):
    punishment = 0
    for value in state:
        punishment += (value * (value+1)) / 2
    return punishment

def progressBar(total, progress, description):
    percent = 100 * (progress / float(total))
    bar = description + '|' + '█' * int(percent) + '-' * (100 - int(percent)) + '|' + str(round(percent, 2)) + '%'
    print(f'\r{bar}', end='\r')

# Creating the Q-table
startTime = time.time()
print('[Started Initialization]')
table = {}
i = 0
for i1 in range(51):
    for i2 in range(31):
        for i3 in range(51):
            for i4 in range(31):
                # progressBar(numStates-1, i, 'Initializing')
                key = (i1, i2, i3, i4)
                table[key] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                i += 1
endTime = time.time()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')

# Training Session
print('[Started Training]')
startTime = time.time()
for episode in range(numEpisodes):
    # Generating the starting state for the episode
    progressBar(numEpisodes - 1, episode, 'Training')
    state = generateRandomState()
    while not checkTerminalState(state):
        # Choosing the appropriate action
        action = findNextAction(state, 0.1)
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
        table[oldState][action] = round(newValue, 3)
endTime = time.time()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')

print('[Saving Data]')
startTime = time.time()
file = open('data.txt', 'w')
keys = table.keys()
i = 0
for key in keys:
    # progressBar(numStates-1, i, 'Saving')
    for item in table[key]:
        file.write(f'{item} ')
    file.write('\n')
    i += 1
file.close()
endTime = time.time()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')


file = open('examples.txt', 'w')
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