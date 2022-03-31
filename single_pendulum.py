#Import modules
import numpy as np
from general_pendulum import GeneralPendulum
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from astropy.io import fits
import os
from astropy.table import Table

#Create a class for a single pendulum
class SinglePendulum(GeneralPendulum):
    def __init__(self, spInput):
        #As a default, m=1kg, l=1m and g=9.81ms^-2
        self.m = spInput[0]
        self.l = spInput[1]
        self.g = 9.81
        self.initialTheta = spInput[2]
        self.initialThetaDegrees = np.rint((180*self.initialTheta/np.pi))
        self.initialz = spInput[3]
        self.simulationTime = spInput[4]
        self.timestep = spInput[5]
        self.directory = spInput[6]
        #Create an array t which runs from zero to simulationTime in intervals of the timestep
        self.t = np.arange(0, self.simulationTime+self.timestep, self.timestep)
        #Create an array for the initial variables
        self.initialVariables = np.array([self.initialTheta, self.initialz])

    def derivatives(self, variables, t):
        #The parameters are variables (theta, z) and time t
        theta, z = variables
        #z is defined as the first derivative of theta, i.e. thetaderiv
        thetaderiv = z
        #zderiv is the first derivative of z, or equivalently, the second derivative of theta
        zderiv = -self.g*np.sin(theta)/self.l
        #Return thetaderiv and zderiv as an array
        return np.array([thetaderiv, zderiv])

    def data(self,variables):
        x = self.l*np.sin(variables[:,0])
        y = -self.l*np.cos(variables[:,0])
        pe = self.potentialEnergy(m=self.m,l=self.l,theta=variables[:,0])
        ke = self.kineticEnergy(m=self.m,l=self.l,z=variables[:,1])
        te = self.totalEnergy(ke,pe)
        return np.append(variables, np.transpose([self.t, x, y, pe, ke, te]), axis=1)

    def saveFits(self, data):
        #Set up the columns for a fits table to store the simulation data
        hdu=fits.BinTableHDU.from_columns(
            [fits.Column(name="Time", format="E", array=data[:,2]),
            fits.Column(name="Theta", format="E", array=data[:,0]),
            fits.Column(name="z", format="E", array=data[:,1]),
            fits.Column(name="x_pos", format="E", array=data[:,3]),
            fits.Column(name="y_pos", format="E", array=data[:,4]),
            fits.Column(name="Potential_Energy", format="E", array=data[:,5]),
            fits.Column(name="Kinetic_Energy", format="E", array=data[:,6]),
            fits.Column(name="Total_Energy", format="E", array=data[:,7])
            ])
        #Delete the current fits file if it exists
        if os.path.exists("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}degrees,t={4}s,step={5}ms.fits".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), self.simulationTime, int(self.timestep*1E3))):
            os.remove("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}degrees,t={4}s,step={5}ms.fits".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), self.simulationTime, int(self.timestep*1E3)))
        #Save the new fits file
        hdu.writeto("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}degrees,t={4}s,step={5}ms.fits".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), self.simulationTime, int(self.timestep*1E3)))

    def openFits(self):
        return Table.read("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}degrees,t={4}s,step={5}ms.fits".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), self.simulationTime, int(self.timestep*1E3)))

    def animation(self, table):
        coordinates = np.array([table["x_pos"],table["y_pos"]])
        plotLength = self.l + 1
        def animatePendulum(step):
            ax.clear()
            ax.plot([0, coordinates[0][step]], [0, coordinates[1][step]], lw=2, c='k')
            ax.plot(coordinates[0, :step+1], coordinates[1, :step+1], c='blue')
            ax.scatter(coordinates[0, step], coordinates[1,step], c='blue', marker='o')
            ax.plot(coordinates[0,0], coordinates[1,0], c='black', marker='o')
            ax.set_xlim([-plotLength,plotLength])
            ax.set_ylim([-plotLength,plotLength])
        fig=plt.figure()
        ax=plt.axes()
        line_ani = ani.FuncAnimation(fig, animatePendulum, interval=1, frames=len(table["Time"]))
        writergif = ani.PillowWriter(fps=50)
        line_ani.save("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}degrees,t={4}s,step={5}ms.gif".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), self.simulationTime, int(self.timestep*1E3)), writer=writergif)
    