# Importing libraries
import random
import time

# Initiating Variables
numStates = 2499561
numLoops = 100000

# Defining Classes
class vehicleGenerator():
    def __init__(self, double):
        self.double = double
        # if double:
        #     self.vehicles = random.randint(0, 50)
        # else:
        #     self.vehicles = random.randint(0, 30)
        self.vehicles = 0
        self.behaviour = random.random()

    def changeBehaviour(self):
        if random.random() < 0.1:
            return random.random()
        else:
            return self.behaviour

    def moreVehicles(self):
        if random.random() < 0.05:
            return int(random.randint(1, 5))
        else:
            return 0

    def addVehicle(self):
        self.behaviour = self.changeBehaviour()
        if random.random() > self.behaviour:
            self.vehicles += 1
        self.vehicles += self.moreVehicles()
        if self.double and self.vehicles > 50:
            self.vehicles = 50
        elif not self.double and self.vehicles > 30:
            self.vehicles = 30

# Defining functions
def findBestAction():
    state = getState()
    maxValue = max(table[state])
    return table[state].index(maxValue)

def getState():
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = trafficLights[i].vehicles
    return tuple(result)

def updateState(action):
    if action == 0:
        trafficLights[0].vehicles = trafficLights[0].vehicles - 2
        trafficLights[2].vehicles = trafficLights[2].vehicles - 2
    if action == 1:
        trafficLights[0].vehicles = trafficLights[0].vehicles - 2
        trafficLights[1].vehicles = trafficLights[1].vehicles - 1
    if action == 2:
        trafficLights[2].vehicles = trafficLights[2].vehicles - 2
        trafficLights[3].vehicles = trafficLights[3].vehicles - 1
    if action == 3:
        trafficLights[1].vehicles = trafficLights[1].vehicles - 1
        trafficLights[3].vehicles = trafficLights[3].vehicles - 1
    for i in range(3):
        if trafficLights[i].vehicles < 0:
            trafficLights[i].vehicles = 0

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
                # progressBar(numStates-1, i, 'Importing')
                key = (i1, i2, i3, i4)
                line = file.readline()
                strings = line.split()
                value = [float(x) for x in strings]
                table[key] = value
                i += 1
endTime = time.time()
file.close()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')

# Traffic simulation
startTime = time.time()
print('[Started Simulation]')
trafficLights = [vehicleGenerator(True), vehicleGenerator(False), vehicleGenerator(True), vehicleGenerator(False)]
simulation = []
file = open('Data/traffic.txt', 'w')

for loop in range(numLoops):
    progressBar(numLoops-1, loop, 'Running')
    state = getState()
    action = findBestAction()

    # print([state, action])
    file.write(f'{[state, action]}\n')
    simulation.append([state, action])

    updateState(action)
    for i in range(4):
        trafficLights[i].addVehicle()

file.close()
endTime = time.time()
print(f'\n[Finished in {round(endTime - startTime, 2)}s]\n')
