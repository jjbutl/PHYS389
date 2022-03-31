#Import modules
import numpy as np
from general_pendulum import GeneralPendulum
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from astropy.io import fits
import os
from astropy.table import Table

#Create a class for a single pendulum
class DoublePendulum(GeneralPendulum):
    def __init__(self, dpInput):
        #As a default, m1=1kg, m2=1kg, l1=1m, l2=1m and g=9.81ms^-2
        self.m1 = dpInput[0]
        self.m2 = dpInput[1]
        self.l1 = dpInput[2]
        self.l2 = dpInput[3]
        self.g = 9.81
        self.initialTheta1 = dpInput[4]
        self.initialTheta2 = dpInput[5]
        self.initialTheta1Degrees=np.rint((180*self.initialTheta1/np.pi))
        self.initialTheta2Degrees=np.rint((180*self.initialTheta2/np.pi))
        self.initialz1 = dpInput[6]
        self.initialz2 = dpInput[7]
        self.simulationTime = dpInput[8]
        self.timestep = dpInput[9]
        self.directory = dpInput[10]
        #Create an array t which runs from zero to simulationTime in intervals of the timestep
        self.t = np.arange(0, self.simulationTime+self.timestep, self.timestep)
        #Create an array for the initial variables
        self.initialVariables = np.array([self.initialTheta1, self.initialTheta2, self.initialz1, self.initialz2])

    def derivatives(self, variables, t=np.arange(0, 10+0.01, 0.01)):
        #The parameters are variables (theta, z) and time t
        theta1, theta2, z1, z2, = variables
        #z is defined as the first derivative of theta, i.e. thetaderiv
        theta1deriv = z1
        theta2deriv = z2
        cos = np.cos(theta1-theta2)
        sin = np.sin(theta1-theta2)
        #zderiv is the first derivative of z, or equivalently, the second derivative of theta
        z1deriv = (self.m2*self.g*np.sin(theta2)*cos - self.m2*sin*(self.l1*z1**2*cos + self.l2*z2**2) - (self.m1+self.m2)*self.g*np.sin(theta1)) / (self.l1*(self.m1 + self.m2*sin**2))
        z2deriv = ((self.m1+self.m2)*(self.l1*z1**2*sin - self.g*np.sin(theta2) + self.g*np.sin(theta1)*cos) + self.m2*self.l2*z2**2*sin*cos) / (self.l2*(self.m1 + self.m2*sin**2))
        #Return derivatives as an array
        return np.array([theta1deriv, theta2deriv, z1deriv, z2deriv])

    def data(self,variables):
        x1 = self.l1*np.sin(variables[:,0])
        y1 = -self.l1*np.cos(variables[:,0])
        x2 = x1 + self.l2*np.sin(variables[:,1])
        y2 = y1 - self.l2*np.cos(variables[:,1])
        pe = self.potentialEnergy(m=self.m1,l=self.l1,theta=variables[:,0]) + self.potentialEnergy(m=self.m2,l=self.l2,theta=variables[:,1])
        ke = self.kineticEnergy(m=self.m1,l=self.l1,z=variables[:,2]) + self.kineticEnergy(m=self.m1,l=self.l2,z=variables[:,3])
        te = self.totalEnergy(ke,pe)
        return np.append(variables, np.transpose([self.t, x1, y1, x2, y2, pe, ke, te]), axis=1)
    
    def saveFits(self, data):
        #Set up the columns for a fits table to store the simulation data
        hdu=fits.BinTableHDU.from_columns(
            [fits.Column(name="Time", format="E", array=data[:,4]),
            fits.Column(name="Theta1", format="E", array=data[:,0]),
            fits.Column(name="Theta2", format="E", array=data[:,1]),
            fits.Column(name="z1", format="E", array=data[:,2]),
            fits.Column(name="z2", format="E", array=data[:,3]),
            fits.Column(name="x1_pos", format="E", array=data[:,5]),
            fits.Column(name="y1_pos", format="E", array=data[:,6]),
            fits.Column(name="x2_pos", format="E", array=data[:,7]),
            fits.Column(name="y2_pos", format="E", array=data[:,8]),
            fits.Column(name="Potential_Energy", format="E", array=data[:,9]),
            fits.Column(name="Kinetic_Energy", format="E", array=data[:,10]),
            fits.Column(name="Total_Energy", format="E", array=data[:,11])
            ])
        #Delete the current fits file if it exists
        if os.path.exists("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(self.directory, self.m1, self.m2, self.l1, self.l2, int(self.initialTheta1Degrees), int(self.initialTheta2Degrees), self.simulationTime, int(self.timestep*1E3))):
            os.remove("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(self.directory, self.m1, self.m2, self.l1, self.l2, int(self.initialTheta1Degrees), int(self.initialTheta2Degrees), self.simulationTime, int(self.timestep*1E3)))      
        #Save the new fits file
        hdu.writeto("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(self.directory, self.m1, self.m2, self.l1, self.l2, int(self.initialTheta1Degrees), int(self.initialTheta2Degrees), self.simulationTime, int(self.timestep*1E3)))
    
    def openFits(self):
        return Table.read("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(self.directory, self.m1, self.m2, self.l1, self.l2, int(self.initialTheta1Degrees), int(self.initialTheta2Degrees), self.simulationTime, int(self.timestep*1E3)))
    
    def animation(self, table):
        coordinates1 = np.array([table["x1_pos"],table["y1_pos"]])
        coordinates2 = np.array([table["x2_pos"],table["y2_pos"]])
        plotLength = self.l1 + self.l2 + 1
        def animatePendulum(step):
            ax.clear()
            ax.plot([0, coordinates1[0][step], coordinates2[0][step]], [0, coordinates1[1][step], coordinates2[1][step]], lw=2, c='k')
            ax.plot(coordinates1[0, :step+1], coordinates1[1, :step+1], c='blue')
            ax.scatter(coordinates1[0, step], coordinates1[1,step], c='blue', marker='o')
            ax.plot(coordinates1[0,0], coordinates1[1,0], c='black', marker='o')
            ax.plot(coordinates2[0, :step+1], coordinates2[1, :step+1], c='blue')
            ax.scatter(coordinates2[0, step], coordinates2[1,step], c='blue', marker='o')
            ax.plot(coordinates2[0,0], coordinates2[1,0], c='black', marker='o')
            ax.set_xlim([-plotLength,plotLength])
            ax.set_ylim([-plotLength,plotLength])
        fig=plt.figure()
        ax=plt.axes()
        line_ani = ani.FuncAnimation(fig, animatePendulum, interval=1, frames=len(table["Time"]))
        writergif = ani.PillowWriter(fps=50)
        line_ani.save("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.gif".format(self.directory, self.m1, self.m2, self.l1, self.l2, int(self.initialTheta1Degrees), int(self.initialTheta2Degrees), self.simulationTime, int(self.timestep*1E3)), writer=writergif)
    