#Import modules
import numpy as np
from general_pendulum import GeneralPendulum

#Create a class for a single pendulum
class SinglePendulum(GeneralPendulum):
    def __init__(self, m=1, l=1):
        #As a default, m=1kg, l=1m and g=9.81ms^-2
        self.m = m
        self.l = l
        self.g = 9.81
    def derivatives(self, variables, t=np.arange(0, 10+0.01, 0.01)):
        #The parameters are variables (theta, z) and time t
        theta, z = variables
        #z is defined as the first derivative of theta, i.e. thetadot
        thetadot = z
        #zdot is the first derivative of z, or equivalently, the second derivative of theta
        zdot = -self.g*np.sin(theta)/self.l
        #Return thetadot and zdot as a tuple
        return thetadot, zdot
    def kineticEnergy(self, z):
        #The parameters are z, bob mass m and length l
        #Calculate the kinetic energy of the pendulum
        kinetic = 0.5*self.m*(self.l**2)*(z**2)
        #Return the kinetic energy
        return kinetic
    def potentialEnergy(self, theta):
        #The parameters are the angle theta, mass m, length l and gravitational acceleration g
        #Calculate the potential energy of the pendulum
        potential = -self.m*self.g*self.l*np.cos(theta)
        return potential