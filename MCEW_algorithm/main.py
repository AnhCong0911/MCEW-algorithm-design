# -*- coding: utf-8 -*-
import random
import csv
import matplotlib.pyplot as plt
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

    MCEW(ax, nlist)


if __name__ == '__main__':
    main()
