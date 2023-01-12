
class Root:
    def __init__(self, x, y, deep, level=0):
        self.x = x
        self.y = y
        self.children = []
        self.deep = deep
        self.level = level
    
    def add_child(self, child):
        child.level = self.level - 1
        child.parent = self
        self.children.append(child)
    
    def visualize_tree():
        a =1
    
class Node(Root):
    def __init__(self, x, y):
        self.w = w
        self.parent = None
        self.center = center  # Backbone
        self.center_dis = center_dis
        self.neighbor = neighbor
        self.neighbor_dis = neighbor_dis
        self.nonlink_checked_neighbor = []  # list of neighbor is checked
        self.path = []
        self.changed_path = changed_path
        self.comp_list = []  # list of Node
        self.trade_off = trade_off
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
