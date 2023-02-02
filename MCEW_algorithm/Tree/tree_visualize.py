# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from tree_constant import *


# create a plane contains backbones, nodes
# Input: backbone_list, node_list
def create_plane(x_max=X_MAX, y_max=Y_MAX):
    # code here
    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Set the limits of the subplot
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)

    return fig, ax


def visualize_node(_axes, _x, _y):
    _axes.plot(_x, _y, 'ok')


def mark_node_ij(_axes, _nodei, _nodej):
    visualize_considering_nodei(_axes, _nodei.x, _nodei.y)
    visualize_considering_nodej(_axes, _nodej.x, _nodej.y)


def remove_mark(_axes, _nodei, _nodej):
    visualize_node(_axes, _nodei.x, _nodei.y)
    visualize_node(_axes, _nodej.x, _nodej.y)


def visualize_considering_nodei(_axes, _x, _y):
    _axes.plot(_x, _y, 'oy')


def visualize_considering_nodej(_axes, _x, _y):
    _axes.plot(_x, _y, 'om')


def visualize_backbone(_axes, _x, _y):
    _axes.plot(_x, _y, 'or')


def draw_slink(_axes, _point1, _point2):
    _axes.plot([_point1.x, _point2.x], [_point1.y, _point2.y], 'g-')


def draw_nlink(_axes, _point1, _point2):
    _axes.plot([_point1.x, _point2.x], [_point1.y, _point2.y], 'b-')

# Xóa visulize giữa hai node


def remove_link(_axes, _nodei, _nodej):
    _axes.plot([_nodei.x, _nodej.x], [_nodei.y, _nodej.y], 'w-')
    _axes.plot(_nodei.x, _nodei.y, 'ok')
    _axes.plot(_nodej.x, _nodej.y, 'or')


def my_show():
    plt.show()
