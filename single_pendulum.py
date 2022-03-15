#Import modules
import numpy as np

#Define the equation of state for a single pendulum
def EoM(theta, l=1, g=9.81):
    #The parameters are the angle theta, the length l (default 1m) and the gravitational acceleration g (default 9.81ms^-2)
    #The second derivative of theta (i.e. the angular acceleration) is returned
    return -g*np.sin(theta)/l

def kineticEnergy(z, m=1, l=1):
    #The parameters are z (defined as the first derivative of theta), bob mass m (default 1kg) and length l (default 1m)
    #The kinetic energy of the pendulum is returned
    return 0.5*m*(l**2)*(z**2)

def potentialEnergy(theta, m=1, l=1, g=9.81):
    #The parameters are the angle theta, mass m (default 1kg), length l (default 1m) and gravitational acceleration g (default 9.81ms^-2)
    #The potential energy of the pendulum is returned
    return -m*g*l*np.cos(theta)