#Import modules
import numpy as np
from single_pendulum import SinglePendulum

#Set the directory to save files in
directory = "C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389"

#Set the simulation paramters:
m=2 #Mass of bob m in kg
l=4 #Length of pendulum l in m
simulationTime = 3 #Simulation time in s
timestep = 0.001 #Timestep in s
initialTheta = np.pi/3 #Initial angle theta in radians
initialz = 0 #Initial z (angular velocity) in rad*s^-1

#Create an instance of a SinglePendulum
singlePendulum = SinglePendulum(m=m, l=l)
#Create an array t which runs from zero to simulationTime in intervals of the timestep
t = np.arange(0, simulationTime+timestep, timestep)
#Create a tuple for the initial variables
initialVariables = np.array([initialTheta, initialz])
#Numerically integrate the equations of motion
variables = singlePendulum.integrate(t, initialVariables, singlePendulum)
#Create a 2d python array containing time, theta, z, x position and y position
data = np.append(variables, np.transpose([t, l*np.sin(variables[:,0]), -l*np.cos(variables[:,0])]), axis=1)
#Plot, save and show an animation of the pendulum's motion
singlePendulum.animation(directory, data, initialTheta, simulationTime, timestep)
#Save the simulation data to a fits file
singlePendulum.saveFits(directory, data, initialTheta, simulationTime, timestep)