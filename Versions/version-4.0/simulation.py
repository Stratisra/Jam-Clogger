# Importing libraries
import random

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

    def changeBehaviour():
        if random.random() > 0.2:
            return random.random()
        else:
            return self.behaviour

    def addVehicle():
        self.behaviour = changeBehaviour()
        if random.random() > self.behaviour:
            self.vehicles += 1

# Defining functions
def findBestAction(state):
    maxValue = max(table[state])
    return table[state].index(maxValue)

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

trafficLights = [vehicleGenerator(True), vehicleGenerator(False), vehicleGenerator(True), vehicleGenerator(False)]
