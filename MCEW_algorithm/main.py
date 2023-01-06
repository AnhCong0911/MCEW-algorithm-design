# -*- coding: utf-8 -*-
import random
import csv
from my_constant import *
from my_logic import *
from my_visualize import *

point_list = []
blist = []
nlist = []

def main():
    fig, ax = create_plane()
    point_list = create_random_points()
    save_point_list_into_csv_file(point_list)
    blist, nlist = create_and_visualize_blist_nlist(point_list)
    find_S(blist, nlist)
    
    

