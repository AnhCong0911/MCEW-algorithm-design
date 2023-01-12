import random
import csv
from my_constant import *
from my_logic import *
from my_visualize import *

def create_plane(x_max=X_MAX, y_max=Y_MAX):
    # code here
    # Create a figure and a subplot
    fig, ax = plt.subplots()

    # Set the limits of the subplot
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    
    return fig, ax
A = [0, 1, 2, 3, 4, 5]
del A[4:]
print(A)