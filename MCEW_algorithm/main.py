# -*- coding: utf-8 -*-
import random
import csv
from my_constant import *
from my_logic import *
from my_visualize import *


def main():
    point_list = []
    blist = []
    nlist = []
    fig, ax = create_plane()
    # create and save
    # point_list = create_random_points()
    # save_point_list_into_csv_file(point_list)
    # get from existing csv file
    point_list = get_point_list()
    # Test
    blist, nlist = create_and_visualize_blist_nlist_test(ax, point_list)
    
    #blist, nlist = create_and_visualize_blist_nlist(ax, point_list)
    find_S(ax, blist, nlist)
    find_neighbor(nlist)
    for n in nlist:
        n.compute_trade_off()
    _nodei, min_trade = min_trade_off(nlist)
    visualize_considering_node(ax, _nodei.x, _nodei.y)
    _nodej = _nodei.neighbor
    if(weight_condition(_nodei, _nodej, W)
        and jump_condition(_nodei, MAX)):
        connect_link(ax, _nodei, _nodej)
    else:
        ignore_link(_nodei, _nodej)
main()