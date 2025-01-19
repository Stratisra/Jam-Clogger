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
print(table)
