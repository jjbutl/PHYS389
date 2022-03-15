#Import modules, including the file being tested, singlePendulum
import single_pendulum as sp
import numpy as np

#Test the EoM function
def test_EoM():
    #Check that when the pendulum is horizontal, sin(theta)=1 and so the angular acceleration = -g/l
    assert sp.EoM(np.pi/2, 1, 9.81) == -9.81
    #Check that when the pendulum is vertical, sin(theta)=0 and so the angular acceleration = 0
    assert sp.EoM(0, 1, 9.81) == 0

test_EoM()