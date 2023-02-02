# -*- coding: utf-8 -*-
import math
import random
import csv
from tree_visualize import *
from tree_constant import *
from my_tree import *
from tree_logic import *
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x = x
        self.y = y


class Backbone:
    def __init__(self, x, y, deep=MAX, level=0):
        self.x = x
        self.y = y
        self.children = []
        self.deep = deep
        self.level = level

    def add_child(self, child):
        child.deep = self.deep - 1
        child.level = self.level + 1  # Change level
        child.parent = self
        if(child.level == 1):
            child.center = self # Create center when finding S
        else:
            child.center = self.center
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


class Node(Backbone):
    def __init__(self, x, y, w=1, parent=None, center=None,
                 neighbor=None, trade_off=None):
        super().__init__(x, y)
        self.w = w
        self.parent = parent
        self.center = center  # Backbone
        self.neighbor = neighbor
        self.nonlink_checked_neighbor = []  # list of neighbor is checked
        self.trade_off = trade_off

    def get_weight(self):
        return self.w

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def update_parent(self, parent):
        self.set_parent(parent)
        parent.get_children().append(self)

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center

    def set_neighbor(self, neighbor):
        self.neighbor = neighbor

    def get_nonlink(self):
        return self.nonlink_checked_neighbor

    def add_to_nonlink(self, _node):
        self.nonlink_checked_neighbor.append(_node)

    # def update_level():

    def find_neighbor_of_node(self, _nlist):
        temp1 = []
        temp1 = self.get_complist() + self.nonlink_checked_neighbor  # nonlink_checked_neighbor
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
        self.neighbor = neighbor_of_node  # Create neighbor

    # Create Tradeoff
    def compute_trade_off(self):
        cost_ij = round(0.3 * self.distance(self.neighbor))
        _1th_level_parent = get_ith_level_parent_from_child(self, 1)
        # center created from findS
        comp_cost = round(0.3 * _1th_level_parent.distance(self.center))
        self.trade_off = cost_ij - comp_cost  # Thoa hiep duoc tinh toan o day

    # Get complist
    def get_complist(self):
        _1th_level_parent = None
        if(self.get_level() == 0):
            raise TypeError("Error: Node level = 0!")
        elif(self.get_level() == 1):
            _1th_level_parent = self
        else:
            _1th_level_parent = get_ith_level_parent_from_child(self, 1)
        if(_1th_level_parent == None):
            raise TypeError("Error: Parent node = None!")
        complist = get_all_children_of(_1th_level_parent)
        complist.append(_1th_level_parent)
        return complist

def create_random_points(number=MAX_POINTS, x_max=X_MAX, y_max=Y_MAX):
    # Create an empty list to store the points
    point_list = []

    # Generate  random points
    for i in range(number):
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        point = Point(x, y)
        point_list.append(point)

    return point_list

# save into csv file
# Input: list
# Output:


def save_point_list_into_csv_file(_list, path):
    if(len(path) == 0):
        raise TypeError("Need to have the file path.")
    with open(path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)

        # Write the data rows
        for point in _list:
            writer.writerow(point.get())


def get_point_list(path):
    point_list = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x_str, y_str = row
            x = int(x_str)
            y = int(y_str)
            point_list.append(Point(x, y))
    return point_list

# Creat bachbone_list, node_list from point_list, set weight cho cac node
# vẽ các node và backbone lên mặt phẳng
# Input: point_list
# Output: b_list, n_list


def create_and_visualize_blist_nlist(_axes, _list, b_index, n_index):
    b_list = []
    n_list = []
    n1_index = n_index[0]
    n2_index = n_index[1]
    n3_index = n_index[2]
    n_index = n1_index + n2_index + n3_index
    for i in range(len(_list)):
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
        if(backbone_of_n is None):
            raise TypeError("Error: backbone_of_n is None!")
        backbone_of_n.add_child(n)
        draw_slink(_axes, n, backbone_of_n)

# Tìm node hàng xóm (neighbor) của từng node trong tập N
# & tính khoảng cách hàng xóm ~ cost(Ni, Nj)
# Input: N list
# Output:


def find_neighbor(_list, _nlist):
    # code here
    if len(_list) == 0:
        for n in _nlist:
            n.find_neighbor_of_node(_nlist)
    else:
        for n in _list:
            n.find_neighbor_of_node(_nlist)


def min_trade_off(_nlist):
    min_value = MAX
    temp_node = None
    for n in _nlist:
        if(n.trade_off < min_value):
            min_value = n.trade_off
            temp_node = n
    return temp_node, min_value


def get_ith_level_parent_from_child(child_node, level):
    if(child_node.get_level() < level):
        raise TypeError("Error: parent level > child level!")
    if(child_node.get_level() == level):
        return child_node
    current_node = child_node
    while current_node.get_parent().get_level() > level:
        current_node = current_node.get_parent()
    return current_node.get_parent()

# Sau khi unlink(nodei.parent(level=1), center)
# Tao cay con voi nodei la subroot, va cap nhat cac new-child


def make_subtree_of(_node):
    current = _node
    level_i = _node.get_level()
    temp_parent = _node
    while current.get_parent().get_level() != 0:
        current = current.get_parent()
        # Compute delta
        delta = level_i - current.get_level()
        # Change level
        current.set_level(level_i + delta)
        # Remove temp_parent from children to assign parent
        current.get_children().remove(temp_parent)
        # Change parent and update children[] of parent
        current.update_parent(temp_parent)
        # Update level of all children of current
        all_children = get_all_children_of(current)
        for child in all_children:
            old_level = child.get_level()
            child.set_level(old_level + 2*delta)
        temp_parent = current

# Get component list from level=1 parent


# def get_complist_of(_node):
#     _1th_level_parent = get_ith_level_parent_from_child(_node, 1)
#     complist = get_all_children_of(_1th_level_parent)
#     complist.append(_1th_level_parent)
#     return complist


def get_all_children_of(parent):
    all_children = []
    queue = [parent]
    while queue:
        node = queue.pop(0)
        children = node.get_children()
        if(len(children) != 0):
            all_children += children
            for child in children:
                queue.append(child)
    return all_children

# Tính cost từ _node, và comp_list cua _node den center
# Output: min_node, min_cost


def comp_cost(_node):
    min_node = None
    min_dis = -1
    node_dis = _node.distance(_node.center)
    component_node, min_component_dis = complist_min_dis(_node)
    if (node_dis < min_component_dis):
        min_node = _node
        min_dis = node_dis
    else:  # >=
        min_node = component_node
        min_dis = min_component_dis
    # Tinh cost
    return min_node, round(0.3 * min_dis)

# Tính khoảng cách nhỏ nhất từ comp_list đến center
# Input: _node
# Output: component_node, min_dis


def complist_min_dis(_node):
    min_dis = MAX
    min_comp = None
    for n in _node.comp_list:
        dis = n.distance(_node.center)
        if(dis < min_dis):
            min_dis = dis
            min_comp = n
    return min_comp, min_dis


def trade_off_calculation(_list, _nlist):
    if(len(_list) == 0):
        for n in _nlist:
            n.compute_trade_off()
    else:
        for n in _list:
            n.compute_trade_off()

    # Input: Node i, Node j
    # Output: True if accept, otherwise False


def weight_condition(_nodei, _nodej, W):
    # code here
    comp_wi = compute_weight(_nodei)
    comp_wj = compute_weight(_nodej)
    w = comp_wi + comp_wj
    if(w <= W):
        return True
    else:
        return False


def compute_weight(_node):
    complist = _node.get_complist()
    if (complist is None):
        raise TypeError("Error: complist[]!")
    weight = 0
    if(len(complist) != 0):
        for n in complist:
            weight += n.get_weight()
    return weight

# Input: Node, MAX_STEP
# Output: True/False


def jump_condition(_nodei, _nodej, steps=MAX_STEP):
    if(_nodej.get_level() < steps):
        if(guess_level(_nodei, _nodej.get_level()) <= steps):
            return True
    return False


def guess_level(_node, pre_level):
    max_level = 0
    _level = _node.get_level()
    delta = pre_level + 1 - _level
    guess_level = _level + delta
    if (guess_level > max_level):
        max_level = guess_level
    all_children = get_all_children_of(_node)
    if (len(all_children) != 0):
        for child in all_children:
            _lv = child.get_level()
            guess_lv = _lv + delta
            if (guess_lv > max_level):
                max_level = guess_lv
    return max_level
    # Tinh buoc nhay cua _node


# Ghép


def connect_link(axes, _nodei, _nodej):
    # Un-visulize
    unlink(axes, _nodei)
    # Make _nodei as subroot
    make_subtree_of(_nodei)
    # Update _nodei: center, level, parent
    _nodei.set_center(_nodej.get_center())
    new_level = _nodej.get_level() + 1
    delta = new_level - _nodei.get_level()
    _nodei.set_level(new_level)
    _nodei.update_parent(_nodej)
    # Update all_children: center & level
    _list = get_all_children_of(_nodei)
    for n in _list:
        n.set_center(_nodej.get_center())
        old_level = n.get_level()
        n.set_level(old_level + delta)
    draw_nlink(axes, _nodei, _nodej)

# Un-visualize


def unlink(axes, _nodei):
    _1th_level_parent = None
    if(_nodei.get_level() == 0):
        raise TypeError("Error: Node level = 0!")
    elif(_nodei.get_level() == 1):
        _1th_level_parent = _nodei
    else:
        _1th_level_parent = get_ith_level_parent_from_child(_nodei, 1)
    if(_1th_level_parent == None):
        raise TypeError("Error: Parent node = None!")
    remove_link(axes, _1th_level_parent, _1th_level_parent.center)

# Bỏ


def ignore_link(_nodei, _nodej):
    # Change nonlink
    _nodei.add_to_nonlink(_nodej)
    _nodej.add_to_nonlink(_nodei)


def finish_algorithm():
    my_show()


def is_finish_algorithm(_nlist):
    end = True
    for n in _nlist:
        if(n.trade_off is None or n.trade_off < 0):
            end = False
            break
    return end


def update_considering_nodes_list(_nodei):
    _list = _nodei.get_complist()
    return _list


def MCEW(axes, _nlist):
    considering_nodes_list = []
    while(not is_finish_algorithm(_nlist)):
        find_neighbor(considering_nodes_list, _nlist)
        trade_off_calculation(considering_nodes_list, _nlist)
        _nodei, min_tradeoff = min_trade_off(_nlist)
        _nodej = _nodei.neighbor
        mark_node_ij(axes, _nodei, _nodej)
        if(weight_condition(_nodei, _nodej, W)
                and jump_condition(_nodei, _nodej, MAX)):  # jump = vo cung
            connect_link(axes, _nodei, _nodej)
        else:
            ignore_link(_nodei, _nodej)
        remove_mark(axes, _nodei, _nodej)
        considering_nodes_list = update_considering_nodes_list(_nodei)
    finish_algorithm()
