# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:47:21 2024

@author: Sehyun
"""

import numpy as np
import robodk.robomath as rm
from time import sleep
from math_tool import matrix_T, inv


def matrix_calc_k(x,y,z):

    translation = np.array([-412.46, -482.2, 344.68])

    UR_RF_T = matrix_T([60,0,0], translation)
    # print(UR_MS_T)
    RF_GG_T = np.array([[0, 0, -1, -11.8461],
                        [0, 1, 0, 68.6781],
                        [1, 0, 0, -142.55],
                        [0, 0, 0, 1]])
        # Vector to add
    shift = np.array([x, y, z])
    
    # Add the vector to the last entries in the first three rows
    RF_GG_T[:3, 3] += shift
    
    RA_GG_T = np.array([[1, 0, 0, 27.22],
                        [0, 1, 0, 0],
                        [0, 0, 1, 147.6],
                        [0, 0, 0, 1]])


    # Stack the rotation matrix and translation vector horizontally
    TCP_RA_T = matrix_T([-50,-2.6,0], np.zeros((3, 1)))
    
    return rm.Mat((UR_RF_T @ RF_GG_T @ inv(RA_GG_T) @ inv(TCP_RA_T)).tolist())


def task_k(robot):
    IP = [-21.890000, -92.730000, 149.060000, -52.630000, 0, -222.620000]
    robot.MoveJ(IP)
    
    L1_standoff = matrix_calc_k(0,0,-50)
    robot.MoveJ(L1_standoff)
    sleep(1)
    
    L1 = matrix_calc_k(0,0,0)
    robot.MoveJ(L1)

    
    sleep(5)
    
    L2 = matrix_calc_k(25,0,0)
    robot.MoveJ(L2)
    sleep(1)
    


    
def task_r(robot):
    L2 = matrix_calc_k(25,0,0)
    robot.MoveJ(L2)
    sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    