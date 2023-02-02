# from tree_constant import *
# from tree_logic import *
# import math


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def get(self):
#         return (self.x, self.y)

#     def set(self, x, y):
#         self.x = x
#         self.y = y


# class Backbone:
#     def __init__(self, x, y, deep=MAX, level=0):
#         self.x = x
#         self.y = y
#         self.children = []
#         self.deep = deep
#         self.level = level

#     def add_child(self, child):
#         child.level = self.level + 1  # Change level
#         child.parent = self
#         if(child.level == 1):
#             child.center = self
#         else:
#             child.center = self.center
#         self.children.append(child)

#     def get_children(self):
#         return self.children

#     def get_level(self):
#         return self.level

#     def set_level(self, level):
#         self.level = level

#     def distance(self, other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return math.sqrt(dx**2 + dy**2)


# class Node(Backbone):
#     def __init__(self, x, y, w=1, parent=None, center=None,
#                  neighbor=None, trade_off=None):
#         super().__init__(x, y)
#         self.w = w
#         self.parent = parent
#         self.center = center  # Backbone
#         self.neighbor = neighbor
#         self.nonlink_checked_neighbor = []  # list of neighbor is checked
#         self.trade_off = trade_off

#     def get_weight(self):
#         return self.w

#     def get_parent(self):
#         return self.parent

#     def set_parent(self, parent):
#         self.parent = parent

#     def update_parent(self, parent):
#         self.set_parent(parent)
#         parent.get_children().append(self)

#     def get_center(self):
#         return self.center

#     def set_center(self, center):
#         self.center = center

#     def set_neighbor(self, neighbor):
#         self.neighbor = neighbor

#     def get_nonlink(self):
#         return self.nonlink_checked_neighbor

#     def add_to_nonlink(self, _node):
#         self.nonlink_checked_neighbor.append(_node)

#     # def update_level():

#     def find_neighbor_of_node(self, _nlist):
#         temp1 = []
#         temp1 = self.get_complist() + self.nonlink_checked_neighbor  # nonlink_checked_neighbor
#         temp1.append(self)
#         temp2 = [i for i in _nlist if i not in set(temp1)]
#         # code here
#         neighbor_of_node = None
#         neighbor_distance = MAX
#         for n in temp2:
#             dis = self.distance(n)
#             if(dis < neighbor_distance):
#                 neighbor_distance = dis
#                 neighbor_of_node = n
#         self.neighbor = neighbor_of_node  # Create neighbor

#     # Create Tradeoff
#     def compute_trade_off(self):
#         cost_ij = round(0.3 * self.distance(self.neighbor))
#         _1th_level_parent = get_ith_level_parent_from_child(self, 1)
#         # center created from findS
#         comp_cost = round(0.3 * _1th_level_parent.distance(self.center))
#         self.trade_off = cost_ij - comp_cost  # Thoa hiep duoc tinh toan o day

#     # Get complist
#     def get_complist(self):
#         _1th_level_parent = None
#         if(self.get_level() == 0):
#             raise TypeError("Error: Node level = 0!")
#         if(self.get_level() == 1):
#             _1th_level_parent = self
#         else:
#             _1th_level_parent = get_ith_level_parent_from_child(self, 1)
#         if(_1th_level_parent == None):
#             raise TypeError("Error: Parent node = None!")
#         complist = get_all_children_of(_1th_level_parent)
#         complist.append(_1th_level_parent)
#         return complist
