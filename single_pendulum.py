#Import modules
import numpy as np
from general_pendulum import GeneralPendulum
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from astropy.io import fits
import os

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
        #z is defined as the first derivative of theta, i.e. thetaderiv
        thetaderiv = z
        #zderiv is the first derivative of z, or equivalently, the second derivative of theta
        zderiv = -self.g*np.sin(theta)/self.l
        #Return thetaderiv and zderiv as a tuple
        return thetaderiv, zderiv
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
    def integrate(self, t, initialVariables, name):
        #Numerically integrate the equations of motion
        return odeint(name.derivatives, initialVariables, t)
    def animation(self, directory, data, initialTheta, simulationTime, timestep):
        coordinates = np.array([data[:,3],data[:,4]])
        initialThetaDegrees=np.rint((180*initialTheta/np.pi))
        def animatePendulum(step):
            ax.clear()
            ax.plot([0, coordinates[0][step]], [0, coordinates[1][step]], lw=2, c='k')
            ax.plot(coordinates[0, :step+1], coordinates[1, :step+1], c='blue')
            ax.scatter(coordinates[0, step], coordinates[1,step], c='blue', marker='o')
            ax.plot(coordinates[0,0], coordinates[1,0], c='black', marker='o')
            ax.set_xlim([-5,5])
            ax.set_ylim([-5,1])
        fig=plt.figure()
        ax=plt.axes()
        line_ani = ani.FuncAnimation(fig, animatePendulum, interval=1, frames=len(data[:,0]))
        writergif = ani.PillowWriter(fps=50)
        line_ani.save("{0}\\Simulation_Data\\single_pendulum_{1}m_{2}kg_{3}degrees_{4}s_{5}ms.gif".format(directory, self.l, self.m, int(initialThetaDegrees), simulationTime, int(timestep*1E3)), writer=writergif)
    def saveFits(self, directory, data, initialTheta, simulationTime, timestep):
        initialThetaDegrees=np.rint((180*initialTheta/np.pi))
        #Set up the columns for a fits table to store the simulation data
        hdu=fits.BinTableHDU.from_columns(
            [fits.Column(name="Time", format="E", array=data[:,2]),
            fits.Column(name="Theta", format="E", array=data[:,0]),
            fits.Column(name="z", format="E", array=data[:,1]),
            fits.Column(name="x_pos", format="E", array=data[:,3]),
            fits.Column(name="y_pos", format="E", array=data[:,4])
            ])
        #Delete the current fits file if it exists
        if os.path.exists("{0}\\Simulation_Data\\single_pendulum_{1}m_{2}kg_{3}degrees_{4}s_{5}s.fits".format(directory, self.l, self.m, int(initialThetaDegrees), simulationTime, int(timestep*1E3))):
            os.remove("{0}\\Simulation_Data\\single_pendulum_{1}m_{2}kg_{3}degrees_{4}s_{5}s.fits".format(directory, self.l, self.m, int(initialThetaDegrees), simulationTime, int(timestep*1E3)))
                    
        #Save the new fits file
        hdu.writeto("{0}\\Simulation_Data\\single_pendulum_{1}m_{2}kg_{3}degrees_{4}s_{5}s.fits".format(directory, self.l, self.m, int(initialThetaDegrees), simulationTime, int(timestep*1E3)))