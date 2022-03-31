#Import modules
import numpy as np
from choose_system import chooseSystem
from simulation import simulation, animation

#Set the directory to save files in
directory = "C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389"

#Set the simulation paramters for single pendulum (sp):
m=2 #Mass of bob m in kg
l=4 #Length of pendulum l in m
spSimulationTime = 5 #Simulation time in s
spTimestep = 0.01 #Timestep in s
initialTheta = np.pi/3 #Initial angle theta in radians
initialz = 0 #Initial z (angular velocity) in rad*s^-1
spInput = [m,l,initialTheta,initialz,spSimulationTime,spTimestep,directory]

#Set the simulation paramters for double pendulum (dp):
m1=2 #Mass of bob m1 in kg
m2=4 #Mass of bob m2 in kg
l1=2 #Length of pendulum l1 in m
l2=5 #Length of pendulum l2 in m
dpSimulationTime = 20 #Simulation time in s
dpTimestep = 0.01 #Timestep in s
initialTheta1 = -np.pi #Initial angle theta1 in radians
initialTheta2 = -np.pi #Initial angle theta2 in radians
initialz1 = 0 #Initial z1 (angular velocity) in rad*s^-1
initialz2 = 0.05 #Initial z2 (angular velocity) in rad*s^-1
dpInput = [m1,m2,l1,l2,initialTheta1,initialTheta2,initialz1,initialz2,dpSimulationTime,dpTimestep,directory]

sys = "dp" #Choose "sp" for single pendulum or "dp" for double pendulum

system = chooseSystem(sys, spInput, dpInput)
simulation(system) #Simulate the system and create the data file
animation(system)