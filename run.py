#Import modules
from configuration import configuration
from simulation import simulationOnce, simulationMany

system = configuration()
#simulationOnce(system) #Simulate the system and create the data file
simulationMany(system)