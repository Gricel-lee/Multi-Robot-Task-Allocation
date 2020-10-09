"""
Probabilistic Road Map (PRM) Planner
author: Atsushi Sakai (@Atsushi_twi)
"""
from probabilistic_road_map import *
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree

# parameter
N_SAMPLE = 500  # number of sample_points
N_KNN = 10  # number of edge from one sampled point
MAX_EDGE_LEN = 30.0  # [m] Maximum edge length

show_animation = True


def prm():

    # start and goal position
    sx = 5.0  # [cm]
    sy = 5.0  # [cm]
    gx = 25.0  # [cm]
    gy = 55.0  # [cm]
    robot_size = 1.0  # [cm]

    # Define obstacles 

    ox = []
    oy = []

    for i in range(41):	#low
        ox.append(i)
        oy.append(0.0)
    for i in range(41):	#top
        ox.append(i)
        oy.append(61.0)
    for i in range(61):	#right
    	ox.append(0.0)
    	oy.append(i)	
    for i in range(61):	#left
        ox.append(40.0)
        oy.append(i)
    for i in range(10):	#cell C1C5
        ox.append(i)
        oy.append(10)
    for i in range(10):	#cell C5C9
        ox.append(i)
        oy.append(20)
    for i in range(10):	#cell C9C13
        ox.append(i)
        oy.append(30)
    for i in range(10):	#cell C13C17
        ox.append(i)
        oy.append(40)
    for i in range(10):	#cell C17C21
        ox.append(i)
        oy.append(50)
    for i in range(29,40):	#cell C4C8
        print(i)
        ox.append(i)
        oy.append(10)
    for i in range(29,40):	#cell C12C16
        ox.append(i)
        oy.append(30)
    for i in range(29,40):	#cell C20C4
        ox.append(i)
        oy.append(50)



    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "^r")
        plt.plot(gx, gy, "^c")
        plt.grid(True)
        plt.axis("equal")
        

    rx, ry = prm_planning(sx, sy, gx, gy, ox, oy, robot_size)
    print(rx,ry)

    assert rx, 'Cannot found path'

    print("Travelling cost is ", cost(rx, ry))

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()
    plt.pause(3.001)

def main():
    print(__file__ + " start!!")
    prm()


if __name__ == '__main__':
    main()

#main1()