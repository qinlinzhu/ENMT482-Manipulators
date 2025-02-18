from robodk.robolink import *
import robodk.robomath as rm
from math_tool import *
import numpy as np
import robodk.robomath as rm
RDK = Robolink()

TCP_T_MA = np.array([[0.643, 0.766, 0, 0],
                      [-0.766, 0.643, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

CFF_T_closed = np.array([[1,0,0,-53.5],
                        [0,1,0,0],
                        [0,0,1,186.62],
                        [ 0,0,0,1,]])

UR_T_CD = np.array([[0, 0, -1, -590],
                    [0, 1, 0, -221],
                    [1, 0, 0, 212],
                    [0, 0, 0, 1]])

UR_T_RS_matrix = np.array([[-0.5, 0.866, 0, -365.1],
                            [-0.866, -0.5, 0, -285.74],
                            [0, 0, 1, 30],
                            [0, 0, 0, 1]])

RS_T_PAN = np.array([[-1, 0, 0, 205.6655],
                    [0, -1, 0, -11.463],
                    [0, 0, 1, 60],
                    [0, 0, 0, 1]])

CD_D_PB = np.array([-100, 71, 32.5]) 
CD_T_PB = matrix_T([0,0,0], CD_D_PB)
CD_D_PB1 = CD_D_PB + np.array([0, 0, -182.5])
CD_T_PB1= matrix_T([0,0,0], CD_D_PB1)
L1 = rm.Mat((UR_T_CD @ CD_T_PB1 @ inv(CFF_T_closed) @ inv(TCP_T_MA)).tolist())
L2 = rm.Mat((UR_T_CD @ CD_T_PB @ inv(CFF_T_closed) @ inv(TCP_T_MA)).tolist())
L3 = rm.Mat((UR_T_RS_matrix @ RS_T_PAN @ inv(CFF_T_closed) @ inv(TCP_T_MA)).tolist())

CUP_ST = ([-143.040000, -86.790000, -131.790000, -146.360000, -113.320000, -219.990000])
Ran_cup = ([-134.180000, -91.390000, -123.750000, -144.880000, -103.160000, -219.990000])

CZ_ST = ([-194.460000, -86.790000, -143.040000, -128.570000, -114.850000, -220.000000])
CZ_zone = ([-188.040000, -106.070000, -123.750000, -126.960000, -93.210000, -220.000000])

def tasks_cup(robot): # Pick up cup from cup dispenser
    robot.MoveJ(L1)
    robot_program = RDK.Item('Cup_Tool_Open_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    robot.MoveL(L2)

    robot_program = RDK.Item('Cup_Tool_Close_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    robot.MoveL(L1)
    robot.MoveJ(CUP_ST)
    robot.MoveJ(Ran_cup)
    robot_program = RDK.Item('Cup_Tool_Open_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    robot.MoveL(CUP_ST)

    robot_program = RDK.Item('Cup_Tool_Close_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()



def customer_zone(robot): # Place cup in customer zone, then return cup tool
    robot_program = RDK.Item('Cup_Tool_Open_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    robot.MoveJ(CUP_ST)
    robot.MoveJ(L3)
    robot_program = RDK.Item('Cup_Tool_Close_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    robot.MoveJ(CZ_ST)

    robot.MoveL(CZ_zone)

    robot_program = RDK.Item('Cup_Tool_Open_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    robot.MoveL(CZ_ST)

    robot_program = RDK.Item('Cup_Tool_Close_(UR5)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()