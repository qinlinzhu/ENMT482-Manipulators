from robodk.robolink import *
import robodk.robomath as rm
from math_tool import inv
import numpy as np
import robodk.robomath as rm
from time import sleep

TCP_T_MA = np.array([[0.643, 0.766, 0, 0],
                      [-0.766, 0.643, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

MA_T_PB = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 102.82],
                     [0, 0, 0, 1]])

UR_T_CD = np.array([[0, 0, -1, -590],
                    [0, 1, 0, -221],
                    [1, 0, 0, 212],
                    [0, 0, 0, 1]])

CD_T_closed = np.array([[1, 0, 0, -8.95],
                      [0, 1, 0, 71.48],
                      [0, 0, 1, -39.83],
                      [0, 0, 0, 1]])

CD_T_open = np.array([[1, 0, 0, -8.95],
                      [0, 1, 0, 71.9],
                      [0, 0, 1, -74.65],
                      [0, 0, 0, 1]])

CD_T_ST = np.array([[1, 0, 0, 30],
                    [0, 1, 0, 71.9],
                    [0, 0, 1, -39.83],
                    [0, 0, 0, 1]])

L1 = rm.Mat((UR_T_CD @ CD_T_ST @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L2 = rm.Mat((UR_T_CD @ CD_T_closed @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L3 = rm.Mat((UR_T_CD @ CD_T_open @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L4 = rm.Mat((UR_T_CD @ CD_T_closed @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())
L5 = rm.Mat((UR_T_CD @ CD_T_ST @ inv(MA_T_PB) @ inv(TCP_T_MA)).tolist())

def cup_dispender(robot):
    robot.MoveJ(L1)
    sleep(1)
    robot.MoveJ(L2)
    sleep(1)
    robot.MoveL(L3)
    sleep(1)
    robot.MoveL(L4)
    sleep(1)
    robot.MoveL(L5)
    sleep(1)
