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
                 neighbor=None, neighbor_dis=-1, trade_off=None):
        super().__init__(x, y)
        self.w = w
        self.center = center  # Backbone
        self.center_dis = center_dis
        self.neighbor = neighbor
        self.neighbor_dis = neighbor_dis
        self.path = []
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
        if(other_node not in self.comp_list):
            self.comp_list.append(other_node)
        if(len(other_node.comp_list) != 0):
            for n in other_node.comp_list:
                if(n not in self.comp_list):
                    self.comp_list.append(n)

    def change_path(self, first_point):
        self.path = [first_point]
        self.path += first_point.path

    def compute_trade_off(self):
        cost_ij = round(0.3 * self.distance(self.neighbor))
        min_node, min_component_cost = comp_cost(self)
        self.trade_off = cost_ij - min_component_cost  # Thoa hiep duoc tinh toan o day


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

# Creat bachbone_list, node_list from point_list, set weight cho cac node
# vẽ các node và backbone lên mặt phẳng
# Input: point_list
# Output: b_list, n_list

# test: 10 Points


def create_and_visualize_blist_nlist_test(_axes, _list):
    b_list = []
    n_list = []
    b_index = [2, 8]
    n1_index = [3, 6, 9]
    n2_index = [4, 11, 12]
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


def create_and_visualize_blist_nlist(_axes1, _axes2, _list):
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
            visualize_backbone(_axes1, x, y)
            visualize_backbone(_axes2, x, y)
            
        else:
            visualize_node(_axes1, x, y)
            visualize_node(_axes2, x, y)
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


def find_S(_axes1, _axes2, _blist, _nlist):
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
        n.path.append(backbone_of_n)
        draw_slink(_axes1, n, backbone_of_n)  # gọi hàm không có axes
        draw_slink(_axes2, n, backbone_of_n)
        backbone_of_n.S.append(n)

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

# Input: Node, MAX_STEP
# Output: True/False


def jump_condition(_node, MAX_STEP):
    if(compute_jumpstep(_node) < MAX_STEP):
        return True
    else:
        return False

# Tinh buoc nhay cua _node


def compute_jumpstep(_node):
    return len(_node.path)

# Ghép


def connect_link(axes, _nodei, _nodej):
    draw_nlink(axes, _nodei, _nodej)
    update_nodei(axes, _nodei, _nodej)
    update_nodej(_nodei, _nodej)

# Cập nhât thông tin nodei theo nodej


def update_nodei(_axes, _nodei, _nodej):
    _nodei.center = _nodej.center  # Gán center(i) = center(j)
    _nodei.center_dis = _nodei.distance(
        _nodei.center)  # Tính lại KC đến center mới
    # Update path cua _nodei
    path_old_i = _nodei.path
    _nodei.change_path(_nodej)
    if (len(path_old_i) == 1 and isinstance(path_old_i[0], Backbone)):
        # Nếu path chứa mỗi Backbone thì remove ngay
        remove_link(_axes, _nodei, path_old_i[0])
    else:
        # Update path của các node trên path từ i về center_old(i)
        for i in range(len(path_old_i) - 1):
            if(i == 0):
                path_old_i[0].change_path(_nodei)
            else:
                path_old_i[i].change_path(path_old_i[i-1])
            if(path_old_i[i] == path_old_i[-2]):
                # Remove link giữa node gần backbone nhất và backbone
                remove_link(_axes, path_old_i[i], path_old_i[i].center)
    for n in _nodei.comp_list:
        n.update_component_list(_nodej)
        n.center = _nodei.center
        n.center_dis = n.distance(n.center)
    _nodei.update_component_list(_nodej)  # Thêm j vào comp_list của i



def update_nodej(_nodei, _nodej):
    for n in _nodej.comp_list:
        n.update_component_list(_nodei)
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


def finish_algorithm():
    my_show()


def is_finish_algorithm(_nlist):
    end = True
    for n in _nlist:
        if(n.trade_off is None or n.trade_off < 0):
            end = False
            break
    return end


def update_considering_nodes_list(_nodei, _nodej):
    _list = []
    _list = [_nodei, _nodej]
    _list += _nodei.comp_list
    _list += _nodej.comp_list
    return _list


def MCEW(axes, _nlist):
    considering_nodes_list = []
    while(not is_finish_algorithm(_nlist)):
        find_neighbor(considering_nodes_list, _nlist)
        trade_off_calculation(considering_nodes_list, _nlist)
        _nodei, min_tradeoff = min_trade_off(_nlist)
        visualize_considering_node(axes, _nodei.x, _nodei.y)
        _nodej = _nodei.neighbor
        if(weight_condition(_nodei, _nodej, W)
                and jump_condition(_nodei, MAX)):  # jump = vo cung
            connect_link(axes, _nodei, _nodej)
        else:
            ignore_link(_nodei, _nodej)
        considering_nodes_list = update_considering_nodes_list(_nodei, _nodej)
    finish_algorithm()