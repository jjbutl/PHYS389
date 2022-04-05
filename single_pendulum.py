#Import modules
import numpy as np
from general_pendulum import GeneralPendulum
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from astropy.io import fits
from astropy.table import Table
import os

#Create a class for a single pendulum
class SinglePendulum(GeneralPendulum):
    def __init__(self, input):
        #As a default, m=1kg, l=1m and g=9.81ms^-2
        self.system = input['system']
        self.method = input['method']
        self.num = int(input['multiplenumber'])
        self.m = float(input['mass'])
        self.l = float(input['length'])
        self.g = 9.81
        self.initialThetaDegrees = float(input['initialtheta'])
        self.initialTheta = np.pi*self.initialThetaDegrees/180
        self.initialz = float(input['initialz'])
        self.simulationTime = float(input['simulationtime'])
        self.timestep = float(input['timestep'])
        self.directory = input['directory']
        #Create an array t which runs from zero to simulationTime in intervals of the timestep
        self.t = np.arange(0, self.simulationTime, self.timestep)
        #Create an array for the initial variables
        self.initialVariables = np.array([self.initialTheta, self.initialz])

    def derivatives(self, t, variables):
        #The parameters are variables (theta, z) and time t
        theta, z = variables
        #z is defined as the first derivative of theta, i.e. thetaderiv
        thetaderiv = z
        #zderiv is the first derivative of z, or equivalently, the second derivative of theta
        zderiv = -self.g*np.sin(theta)/self.l
        #Return thetaderiv and zderiv as an array
        return np.array([thetaderiv, zderiv])

    def data(self,variables):
        theta = variables[0] - ((variables[0] + np.pi) // (2*np.pi)) * 2*np.pi
        z = variables[1]
        x = self.l*np.sin(theta)
        y = -self.l*np.cos(theta)
        v_squared = (self.l*z)**2
        p = self.m*(self.l**2)*z
        pe = self.potentialEnergy(m=self.m,y=y)
        ke = self.kineticEnergy(m=self.m,v_squared=v_squared)
        te = self.totalEnergy(ke,pe)
        return [self.t, theta, z, x, y, p, pe, ke, te]

    def makeDirectory(self):
        dir = "{0}\\Simulation_Data\\sp_m={1}kg,l={2}m,t={3}s,step={4}ms".format(self.directory, self.m, self.l, int(self.simulationTime), int(self.timestep*1E3))
        if os.path.exists(dir) == False:
            os.mkdir(dir)

    def saveFits(self, data):
        #Set up the columns for a fits table to store the simulation data
        hdu=fits.BinTableHDU.from_columns(
            [fits.Column(name="Time", format="E", array=data[0]),
            fits.Column(name="Theta", format="E", array=data[1]),
            fits.Column(name="z", format="E", array=data[2]),
            fits.Column(name="x_pos", format="E", array=data[3]),
            fits.Column(name="y_pos", format="E", array=data[4]),
            fits.Column(name="p", format="E", array=data[5]),
            fits.Column(name="Potential_Energy", format="E", array=data[6]),
            fits.Column(name="Kinetic_Energy", format="E", array=data[7]),
            fits.Column(name="Total_Energy", format="E", array=data[8])
            ])
        file = "{0}\\Simulation_Data\\sp_m={1}kg,l={2}m,t={3}s,step={4}ms\\sp_theta={5}deg,z={6}s^-1.fits".format(self.directory, self.m, self.l, int(self.simulationTime), int(self.timestep*1E3), int(self.initialThetaDegrees), int(self.initialz))
        hdu.writeto(file, overwrite="True")

    def loadFits(self):
        return Table.read("{0}\\Simulation_Data\\sp_m={1}kg,l={2}m,t={3}s,step={4}ms\\sp_theta={5}deg,z={6}s^-1.fits".format(self.directory, self.m, self.l, int(self.simulationTime), int(self.timestep*1E3), int(self.initialThetaDegrees), int(self.initialz)))

    def createInitialRange(self):
        initialThetaRange = np.linspace(-self.initialTheta, self.initialTheta, num=self.num)
        hdu=fits.BinTableHDU.from_columns(
            [fits.Column(name="InitialTheta", format="E", array=initialThetaRange)])
        file = "{0}\\Simulation_Data\\sp_m={1}kg,l={2}m,t={3}s,step={4}ms\\sp_initial_range.fits".format(self.directory, self.m, self.l, int(self.simulationTime), int(self.timestep*1E3))
        hdu.writeto(file, overwrite="True")

    def loadInitialRange(self):
        t = Table.read("{0}\\Simulation_Data\\sp_m={1}kg,l={2}m,t={3}s,step={4}ms\\sp_initial_range.fits".format(self.directory, self.m, self.l, int(self.simulationTime), int(self.timestep*1E3)))
        return np.array(t["InitialTheta"])

    def updateInitialRange(self, initialRange, x):
        self.initialTheta = initialRange[x]
        self.initialThetaDegrees = 180*self.initialTheta/np.pi

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
        line_ani.save("{0}\\Simulation_Data\\single_pendulum_m={1}kg,l={2}m,theta={3}deg,t={4}s,step={5}ms.gif".format(self.directory, self.m, self.l, int(self.initialThetaDegrees), int(self.simulationTime), int(self.timestep*1E3)), writer=writergif)
    