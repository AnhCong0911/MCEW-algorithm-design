from my_constant import *
import math

class Backbone:
    def __init__(self, x, y, deep=MAX, level=0):
        self.x = x
        self.y = y
        self.children = []
        self.deep = deep
        self.level = level
    
    def add_child(self, child):
        child.level = self.level + 1 # Change level
        child.parent = self
        self.children.append(child)
        
    def visualize_root(self):
        
    
    def visualize_tree():
        a =1
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
class Node(Backbone):
    def __init__(self, x, y, w=1, parent=None, center=None, level,
                 neighbor=None, trade_off=None):
        super().__init__(x, y)
        self.w = w
        self.parent = parent
        self.center = center  # Backbone
        self.level = level # Create level
        self.neighbor = neighbor
        self.nonlink_checked_neighbor = []  # list of neighbor is checked
        self.trade_off = trade_off
        # self.comp_list = []  # list of Node
    
    def get_parent():
        
    def compute_tradeoff():
        
    def update_level():
        
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
        
