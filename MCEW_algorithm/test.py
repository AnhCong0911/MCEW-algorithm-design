# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

point1 = Point(1, 2)
point2 = Point(3, 4)

# Create a figure and a subplot
fig, ax = plt.subplots()

# Set the limits of the subplot
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Add the points to the plot
ax.plot(point1.x, point1.y, 'ok')
ax.plot(point2.x, point2.y, 'og')

# Draw a line between the points
ax.plot([point1.x, point2.x], [point1.y, point2.y], 'r-')

list1 = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3]
list3 = []

print(list3)

