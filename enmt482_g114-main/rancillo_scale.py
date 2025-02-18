from math_tool import *
import numpy as np
import robodk.robomath as rm
from time import sleep

UR_T_RS_matrix = np.array([[-0.5, 0.866, 0, -365.1],
                            [-0.866, -0.5, 0, -285.74],
                            [0, 0, 1, 30],
                            [0, 0, 0, 1]])


MA_P3_T = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 102.82],
                    [0, 0, 0, 1]])


Rz = R_z(-50)
translation = np.zeros((3, 1))
TCP_RA_T = np.hstack((Rz, translation))
homogeneous_row = np.array([[0, 0, 0, 1]])
TCP_RA_T = np.vstack((TCP_RA_T, homogeneous_row))



MA_R_RS = [90, 200, 20]
RS_D_P3 = np.array([76.5, 21.1, -9.2])
MS_D_MSL1 = RS_D_P3 + np.array([25, 0, 0])
RS_T_P_matrix = matrix_T(MA_R_RS, MS_D_MSL1)
L1 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


MS_D_MSL1 = RS_D_P3 + np.array([-15, 0, 0])
RS_T_P_matrix = matrix_T(MA_R_RS, MS_D_MSL1)
L2 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


MS_D_MSL1 = RS_D_P3 + np.array([-15, 0, -5])
RS_T_P_matrix = matrix_T(MA_R_RS, MS_D_MSL1)
L3 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


MS_D_MSL1 = RS_D_P3 + np.array([-15, 0, 0])
RS_T_P_matrix = matrix_T(MA_R_RS, MS_D_MSL1)
L4 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


def unlock(robot):
    robot.MoveJ(L1)
    sleep(1)
    robot.MoveL(L2)
    sleep(1)
    robot.MoveL(L3)
    sleep(1)
    robot.MoveL(L4)


MS = RS_D_P3 + np.array([-15, 0, 0])
RS_T_P_matrix_lock = matrix_T(MA_R_RS, MS)
LL1 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix_lock @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())

MS = RS_D_P3 + np.array([25, 0, 0])
RS_T_P_matrix_lock = matrix_T(MA_R_RS, MS)
LL2 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix_lock @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())

MS = RS_D_P3 + np.array([25, 0, 0])
RS_T_P_matrix_lock = matrix_T(MA_R_RS, MS)
LL3 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix_lock @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


MS = RS_D_P3 + np.array([25, 0, -5])
RS_T_P_matrix_lock = matrix_T(MA_R_RS, MS)
LL4 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix_lock @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())


MS = RS_D_P3 + np.array([25, 0, 0])
RS_T_P_matrix_lock = matrix_T(MA_R_RS, MS)
LL5 = rm.Mat((UR_T_RS_matrix @ RS_T_P_matrix_lock @ inv(MA_P3_T) @ inv(TCP_RA_T)).tolist())

def lock(robot):
    robot.MoveJ(LL1)
    sleep(1)
    robot.MoveL(LL2)
    sleep(1)
    robot.MoveL(LL3)
    sleep(1)
    robot.MoveL(LL4)
    sleep(1)
    robot.MoveL(LL5)
