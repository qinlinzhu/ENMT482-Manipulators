from robodk.robolink import *
import robodk.robomath as rm
import numpy as np
from time import sleep
import mazzer_scale as MS
import mazzer_machine as MM
import WDT as WDT
import PUQ as PUQ
import rancilio as RAN
import cup_dispenser as CD
import cup_tasks as CT
import rancilio_brew as RB
import rancillo_scale as RS

RDK = Robolink()
RDK.setRunMode(RUNMODE_SIMULATE)
UR5 = RDK.Item('UR5', ITEM_TYPE_ROBOT)
world_frame = RDK.Item('UR5 Base', ITEM_TYPE_FRAME)
target = RDK.Item('Home', ITEM_TYPE_TARGET)   # existing target in station
UR5.setPoseFrame(world_frame)
UR5.setPoseTool(UR5.PoseTool())
robot_program = RDK.Item('Reset_Simulation', ITEM_TYPE_PROGRAM)
robot_program.RunCode()
home = [0, -90, -90, -90, 90, 0]

def test():

    
    IP = [-48.510000, -80.850000, -87.660000, -126.540000, 84.260000, -212.440000]
    UR5.MoveJ(IP)
    
    robot_program = RDK.Item('Cup_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    CT.tasks_cup(UR5) #task_m

    
    IP = [-85.960000, -62.130000, -131.910000, -17.870000, -77.450000, -220.430000]
    UR5.MoveJ(IP)
    IP = [-155.740000, -62.130000, -131.910000, -17.870000, -77.450000, -220.430000]
    UR5.MoveJ(IP)


    IP = [-145.530000, -57.020000, -145.530000, -146.360000, -113.320000, -220.000000]
    UR5.MoveJ(IP)
    CT.customer_zone(UR5) #task_q
    
    robot_program = RDK.Item('Cup_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()




def main():
    robot_program = RDK.Item('Reset_Simulation', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    UR5.MoveJ(home)
 
    """
        TASK A
        PICK UP RANCILIO TOOL
        PLACE ON MAZZER SCALE PAN AND DETACH
    """
    robot_program = RDK.Item('Rancilio_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    MS.task_a(UR5)

    MS.task_ab(UR5)
    
    """
        TASK B
        PICK UP MAZZER TOOL
        UNLOCK MAZZER SCALE
    """

    robot_program = RDK.Item('Rancilio_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    robot_program = RDK.Item('Mazzer_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    MS.task_b(UR5)
     
    """
        TASK C
        TURN GRINDER ON
        WAIT 15s
        TURN GRINDER OFF
    """

    MM.task_c(UR5)

    """
        TASK D
        TURN DOSING LEVER
    """

    MM.task_d(UR5)
    
    """
        TASK E
        LOCK MAZZER SCALE
    """

    MS.task_e(UR5)
    MS.task_ef(UR5)
    
    """
    TASK F
        DETACH MAZZER TOOL
        GRAB RANCILIO TOOL FROM MAZZER SCALE
    """

    
    robot_program = RDK.Item('Mazzer_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    MS.task_f(UR5)
    
    robot_program = RDK.Item('Student_Tool_Attach', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    
    """ 
        TASK G
        OPEN WDT FIXTURE
    """
    # robot_program = RDK.Item('Distribution_Tool_Open', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    
    #WDT.task_g(UR5)
    
    
    """
        TASK H
        RELEASE RANCILIO TOOL
        CLOSE THE WDT FIXTURE
        WAIT 15 SECONDS
    """
    
    # robot_program = RDK.Item('Student_Tool_Detach', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    
    # robot_program = RDK.Item('Distribution_Tool_Close', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    # sleep(14)
    
    
    """
        TASK I
        OPEN WDT FIXTURE
        REMOVE RANCILIO TOOL
        CLOSE WDT FIXTURE
    """
    # robot_program = RDK.Item('Distribution_Tool_Open', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    # robot_program = RDK.Item('Student_Tool_Attach', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()  
    # robot_program.WaitFinished()
    
    # WDT.task_i(UR5)
    
    # robot_program = RDK.Item('Distribution_Tool_Close', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    """
        TASK J
        PLACE RANCILIO TOOL IN PUQ
        WAIT 2 SECONDS
    """
    
    PUQ.task_j(UR5)
    
    
    """
        TASK K
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    
    RAN.task_k(UR5)
    IP = [-345.730000, -109.460000, 143.510000, -31.920000, 47.750000, -217.320000]
    UR5.MoveL(IP)
    sleep(1)
    
    IP = [-344.840000, -102.160000, 43.780000, 53.510000, 75.410000, -217.260000]
    UR5.MoveL(IP)
    sleep(1)
    
    """
        TASK L
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    robot_program = RDK.Item('Mazzer_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    IP = [-48.510000, -80.850000, -87.660000, -126.540000, 84.260000, -212.440000]
    UR5.MoveJ(IP)

    
    CD.cup_dispender(UR5) #task_l
    """
        TASK M
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    
    IP = [-48.510000, -80.850000, -87.660000, -126.540000, 84.260000, -212.440000]
    UR5.MoveJ(IP)
    
    robot_program = RDK.Item('Mazzer_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    IP = [-48.510000, -80.850000, -87.660000, -126.540000, 84.260000, -212.440000]
    UR5.MoveJ(IP)
    
    robot_program = RDK.Item('Cup_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()

    IP = [-194.844324, -83.269851, -142.076776, -134.653704, -114.853959, -220.000195]
    UR5.MoveJ(IP)
    IP = [-184.089942, -101.790286, -123.756968, -134.453056, -104.099577, -220.000131]
    UR5.MoveJ(IP)
    CT.tasks_cup(UR5) #task_m

    """
        TASK N
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """

    IP = [-143.830000, -72.340000, -150.640000, -131.910000, -111.490000, -217.020000]
    UR5.MoveJ(IP)

    IP = [-152.340000, -72.340000, -150.640000, -58.720000, -102.980000, -217.020000]
    UR5.MoveJ(IP)
    IP = [-145.530000, -78.020000, -135.320000, -22.980000, -106.380000, -218.900000]
    UR5.MoveJ(IP)
    IP = [-79.150000, -78.020000, -135.320000, -22.980000, -106.380000, -218.900000]
    UR5.MoveJ(IP)
    robot_program = RDK.Item('Cup_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    robot_program = RDK.Item('Mazzer_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    IP= [-36.600000, -74.040000, -131.730000, -68.940000, 90.590000, -201.850000]
    UR5.MoveJ(IP)
    IP= [-125.586872, -71.838837, -130.601998, -27.751281, 89.271708, -223.836247]
    UR5.MoveJ(IP)
    
    RS.unlock(UR5) #task_n
    
    """
        TASK O
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    
    IP = [-120.530000, -64.560000, -138.490000, -15.660000, 89.150000, -225.830000]
    UR5.MoveJ(IP)
    IP = [-130.320000, -100.250000, -135.060000, 56.310000, 100.320000, -40.000000]
    UR5.MoveJ(IP)
    RB.Brew(UR5) #task_o
    IP = [-130.320000, -100.250000, -135.060000, 56.310000, 100.320000, -40.000000]
    UR5.MoveJ(IP)
    IP = [-120.530000, -64.560000, -138.490000, -15.660000, 89.150000, -225.830000]
    UR5.MoveJ(IP)
    
    """
        TASK P
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    
    RS.lock(UR5) #task_p
    
    """
        TASK Q
        REMOVE RANCILIO TOOL FROM PUQ
        INSERT INTO RANCILIO GROUP HEAD
        DETACH TOOL
        MOVE AWAY 25mm
    """
    
    IP= [-125.586872, -71.838837, -130.601998, -27.751281, 89.271708, -223.836247]
    UR5.MoveJ(IP)
    
    IP= [-36.600000, -74.040000, -131.730000, -68.940000, 90.590000, -201.850000]
    UR5.MoveJ(IP)
    
    robot_program = RDK.Item('Mazzer_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    robot_program = RDK.Item('Cup_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    IP = [-85.960000, -62.130000, -131.910000, -17.870000, -77.450000, -220.430000]
    UR5.MoveJ(IP)
    IP = [-155.740000, -62.130000, -131.910000, -17.870000, -77.450000, -220.430000]
    UR5.MoveJ(IP)


    IP = [-145.530000, -57.020000, -145.530000, -146.360000, -113.320000, -220.000000]
    UR5.MoveJ(IP)
    CT.customer_zone(UR5) #task_q
    
    robot_program = RDK.Item('Cup_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    """
        TASK R
        GO TO RANCILIO GROUP HEAD
        CALL CLEANING ROUTINE
    """
    IP = [-126.810000, -82.550000, -140.430000, 51.910000, 92.770000, -36.600000]
    UR5.MoveJ(IP)
    
    RAN.task_r(UR5)
    robot_program = RDK.Item('Rancilio_Tool_Clean', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    
    """
        TASK S
        RETURN RANCILIO TOOL 
    """

    # robot_program = RDK.Item('Rancilio_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    # robot_program.RunCode()
    # robot_program.WaitFinished()
    
    """
        TASK T
        RETURN RANCILIO TOOL 
    """
    

    robot_program = RDK.Item('Mazzer_Tool_Attach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
    IP = [-120.530000, -64.560000, -138.490000, -15.660000, 89.150000, -225.830000]
    UR5.MoveJ(IP)
    IP = [-130.320000, -100.250000, -135.060000, 56.310000, 100.320000, -40.000000]
    UR5.MoveJ(IP)
    RB.Brew2(UR5) #task_t
    IP = [-130.320000, -100.250000, -135.060000, 56.310000, 100.320000, -40.000000]
    UR5.MoveJ(IP)
    IP = [-120.530000, -64.560000, -138.490000, -15.660000, 89.150000, -225.830000]
    UR5.MoveJ(IP)
    robot_program = RDK.Item('Mazzer_Tool_Detach_(ATI)', ITEM_TYPE_PROGRAM)
    robot_program.RunCode()
    robot_program.WaitFinished()
        
    """
    END
    GO HOME
    """
    UR5.MoveJ(home)
    
#main()
test()
