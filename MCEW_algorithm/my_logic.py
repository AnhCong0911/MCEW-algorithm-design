# -*- coding: utf-8 -*-
import math
from my_visualize import *

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
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 1
        self.center = center # Backbone
        self.center_dis = -1
        self.previous = previous # Point
        self.neighbor_dis = -1
        self.comp_list = [] # list of Node
        self.thoa_hiep = thoa_hiep
        
    # DUY
    def cost(self, _node):
        # code here
        # Tính cost theo yêu cầu đề bài
        # cost = round(0.3 x distance())
    
    # X
    def thoa_hiep(self):
        #code here
    
class Backbone(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.S = []

# create MAX_POINTS points randomly
# Input:
# Output: List of Points
def create_random_points():
    # Create an empty list to store the points
    point_list = []

    # Generate  random points
    for i in range(MAX_POINTS):
        x = random.randint(0, X_MAX)
        y = random.randint(0, Y_MAX)
        point = Point(x, y)
        point_list.append(point)
    
    return point_list

# save into csv file
# Input: list
# Output:
def save_point_list_into_csv_file(_list):
    with open('point_list.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['x', 'y'])

        # Write the data rows
        for point in _list:
            writer.writerow(point.get())

# HIEP
# Creat bachbone_list, node_list from point_list, set weight cho cac node
# Input: point_list
# Output: b_list, n_list
def create_blist_nlist(_list):
    b_list = []
    n_list = []
    # code here: use get_index()

# DUY 
# Find S - Tập node con của backbone b    
def find_S(_blist, _nlist):
    for n in _nlist:
        min_center = MAX
        backbone_of_n = None
        for b in _blist:
            nb_dis = n.distance(b)
            if(nb_dis < min_center):
                min_center = nb_dis
                backbone_of_n = b
        n.center_dis = min_center
        n.center = backbone_of_n
        draw_link(n, backbone_of_n)
        backbone_of_n.S.append(n)

# DUONG
# Tìm node hàng xóm (neighbor) của từng node trong tập N
# & tính khoảng cách hàng xóm ~ cost(Ni, Nj)
# Input: N list
# Output:
def find_neighbor(_nlist):
    # code here
    
# DUY
# Tìm thỏa hiệp của từng node trong tập N, duyệt tìm TH min => Theo pseudocode
# Input: N list
# Output:
def find_thoa_hiep(_nlist):
    # code here

# HIEP
def update_thoa_hiep(_nodei, _nodej):
    # code here

# DUY
# Input: Node i, Node j
# Output: True if accept, otherwise False
def weight_condition(_nodei, _nodej):
    # code here

# DUONG
# Input: Node
# Output: True/False    
def jump_condition(_node):
    # code here

# HIEP
# Ghép
def connect_link(_nodei, _nodej):
    draw_link(_nodei, _nodej)
    _nodei.previous = _nodej
    remove_link(_nodei, _nodei.center)
    _nodei.center = _nodej.center

# HIEP
# Bỏ
def ignore_link(_nodei, _nodej):
    # code here

# DUONG
def is_finish_algorithm():
    # code here
    
# CONG
def MCEW( _nlist, _blist):
    find_neighbor(_nlist)
    min_thoa_hiep = MAX
    Ni = None # Ni
    Nj = None
    for n in N:
        # Thỏa_hiệp(Ni) = cost(Ni, neighbor) - cost(Ni, Root)
        n.thoa_hiep = n.neighbor_dis - n.center_dis
        if(n.thoa_hiep < min_thoa_hiep):
            min_thoa_hiep = n.thoa_hiep
            Ni = n
    Nj = Ni.neighbor
    if(weight_condition(Ni, Ni.neighbor)):
        connect_link(Ni, Ni.neighbor)
    else:
        ignore_link(Ni, Ni.neighbor)
    update_thoa_hiep(Ni, Nj)
    is_finish_algorithm()
    
    


        
        
    