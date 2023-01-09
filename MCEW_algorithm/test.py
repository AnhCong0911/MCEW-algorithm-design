# -*- coding: utf-8 -*-
import math
import csv
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

    # Tính khoảng cách đề-các giữa 2 points
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


class Node(Point):
    def __init__(self, x, y, w=1, center=None, center_dis=-1,
                 previous=None, neighbor=None, neighbor_dis=-1,
                 trade_off=None):
        super().__init__(x, y)
        self.w = w
        self.center = center  # Backbone
        self.center_dis = center_dis
        self.previous = previous  # Node
        self.neighbor = neighbor
        self.neighbor_dis = neighbor_dis
        self.nonlink_checked_neighbor = []  # list of neighbor is checked
        self.comp_list = []  # list of Node
        self.trade_off = trade_off


class Backbone(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.S = []

a = [1, 3]
b = []
a += b

