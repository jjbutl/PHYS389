#Import modules, including the file being tested, singlePendulum
import single_pendulum as sp
import numpy as np

#Test the EoM function
def test_EoM():
    #Check that when the pendulum is horizontal, sin(theta)=1 and so the angular acceleration = -g/l:
    assert sp.EoM(np.pi/2, 1, 9.81) == -9.81
    #Check that when the pendulum is vertical, sin(theta)=0 and so the angular acceleration = 0:
    assert sp.EoM(0, 1, 9.81) == 0

#test_EoM()

#Test the kineticEnergy function
def test_kineticEnergy():
    #Check that when the pendulum is horizontal (i.e. z=0 since the pendulum velocity will be 0), the kinetic energy is 0:
    assert sp.kineticEnergy(0, 1, 1) == 0
    #An equation for the first derivative of theta is z=sqrt(-2*g*y)/l. When l=1 and the pendulum is vertical (so y=-l=-1):
    z=np.sqrt(-2*9.81*-1)/1
    #Check that when the pendulum is vertical and m=l=1, the kinetic energy is g=9.81
    assert sp.kineticEnergy(z, 1, 1) == 9.81

#test_kineticEnergy()

#Test the potentialEnergy function
def test_potentialEnergy():
    #Check that when the pendulum is horizontal (i.e. theta=pi/2), the potential energy is approximately 0:
    assert np.abs(sp.potentialEnergy(np.pi/2, 1, 1, 9.81)) <= 1e-10
    #Check that when the pendulum is vertical (i.e. theta=0) and l=1 and m=1, the potential energy is -g=-9.81:
    assert sp.potentialEnergy(0, 1, 1, 9.81) == -9.81

test_potentialEnergy()