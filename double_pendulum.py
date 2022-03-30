#Import modules
import numpy as np
from general_pendulum import GeneralPendulum
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from astropy.io import fits
import os

#Create a class for a single pendulum
class DoublePendulum(GeneralPendulum):
    def __init__(self, m1=1, m2=1, l1=1, l2=1):
        #As a default, m1=1kg, m2=1kg, l1=1m, l2=1m and g=9.81ms^-2
        self.m1 = m1
        self.m2 = m2
        self.l1 = l1
        self.l2 = l2
        self.g = 9.81
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
        #Return thetaderiv and zdot as a tuple
        return theta1deriv, theta2deriv, z1deriv, z2deriv
    def kineticEnergy(self, z1, z2):
        #The parameters are z, bob mass m and length l
        #Calculate the kinetic energy of the pendulum
        kinetic = 0.5*self.m1*(self.l1**2)*(z1**2) + 0.5*self.m2*(self.l2**2)*(z2**2)
        #Return the kinetic energy
        return kinetic
    def potentialEnergy(self, theta1, theta2):
        #The parameters are the angle theta, mass m, length l and gravitational acceleration g
        #Calculate the potential energy of the pendulum
        potential = -self.m1*self.g*self.l1*np.cos(theta1) - self.m2*self.g*self.l2*np.cos(theta2) 
        return potential
    def integrate(self, t, initialVariables, name):
        #Numerically integrate the equations of motion
        return odeint(name.derivatives, initialVariables, t)
    def animation(self, directory, data, initialTheta1, initialTheta2, simulationTime, timestep):
        coordinates1 = np.array([data[:,5],data[:,6]])
        coordinates2 = np.array([data[:,7],data[:,8]])
        initialTheta1Degrees=np.rint((180*initialTheta1/np.pi))
        initialTheta2Degrees=np.rint((180*initialTheta2/np.pi))
        def animatePendulum(step):
            ax.clear()
            ax.plot([0, coordinates1[0][step], coordinates2[0][step]], [0, coordinates1[1][step], coordinates2[1][step]], lw=2, c='k')
            ax.plot(coordinates1[0, :step+1], coordinates1[1, :step+1], c='blue')
            ax.scatter(coordinates1[0, step], coordinates1[1,step], c='blue', marker='o')
            ax.plot(coordinates1[0,0], coordinates1[1,0], c='black', marker='o')
            ax.plot(coordinates2[0, :step+1], coordinates2[1, :step+1], c='blue')
            ax.scatter(coordinates2[0, step], coordinates2[1,step], c='blue', marker='o')
            ax.plot(coordinates2[0,0], coordinates2[1,0], c='black', marker='o')
            ax.set_xlim([-10,10])
            ax.set_ylim([-10,10])
        fig=plt.figure()
        ax=plt.axes()
        line_ani = ani.FuncAnimation(fig, animatePendulum, interval=1, frames=len(data[:,0]))
        writergif = ani.PillowWriter(fps=50)
        line_ani.save("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.gif".format(directory, self.m1, self.m2, self.l1, self.l2, int(initialTheta1Degrees), int(initialTheta2Degrees), simulationTime, int(timestep*1E3)), writer=writergif)
    def saveFits(self, directory, data, initialTheta1, initialTheta2, simulationTime, timestep):
        initialTheta1Degrees=np.rint((180*initialTheta1/np.pi))
        initialTheta2Degrees=np.rint((180*initialTheta2/np.pi))
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
            fits.Column(name="y2_pos", format="E", array=data[:,8])
            ])
        #Delete the current fits file if it exists
        if os.path.exists("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(directory, self.m1, self.m2, self.l1, self.l2, int(initialTheta1Degrees), int(initialTheta2Degrees), simulationTime, int(timestep*1E3))):
            os.remove("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(directory, self.m1, self.m2, self.l1, self.l2, int(initialTheta1Degrees), int(initialTheta2Degrees), simulationTime, int(timestep*1E3)))
                    
        #Save the new fits file
        hdu.writeto("{0}\\Simulation_Data\\double_pendulum_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,theta1={5}degrees,theta2={6}degrees,t={7}s,step={8}ms.fits".format(directory, self.m1, self.m2, self.l1, self.l2, int(initialTheta1Degrees), int(initialTheta2Degrees), simulationTime, int(timestep*1E3)))