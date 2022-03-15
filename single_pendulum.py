#Import modules
import numpy as np

#Define the equation of state for a single pendulum
def EoM(theta, l=1, g=9.81):
    #The parameters are the angle theta, the length l (default 1m) and the gravitational acceleration g (default 9.81ms^-2)
    #The second derivative of theta (i.e. the angular acceleration) is given by the following equation
    secondDeriv = -g*np.sin(theta)/l
    return secondDeriv