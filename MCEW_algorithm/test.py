# -*- coding: utf-8 -*-
import csv
from my_constant import *
from my_logic import *
from my_visualize import *
PATH = 'test_points.csv'


def main():
    point_list = []
    blist = []
    nlist = []
    b_index = [5, 9]
    n1_index = [0, 7]
    n2_index = [3, 5]
    n3_index = [13]
    x_max = 30
    y_max = 30
    n_index = [n1_index, n2_index, n3_index]

    # Create a plane
    fig, ax = create_plane(x_max, y_max)

    # Create and save a list
    # point_list = create_random_points(15, x_max, y_max)
    # save_point_list_into_csv_file(point_list, PATH)
    
    # Get list from existing csv file
    point_list = get_point_list(PATH)
    
    # Test
    # blist, nlist = create_and_visualize_blist_nlist_test(ax, point_list)

    # Create blist, nlist
    blist, nlist = create_and_visualize_blist_nlist(ax, point_list,
                                                    b_index, n_index)
    # Find neighbors
    find_S(ax, blist, nlist)
    
    # MCEW algorithm
    MCEW(ax, nlist)


if __name__ == '__main__':
    main()
