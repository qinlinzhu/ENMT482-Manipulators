# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 04:46:20 2024

@author: Sehyun
"""


import numpy as np
import robodk.robomath as rm
from time import sleep
from math_tool import *

    
def matrix_calc_a(x,y,z):
    Rp = R_z(-60)
    translation = np.array([412.62, -234.06, 30])
    UR_MS_T = np.hstack((Rp, translation.reshape(3,1)))
    homogeneous_row = np.array([[0,0,0,1]])
    UR_MS_T = np.vstack((UR_MS_T, homogeneous_row))
    # print(UR_MS_T)
    MS_BB_T = np.array([[0, 0, 1, 37.278],
                        [0, -1, 0, -14.4326],
                        [1, 0, 0, 13.73],
                        [0, 0, 0, 1]])
        # Vector to add
    shift = np.array([x, y, z])
    
    # Add the vector to the last entries in the first three rows
    MS_BB_T[:3, 3] += shift
    
    BB_RA_T = np.array([[1, 0, 0, -32],
                        [0, 1, 0, 0],
                        [0, 0, 1, 28.07],
                        [0, 0, 0, 1]])
    Rz = R_z(-50)
    translation = np.zeros((3, 1))

    # Stack the rotation matrix and translation vector horizontally
    TCP_RA_T = matrix_T([-50,-2.6,0], np.zeros((3, 1)))
    
    return rm.Mat((UR_MS_T @ MS_BB_T @ inv(BB_RA_T) @ inv(TCP_RA_T)).tolist())

def task_a(robot):
    
    
    
    L1_standoff = matrix_calc_a(-80, 0, 0)
    L1 = matrix_calc_a(0,0,0)
    
    
    IP = [-238.380000, -63.240000, -53.950000, -126.490000, 279.730000, -9.410000]
    robot.MoveJ(IP)
    sleep(1)

    IP = [-182.430000, -136.220000, 136.220000, 7.300000, 150.810000, -214.050000]
    robot.MoveJ(IP)
    sleep(1)
    
     
    robot.MoveJ(L1_standoff)
    sleep(1)
    # L1 = 
    robot.MoveL(L1)
    sleep(1)
    

    print("new:",L1)
    
    """
    DETACH RANCILIO TOOL
    """
    
def task_ab(robot):
    L1_standoff = matrix_calc_a(-80, 0, 10)
    robot.MoveJ(L1_standoff)
    sleep(1)
    
    IP = [-228.840000, -107.030000, 155.680000, 
          -54.530000, 86.570000, -220.100000]
    robot.MoveL(IP)
    sleep(1)
    
    IP = [-216.490000, -114.320000, 70.540000, 
          -56.660000, 114.700000, -219.990000]
    robot.MoveJ(IP)
    sleep(1)
    
def matrix_calc_b(x, y, z):
    
    
    UR_MS_T = np.array([[0.5, 0.866, 0, 412.62],
                        [-0.866, 0.5, 0, -234.06],
                        [0, 0, 1, 30],
                        [0, 0, 0, 1]])
    
    
    shift = np.array([x,y,z])
    D = np.array([76.5, -49.1, -9.2]) 
    MS_P2_T = matrix_T([0, 180, -45], D)

    
    
    # Add the vector to the last entries in the first three rows
    MS_P2_T[:3, 3] += shift
    P2_MA_T = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 102.82],
                        [0, 0, 0, 1]])

    
    TCP_MA_T = matrix_T([-50,0,0], np.zeros((3, 1)))
    
    print(TCP_MA_T)
    return rm.Mat((UR_MS_T @ MS_P2_T @ inv(P2_MA_T) @ inv(TCP_MA_T)).tolist())
    
def task_b(robot):
    

    IP = [-228.650000, -107.030000, 145.950000, -53.980000, 87.570000, -220.000000]
    robot.MoveJ(IP)
    sleep(1)
    
    IP = [-255.410000, -92.430000, 131.350000, -128.750000, -45.860000, -233.970000]

    robot.MoveJ(IP)
    sleep(1)
    
    L1_standoff = matrix_calc_b(15, 0, 0)
    robot.MoveL(L1_standoff)
    sleep(1)
    
    L1 = matrix_calc_b(-20, 0, 0)
    robot.MoveL(L1)
    sleep(1)
    
    L2 = matrix_calc_b(-20,0,-5)
    robot.MoveL(L2)
    sleep(1)
    
    L3 = matrix_calc_b(-20,0,20)
    robot.MoveL(L3)
    sleep(1)
    
    L4 = matrix_calc_b(-20,-100,100)
    robot.MoveL(L4)
    sleep(1)
    
    
    

def task_e(robot):
    IP = [-255.410000, -92.430000, 131.350000, -128.750000, -45.860000, -233.970000]

    robot.MoveJ(IP)
    sleep(1)
    
    L1_standoff = matrix_calc_b(-20, 0, 0)
    robot.MoveL(L1_standoff)
    sleep(1)
    
    L1 = matrix_calc_b(20, 0, 0)
    robot.MoveL(L1)
    sleep(1)
    
    L2 = matrix_calc_b(20,0,-5)
    robot.MoveL(L2)
    sleep(1)
    
    L3 = matrix_calc_b(20,0,20)
    robot.MoveL(L3)
    sleep(1)
    
    L4 = matrix_calc_b(20,-100,100)
    robot.MoveL(L4)
    sleep(1)
    
def task_ef(robot):
    IP = [-250.540000, -136.220000, 131.350000, -136.220000, -48.590000, -348.150000]
    
    robot.MoveL(IP)
    sleep(1)
    
    IP = [-267.570000, -114.320000, 85.140000, -136.220000, -48.590000, -348.150000]
    
    robot.MoveL(IP)
    sleep(1)
    
    
    IP = [-62.020000, -65.680000, -45.880000, -118.590000, 76.060000, -198.290000]
    
    robot.MoveJ(IP)
    sleep(1)
    
    
def task_f(robot):
    IP = [-238.380000, -63.240000, -53.950000, -126.490000, 279.730000, -9.410000]
    robot.MoveJ(IP)
    sleep(1)
    
    IP = [-219.190000, -114.320000, 138.650000, -194.590000, 249.190000, -40.000000]
    robot.MoveJ(IP)
    sleep(1)
    
    IP = [-209.190000, -128.920000, 131.350000, -12.160000, 111.890000, -214.050000]
    robot.MoveJ(IP)
    sleep(1)
    
    L1_standoff = matrix_calc_a(-80, 0, -5)
    
    L1 = matrix_calc_a(0,0,-5)
    
    L2 = matrix_calc_a(-80, 0, 100)
    
    robot.MoveJ(L1_standoff)
    sleep(1)
    # L1 = 
    robot.MoveL(L1)
    sleep(1)
    
    robot.MoveL(L1_standoff)
    sleep(1)
    
    robot.MoveL(L2)
    sleep(1)
    
    