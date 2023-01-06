# -*- coding: utf-8 -*-
import math, csv
import matplotlib.pyplot as plt
from my_constant import *
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

with open('point_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:

        print(type(row))
        print(type(x_int), type(y_int))
