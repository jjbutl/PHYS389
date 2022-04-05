import numpy as np

def testKE(system):
    if system.system == "TEST_SP":
        #Check that when v=0, kineticEnergy = 0.5*m*v^2 = 0:
        assert np.abs(system.kineticEnergy(m=system.m, v_squared=0**2)) <= 1e-5
        #Check that when v=10, kineticEnergy = 0.5*m*v^2 = 50:
        assert system.kineticEnergy(m=system.m, v_squared=10**2) == 50
    elif system.system == "TEST_DP":
        #Check that when v1=0, kineticEnergy1 = 0.5*m1*v1^2 = 0:
        assert np.abs(system.kineticEnergy(m=system.m1, v_squared=0**2)) <= 1e-5
        #Check that when v2=0, kineticEnergy2 = 0.5*m2*v2^2 = 0:
        assert np.abs(system.kineticEnergy(m=system.m2, v_squared=0**2)) <= 1e-5
        #Check that when v1=10, kineticEnergy1 = 0.5*m1*v1^2 = 50:
        assert system.kineticEnergy(m=system.m1, v_squared=10**2) == 50
        #Check that when v2=10, kineticEnergy2 = 0.5*m2*v2^2 = 50:
        assert system.kineticEnergy(m=system.m2, v_squared=10**2) == 50
    else:
        print("Please choose a valid system to test (TEST_SP or TEST_DP).")

def testPE(system):
    if system.system == "TEST_SP":
        #Check that when y=0, potentialEnergy = m*g*y = 0:
        assert np.abs(system.potentialEnergy(m=system.m, y=0)) <= 1e-5
        #Check that when y=10, potentialEnergy = m*g*y = 98.1:
        assert np.abs(system.potentialEnergy(m=system.m, y=10) - 98.1) <= 1e-5
    elif system.system == "TEST_DP":
        #Check that when y1=0, potentialEnergy1 = m1*g*y1 = 0:
        assert np.abs(system.potentialEnergy(m=system.m1, y=0)) <= 1e-5
        #Check that when y2=0, potentialEnergy2 = m2*g*y2 = 0:
        assert np.abs(system.potentialEnergy(m=system.m2, y=0)) <= 1e-5
        #Check that when y1=10, potentialEnergy1 = m1*g*y1 = 98.1:
        assert np.abs(system.potentialEnergy(m=system.m1, y=10) - 98.1) <= 1e-5
        #Check that when y2=10, potentialEnergy2 = m2*g*y2 = 98.1:
        assert np.abs(system.potentialEnergy(m=system.m2, y=10) - 98.1) <= 1e-5
    else:
        print("Please choose a valid system to test (TEST_SP or TEST_DP).")

def testTE(system):
    #Check that when kineticEnergy=5 and potentialEnergy=5, totalEnergy = kineticEnergy + potentialEnergy = 10:
    assert system.totalEnergy(kinetic=5, potential=5) == 10