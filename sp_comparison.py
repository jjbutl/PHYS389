#Import modules, including the file being tested, singlePendulum
import numpy as np

#Test the derivatives function
def test_derivatives(system):
    if system.system == "TEST_SP":
        #Check that when the pendulum is horizontal and stationary, so theta=pi/2 and z=0, that thetadot=z=0 and zdot=-g*sin(theta)/l=-9.81:
        theta, z = np.pi/2, 0
        assert np.all(system.derivatives(variables=(theta,z),t=system.t) == (0, -9.81))
        #Check that when the pendulum is vertical, so theta=0 and z=sqrt(2*g*cos(theta)/l), that thetadot=z=sqrt(2*g*cos(theta)/l) and zdot=-g*sin(theta)/l=0:
        theta, z = 0, np.sqrt(2*9.81*1)/1
        assert np.all(system.derivatives(variables=(theta,z),t=system.t) == (np.sqrt(2*9.81*1)/1, 0))
    elif system.system == "TEST_DP":
        #Check that when the pendulum is horizontal, so theta=pi/2 and z=sqrt(2*g*cos(theta)/l)=0, that thetadot=z=0 and zdot=-g*sin(theta)/l=-9.81:
        theta1, theta2, z1, z2 = np.pi/2, 0
        assert np.all(system.derivatives(variables=(theta,z),t=system.t) == (0, -9.81))
        #Check that when the pendulum is vertical, so theta=0 and z=sqrt(2*g*cos(theta)/l), that thetadot=z=sqrt(2*g*cos(theta)/l) and zdot=-g*sin(theta)/l=0:
        theta, z = 0, np.sqrt(2*9.81*1)/1
        assert np.all(system.derivatives(variables=(theta,z),t=system.t) == (np.sqrt(2*9.81*1)/1, 0))
    else:
        print("Please choose a valid system to test (TEST_SP or TEST_DP).")

#test_derivatives()

#Test the kineticEnergy function
def test_kineticEnergy():
    #Check that when the pendulum is horizontal, so theta=pi/2 and z=sqrt(2*g*cos(theta)/l)=0, that kineticEnergy=0.5*m*l^2*z^2=0:
    theta = np.pi/2
    z = np.sqrt(2*9.81*np.cos(theta)/1)
    assert np.abs(default.kineticEnergy(z=z)) <= 1e-10
    #Check that when the pendulum is vertical, so theta=0 so z=sqrt(2*g*cos(theta)/l)=sqrt(2*9.81), that kineticEnergy=0.5*m*l^2*z^2=g=9.81:
    theta = 0
    z = np.sqrt(2*9.81*np.cos(theta)/1)
    assert default.kineticEnergy(z=z) == 9.81

#test_kineticEnergy()

#Test the potentialEnergy function
def test_potentialEnergy():
    #Check that when the pendulum is horizontal, so theta=pi/2, that potentialEnergy=-m*g*l*cos(theta)=0:
    theta=np.pi/2
    assert np.abs(default.potentialEnergy(theta=theta)) <= 1e-10
    #Check that when the pendulum is vertical, so theta=0, that potentialEnergy=-m*g*l*cos(theta)=-9.81:
    assert default.potentialEnergy(theta=0) == -9.81

#test_potentialEnergy()