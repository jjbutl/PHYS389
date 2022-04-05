#Import modules
from abc import ABC, abstractmethod
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

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
        return solve_ivp(self.derivatives, [0,self.simulationTime],self.initialVariables,method=self.method, t_eval=self.t, rtol=1e-8, atol=1e-8).y
    def totalEnergy(self,kinetic,potential):
        return kinetic + potential
    @abstractmethod
    def saveFits(self):
        pass
    @abstractmethod
    def loadFits(self):
        pass
