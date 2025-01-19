# Importing libraries
import random
import time

# Reading the Q-table
file = open('data.txt', 'r')
table = {}
for i1 in range(11):
    for i2 in range(7):
        for i3 in range(11):
            for i4 in range(7):
                key = (i1*5, i2*5, i3*5, i4*5)
                line = file.readline()
                table[key] = line.split()

# Defining Classes
class vehicleGenerator():
    def __init__(self, double):
        if double:
            self.vehicles = random.randint(0, 10) * 5
        else:
            self.vehicles = random.randint(0, 6) * 5
        self.behaviour = random.random()

    def changeBehaviour(self):
        if random.random() < 0.1:
            return random.random()
        else:
            return self.behaviour

    def moreVehicles(self):
        if random.random() < 0.03:
            return int(random.randint(1, 5))
        else:
            return 0

    def addVehicle(self):
        self.behaviour = self.changeBehaviour()
        if random.random() > self.behaviour:
            self.vehicles += 1
        self.vehicles += self.moreVehicles()

# Defining functions
def categorizeState():
    state = [0, 0, 0, 0]
    help = [0, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 40, 40, 40, 40, 40, 45, 45, 45, 45, 45, 50, 50, 50, 50, 50]
    for i in range(3):
        if trafficLights[i].vehicles > 30 and i == 1 or i == 3:
            state[i] = 30
        elif trafficLights[i].vehicles > 50 and i == 0 or i == 2:
            state[i] = 50
        else:
            state[i] = help[trafficLights[i].vehicles]
    return tuple(state)

def findBestAction():
    state = categorizeState()
    maxValue = max(table[state])
    return table[state].index(maxValue)

def getState():
    result = [0, 0, 0, 0]
    for i in range(3):
        result[i] = trafficLights[i].vehicles
    return result

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

# Traffic simulation
trafficLights = [vehicleGenerator(True), vehicleGenerator(False), vehicleGenerator(True), vehicleGenerator(False)]
simulation = []

while 1:
    state = getState()
    action = findBestAction()

    print([state, action])
    simulation.append([state, action])

    updateState(action)
    for i in range(3):
        trafficLights[i].addVehicle()
    time.sleep(0.5)
