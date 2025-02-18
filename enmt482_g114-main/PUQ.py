from math_tool import matrix_T, inv
import numpy as np
import robodk.robomath as rm
from time import sleep
import numpy as np


def matrix_calc_j(x,y,z):

    translation = np.array([386.92, 86.92, 267.42])
    UR_PUQ_T = matrix_T([-135,0,0], translation)

    # UR_PUQ_T= np.array([[-0.707, 0.707, 0, 386.92],
    #                     [-0.707, -0.707, 0, 86.92],
    #                     [0, 0, 1, 267.42],
    #                     [0, 0, 0, 1]])

    PUQ_TFC_T = np.array([[0, 0, -1, 12.5582],
                        [0, 1, 0, 0.5091],
                        [1, 0, 0, -131.33],
                        [0, 0, 0, 1]])

    shift = np.array([x,y,z])
    PUQ_TFC_T[:3, 3] += shift
    RA_PUQ_T = np.array([[1, 0, 0, 27.22],
                        [0, 1, 0, 0],
                        [0, 0, 1, 147.6],
                        [0, 0, 0, 1]])


    TCP_RA_T = matrix_T([-50,-2.6,0], np.zeros((3, 1)))

    # Stack the rotation matrix and translation vector horizontally
    return rm.Mat((UR_PUQ_T @ PUQ_TFC_T @ inv(RA_PUQ_T) @ inv(TCP_RA_T)).tolist())
    

def task_j(robot):

    L1_standoff = matrix_calc_j(100, 0, -10)
    robot.MoveJ(L1_standoff)
    sleep(1)
    
    
    L1 = matrix_calc_j(0, 0, -10) 
    robot.MoveL(L1)
    sleep(2)
    
    L1_standoff = matrix_calc_j(200, 0, -10)
    robot.MoveL(L1_standoff)
    sleep(1)
    