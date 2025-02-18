# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:04:35 2024

@author: Sehyun
"""

import numpy as np
import robodk.robomath as rm
from time import sleep
from math_tool import matrix_T, inv

def matrix_calc_g(x,y,z):
    
    UR_WDT_T= np.array([[-1, 0, 0, 590],
                    [0, -1, 0, -100],
                    [0, 0, 1, 85],
                    [0, 0, 0, 1]])

    WDT_PORTA_T = np.array([[0, 0, -1, 0],
                        [0, 1, 0, 0],
                        [1, 0, 0, 30],
                        [0, 0, 0, 1]])
    
    WDT_PORTA_T[:3,3] += np.array([x,y,z])
    
    RA_PORTA_T = matrix_T(([0,-2.6,0]), np.array([27.22, 0, 147.6]))
    TCP_RA_T = matrix_T(([-50,0,0]), np.zeros((3, 1)))
    print("TCP::", TCP_RA_T)
    return rm.Mat((UR_WDT_T @ WDT_PORTA_T @ inv(RA_PORTA_T) @ inv(TCP_RA_T)).tolist())
    
def task_g(robot):
    
    IP = [-213.395889, -92.856110, 132.343587, 
          -42.394857, 116.574574, -221.301546]
    robot.MoveJ(IP)

    L1_standoff = matrix_calc_g(0,0,100)
    
    robot.MoveJ(L1_standoff)
    sleep(1)
    
    L1 = matrix_calc_g(0, 0, 28.57)
    robot.MoveL(L1)
    # sleep(1)
    
def task_i(robot):
    L1_standoff = matrix_calc_g(0,0,100)
    
    robot.MoveJ(L1_standoff)
    
    sleep(1)
    
    IP = [-240.810000, -87.570000, 145.950000, -65.680000, 43.780000, -220.000000]
    robot.MoveJ(IP)
    
    sleep(1)