# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from my_constant import *


# create a plane contains backbones, nodes
# Input: backbone_list, node_list
def create_plane():
    # code here
    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Set the limits of the subplot
    ax.set_xlim(0, X_MAX)
    ax.set_ylim(0, Y_MAX)
    
    return fig, ax

# create a point
# Input: ( x, y)
#def create_point( _axes, _x, _y):
    # code here
    
    
def visualize_node( _axes, _x, _y):
    _axes.plot(_x, _y, 'ok')

def visualize_considering_node( _axes, _x, _y):
    _axes.plot(_x, _y, 'og')
    
def visualize_backbone( _axes, _x, _y):
    _axes.plot(_x, _y, 'or')

def draw_link( _axes, _point1, _point2):
    _axes.plot([_point1.x, _point2.x], [_point1.y, _point2.y], 'k-')
    
#def remove_link(_point1, _point2):
    