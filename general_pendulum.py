#Import modules
from abc import ABC, abstractmethod
from scipy.integrate import odeint
import numpy as np

#Create abstract class for an n-pendulum
class GeneralPendulum(ABC):
    @abstractmethod
    def derivatives(self):
        pass
    @abstractmethod
    def data(self):
        pass
    def kineticEnergy(self,m,v_squared):
        return 0.5*m*v_squared
    def potentialEnergy(self,m,y):
        return m*self.g*y
    def integrate(self):
        #Numerically integrate the equations of motion
        return odeint(self.derivatives, self.initialVariables, self.t)
    def totalEnergy(self,kinetic,potential):
        return kinetic + potential
    @abstractmethod
    def saveFits(self):
        pass
    @abstractmethod
    def openFits(self):
        pass
