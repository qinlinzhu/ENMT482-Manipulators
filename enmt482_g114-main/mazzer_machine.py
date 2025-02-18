from math_tool import matrix_T, inv
import numpy as np
import robodk.robomath as rm
from time import sleep


UR_T_MM = np.array([[-0.866, 0.241, -0.438, 502.38],
                    [-0.5, -0.418,   0.759, -417.51],
                    [0,     0.876,   0.482, 317],
                    [0,     0,       0,     1]])


TCP_T_MA = np.array([[0.643, 0.766, 0, 0],
                      [-0.766, 0.643, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 1]])

MA_T_PB = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 102.82],
                     [0, 0, 0, 1]])


def task_c(robot):


    MM_alpha_MML = [90, 180, -45]
    MM_D_PON = np.array([93.8569, -165.8373, -168.82])
    MM_D_POFF = np.array([96.6787,-158.484,-182.565])


    # Mazzer Machine location 1 frame transformation in the Mazzer Machine frame
    MM_D_MML1 = MM_D_PON + np.array([10, 0, 0])
    MM_T_MML1 = matrix_T(MM_alpha_MML, MM_D_MML1)

    # Mazzer Machine location 2 frame transformation in the Mazzer Machine frame
    MM_D_MML2 = MM_D_PON + np.array([-8, 0, 0])
    MM_T_MML2 = matrix_T(MM_alpha_MML, MM_D_MML2)

    # Mazzer Machine location 3 frame transformation in the Mazzer Machine frame
    MM_D_MML3 = MM_D_POFF + np.array([10, 0, 0])
    MM_T_MML3 = matrix_T(MM_alpha_MML, MM_D_MML3)

    # Mazzer Machine location 4 frame transformation in the Mazzer Machine frame
    MM_D_MML4 = MM_D_POFF + np.array([-8, 0, 0])
    MM_T_MML4 = matrix_T(MM_alpha_MML, MM_D_MML4)



    # Calculate UR_T_MM for each location
    # Mazzer Machine Location 1
    L1 = rm.Mat((UR_T_MM @ MM_T_MML1 @ inv(MA_T_PB) 
                @ inv(TCP_T_MA)).tolist())

    # Mazzer Machine Location 2
    L2 = rm.Mat((UR_T_MM @ MM_T_MML2 @ inv(MA_T_PB) 
                @ inv(TCP_T_MA)).tolist())

    # Mazzer Machine Location 3
    L3 = rm.Mat((UR_T_MM @ MM_T_MML3 @ inv(MA_T_PB) 
                @ inv(TCP_T_MA)).tolist())

    # Mazzer Machine Location 4
    L4 = rm.Mat((UR_T_MM @ MM_T_MML4 @ inv(MA_T_PB) 
                @ inv(TCP_T_MA)).tolist())

    # Mazzer Machine Location 5
    L5 = rm.Mat((UR_T_MM @ MM_T_MML2 @ inv(MA_T_PB) 
                @ inv(TCP_T_MA)).tolist())




    robot.MoveL(L1)

    sleep(1)
    robot.MoveL(L2)

    sleep(13) # should be 15

    robot.MoveL(L1)
    
    sleep(1)

    robot.MoveL(L3)

    sleep(1)

    robot.MoveL(L4)
    
    sleep(1)
    
    robot.MoveL(L3)

    sleep(1)




def task_d(robot):
    print("starting task d")
    UR_T_MM = np.array([[-0.866, 0.5, -0.0, 502.38],
                        [-0.5, -0.866,   0.0, -417.51],
                        [0,     0.0,   1, 317],
                        [0,     0,       0,     1]])

    MM_alpha_MML = [0,0,-90]
    MM_D_DL = np.array([84.1929, -119.612, -102.827])
    # matrix1 = makeT(-49.1, MM_D_DL)
    # print("matrix1:", matrix1)
    MM_D_MML1 = MM_D_DL + np.array([45, 200, 10])
    MM_T_MML1 = matrix_T(MM_alpha_MML, MM_D_MML1)
    
    MM_D_MML2 = MM_D_MML1 + np.array([0,0,-50])
    MM_T_MML2 = matrix_T(MM_alpha_MML, MM_D_MML2)
    
    MM_D_MML3 = MM_D_MML2 + np.array([-20,-100, 0])
    MM_T_MML3 = matrix_T(MM_alpha_MML, MM_D_MML3)
    
    MM_D_MML4 = MM_D_MML3 + np.array([100,30, 0])
    MM_T_MML4 = matrix_T(MM_alpha_MML, MM_D_MML4)
    
    
    
    
    L1 = rm.Mat((UR_T_MM @ MM_T_MML1 @ inv(MA_T_PB)
                @ inv(TCP_T_MA)).tolist())
    
    L2 = rm.Mat((UR_T_MM @ MM_T_MML2 @ inv(MA_T_PB)
                @ inv(TCP_T_MA)).tolist())
    
    L3 = rm.Mat((UR_T_MM @ MM_T_MML3 @ inv(MA_T_PB)
                @ inv(TCP_T_MA)).tolist())
    
    L4 = rm.Mat((UR_T_MM @ MM_T_MML4 @ inv(MA_T_PB)
                @ inv(TCP_T_MA)).tolist())
    
    
    robot.MoveL(L1)
    sleep(1)
    
    robot.MoveL(L2)
    sleep(1)
    
    robot.MoveL(L3)
    sleep(1)
    
    robot.MoveL(L4)
    sleep(1)
    print("ending task d")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
