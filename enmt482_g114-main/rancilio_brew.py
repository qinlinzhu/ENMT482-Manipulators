from robodk.robolink import *
import robodk.robomath as rm
from math_tool import *
import numpy as np
import robodk.robomath as rm
from time import sleep
RDK = Robolink()

TCP_T_MA = np.array([[0.643, 0.766, 0, 0],
                      [-0.766, 0.643, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

MA_T_PB = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 102.82],
                     [0, 0, 0, 1]])

UR_T_RF = np.array([[0.5, -0.866, 0, -412.46],
                    [0.866, 0.5, 0, -482.2],
                    [0, 0, 1, 344.68],
                    [0, 0, 0, 1]])


RF_D_PB = np.array([49.72, 38.6825, -50.46]) 
RF_T_PB = matrix_T([0,-90,0], RF_D_PB)

RF_ST_PB = np.array([149.72, 38.6825, -50.46])
RF_ST_PB = matrix_T([0,-90,0], RF_ST_PB)

RF_ST2_PB = np.array([69.72, 38.6825, -66.46])
RF_ST2_PB = matrix_T([0,-90,0], RF_ST2_PB)

RF_P_PB = np.array([49.72, 38.6825, -66.46])
RF_P_PB = matrix_T([0,-90,0], RF_P_PB)


L1 = rm.Mat((UR_T_RF @ RF_ST_PB@ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L2 = rm.Mat((UR_T_RF @ RF_T_PB @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L3 = rm.Mat((UR_T_RF @ RF_ST2_PB @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L5 = rm.Mat((UR_T_RF @ RF_P_PB @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L6 = rm.Mat((UR_T_RF @ RF_ST_PB@ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())

def Brew(robot):
    robot.MoveL(L1)
    robot.MoveL(L2)
    robot.MoveL(L3)
    sleep(7)
    robot.MoveL(L5)
    robot.MoveL(L6)
   
def Brew2(robot):
    robot.MoveL(L1)
    robot.MoveL(L2)
    robot.MoveL(L3)
    sleep(5)
    robot.MoveL(L5)
    robot.MoveL(L6)
    
