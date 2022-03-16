#Import modules
from scipy.integrate import odeint
from astropy.io import fits
import os
import numpy as np
from single_pendulum import SinglePendulum

#Set the directory to save files in
directory = "C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389"

#Set the simulation paramters:
m=2 #Mass of bob m in kg
l=4 #Length of pendulum l in m
simulationTime = 30 #Simulation time in s
timestep = 0.01 #Timestep in s
initialTheta = np.pi/2 #Initial angle theta in radians
initialz = 0 #Initial z (angular velocity) in rad*s^-1

#Create an instance of a SinglePendulum
singlePendulum = SinglePendulum(m=m, l=l)
#Create an array t which runs from zero to simulationTime in intervals of the timestep
t = np.arange(0, simulationTime+timestep, timestep)
#Create a tuple for the initial variables
initialVariables = np.array([initialTheta, initialz])
#Numerically integrate the equations of motion
variables = odeint(singlePendulum.derivatives, initialVariables, t)

#Set up the columns for a fits table to store the simulation data
hdu=fits.BinTableHDU.from_columns(
    [fits.Column(name="Time", format="E", array=t),
    fits.Column(name="Theta", format="E", array=variables[:,0]),
    fits.Column(name="z", format="E", array=variables[:,1])
    ])
#Delete the current fits file if it exists
if os.path.exists("{0}\\single_pendulum_simulation.fits".format(directory)):
    os.remove("{0}\\single_pendulum_simulation.fits".format(directory))
            
#Save the new fits file
hdu.writeto("{0}\\single_pendulum_simulation.fits".format(directory))