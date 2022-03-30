#Import modules
import numpy as np
from double_pendulum import DoublePendulum

#Set the directory to save files in
directory = "C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389"

#Set the simulation paramters:
m1=2 #Mass of bob m in kg
m2=2
l1=2 #Length of pendulum l in m
l2=5
simulationTime = 2 #Simulation time in s
timestep = 0.001 #Timestep in s
initialTheta1 = np.pi/2 #Initial angle theta in radians
initialTheta2 = -np.pi
initialz1 = 0 #Initial z (angular velocity) in rad*s^-1
initialz2 = 0

#Create an instance of a doublePendulum
doublePendulum = DoublePendulum(m1=m1, m2=m2, l1=l1, l2=l2)
#Create an array t which runs from zero to simulationTime in intervals of the timestep
t = np.arange(0, simulationTime+timestep, timestep)
#Create an array for the initial variables
initialVariables = np.array([initialTheta1, initialTheta2, initialz1, initialz2])
#Numerically integrate the equations of motion
variables = doublePendulum.integrate(t, initialVariables, doublePendulum)
#Create a 2d python array containing time, theta, z, x position and y position
x1 = l1*np.sin(variables[:,0])
y1 = -l1*np.cos(variables[:,0])
x2 = x1 + l2*np.sin(variables[:,1])
y2 = y1 - l2*np.cos(variables[:,1])

data = np.append(variables, np.transpose([t, x1, y1, x2, y2]), axis=1)
#Plot, save and show an animation of the pendulum's motion
doublePendulum.animation(directory, data, initialTheta1, initialTheta2, simulationTime, timestep)
#Save the simulation data to a fits file
doublePendulum.saveFits(directory, data, initialTheta1, initialTheta2, simulationTime, timestep)