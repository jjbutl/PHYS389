#Import modules
from abc import ABC, abstractmethod

#Create abstract class for an n-pendulum
class GeneralPendulum(ABC):
    @abstractmethod
    def derivatives(self):
        pass
    @abstractmethod
    def kineticEnergy(self):
        pass
    @abstractmethod
    def potentialEnergy(self):
        pass
    def totalEnergy(self,kinetic,potential):
        return kinetic + potential