# -*- coding: utf-8 -*-
import math
import random
import csv
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

    # DUY
    def cost(self, _node):
        # code here
        # Tính cost theo yêu cầu đề bài
        # cost = round(0.3 x distance())
        return round(0.3 * self.distance(_node))

        # Tìm hàng xóm của Node
        # Hàng xóm: (Nodes in Nlist) - (self $ comp_list(_node))
    def find_neighbor_of_node(self, _nlist):
        temp1 = []
        temp1 = self.comp_list + self.nonlink_checked_neighbor
        temp1.append(self)
        temp2 = [i for i in _nlist if i not in set(temp1)]
        # code here
        neighbor_of_node = None
        neighbor_distance = MAX
        for n in temp2:
            dis = self.distance(n)
            if(dis < neighbor_distance):
                neighbor_distance = dis
                neighbor_of_node = n
        self.neighbor = neighbor_of_node
        self.neighbor_dis = neighbor_distance

    def update_component_list(self, other_node):
        self.comp_list.append(other_node)
        self.comp_list += other_node.comp_list
    
    def compute_trade_off(self):
        cost_ij = round(0.3 * self.distance(self.neighbor))
        min_node, min_component_cost = comp_cost(self)
        self.trade_off = cost_ij - min_component_cost # Thoa hiep duoc tinh toan o day


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

        # Write the data rows
        for point in _list:
            writer.writerow(point.get())


def get_point_list():
    point_list = []
    with open('point_list.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x_str, y_str = row
            x = int(x_str)
            y = int(y_str)
            point_list.append(Point(x, y))
    return point_list

# HIEP
# Creat bachbone_list, node_list from point_list, set weight cho cac node
# vẽ các node và backbone lên mặt phẳng
# Input: point_list
# Output: b_list, n_list

# test: 10 Points
def create_and_visualize_blist_nlist_test(_axes, _list):
    b_list = []
    n_list = []
    b_index = [2, 5, 8]
    n1_index = [3, 6]
    n2_index = [9]
    n_index = n1_index + n2_index
    for i in range(MAX_POINTS):
        x, y = _list[i].get()
        if i in b_index:
            b_list.append(Backbone(x, y))
            visualize_backbone(_axes, x, y)
        else:
            visualize_node(_axes, x, y)
            if i in n1_index:
                n_list.append(Node(x, y, w=2))
            elif i in n2_index:
                n_list.append(Node(x, y, w=3))
            else:
                n_list.append(Node(x, y))
    return b_list, n_list

def create_and_visualize_blist_nlist(_axes, _list):
    b_list = []
    n_list = []
    b_index = [4, 11, 30, 64, 87]
    n1_index = [0, 7, 8]
    n2_index = [22, 71, 28, 66, 54]
    n3_index = [3, 47]
    n_index = n1_index + n2_index + n3_index
    for i in range(MAX_POINTS):
        x, y = _list[i].get()
        if i in b_index:
            b_list.append(Backbone(x, y))
            visualize_backbone(_axes, x, y)
        else:
            visualize_node(_axes, x, y)
            if i in n1_index:
                n_list.append(Node(x, y, w=2))
            elif i in n2_index:
                n_list.append(Node(x, y, w=3))
            elif i in n3_index:
                n_list.append(Node(x, y, w=5))
            else:
                n_list.append(Node(x, y))
    return b_list, n_list

# DUY
# Find S - Tập node con của backbone b


def find_S(_axes, _blist, _nlist):
    for n in _nlist:
        min_center = MAX
        backbone_of_n = None
        for b in _blist:
            nb_dis = n.distance(b)
            if(nb_dis < min_center):
                min_center = nb_dis
                backbone_of_n = b
        n.center_dis = min_center
        n.center = backbone_of_n  # final min distance
        draw_link(_axes, n, backbone_of_n)  # gọi hàm không có axes
        backbone_of_n.S.append(n)

# DUONG
# Tìm node hàng xóm (neighbor) của từng node trong tập N
# & tính khoảng cách hàng xóm ~ cost(Ni, Nj)
# Input: N list
# Output:


def find_neighbor(_nlist):
    # code here
    for n in _nlist:
        n.find_neighbor_of_node(_nlist)

# DUY
# Tìm thỏa hiệp của từng node trong tập N, duyệt tìm TH min => Theo pseudocode
# Input: N list
# Output:


# def compute_trade_off(_node):
#     # code here
#     cost_ij = round(0.3 * _node.distance(_node.neighbor))
#     min_node, min_component_cost = comp_cost(_node)
#     trade_off = cost_ij - min_component_cost
#     _node.trade_off = trade_off
#     return trade_off

# Input: Nlist
# Output: Node, min_trade_off


def min_trade_off(_nlist):
    min_value = MAX
    temp_node = None
    for n in _nlist:
        if(n.trade_off < min_value):
            min_value = n.trade_off
            temp_node = n
    return temp_node, min_value


# Tính cost từ _node, và comp_list cua _node den center
# Output: min_node, min_cost
def comp_cost(_node):
    temp = []
    temp.append(_node)
    temp += _node.comp_list
    center = _node.center
    min_dis = MAX
    min_node = None
    for n in temp:
        dis = center.distance(n)
        if(dis < min_dis):
            min_dis = dis
            min_node = n
    # Tinh cost
    return min_node, round(0.3 * min_dis)


# HIEP
# def update_thoa_hiep(_nodei, _nodej):
    # code here

    # DUY
    # Input: Node i, Node j
    # Output: True if accept, otherwise False


def weight_condition(_nodei, _nodej, W):
    # code here
    comp_wi = compute_comp_w(_nodei)
    comp_wj = compute_comp_w(_nodej)
    w = comp_wi + comp_wj
    if(w <= W):
        return True
    else:
        return False


def compute_comp_w(_node):
    weight = _node.w
    if(len(_node.comp_list) != 0):
        for n in _node.comp_list:
            weight += n.w
    return weight

# DUONG
# Input: Node, MAX_STEP
# Output: True/False


def jump_condition(_node, MAX_STEP):
    # code here
    if(compute_jumpstep(_node) <= MAX_STEP):
        return True
    else:
        return False

# Tinh buoc nhay cua _node


def compute_jumpstep(_node):
    jump_step = 1
    node_temp = _node
    while(node_temp.previous != None):
        jump_step += 1
        node_temp = node_temp.previous
    return jump_step

# HIEP
# Ghép


def connect_link(axes, _nodei, _nodej):
    remove_link(axes, _nodei, _nodei.center)
    draw_link(axes, _nodei, _nodej)
    update_nodei(_nodei, _nodej)
    update_nodej(_nodei, _nodej)

# Cập nhât thông tin nodei theo nodej


def update_nodei(_nodei, _nodej):
    _nodei.center = _nodej.center
    _nodei.center_dis = _nodei.distance(_nodei.center)
    _nodei.previous = _nodej  # Create Previous node
    _nodei.update_component_list(_nodej)


def update_nodej(_nodei, _nodej):
    _nodej.update_component_list(_nodei)

# Xóa visulize giữa hai node


def remove_link(_axes, _nodei, _nodej):
    _axes.plot([_nodei.x, _nodej.x], [_nodei.y, _nodej.y], 'w-')
    _axes.plot(_nodei.x, _nodei.y, 'ok')
    _axes.plot(_nodej.x, _nodej.y, 'or')

# HIEP
# Bỏ


def ignore_link(_nodei, _nodej):
    # code here
    _nodei.nonlink_checked_neighbor.append(_nodej)
    _nodej.nonlink_checked_neighbor.append(_nodei)


# DUONG
# def is_finish_algorithm():
    # code here

    # CONG


def MCEW(_nlist, _blist):
    find_neighbor(_nlist)
    min_thoa_hiep = MAX
    Ni = None  # Ni
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
