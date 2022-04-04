#Import modules
from config_reader import configReader
from simulation import simulationOnce, simulationMany
from analysis import flipTime
from graphing import flipTimePlot
import numpy as np

system = configReader()
system.simulationTime = 1000*np.sqrt(system.l1/system.g)
system.t = np.arange(0, system.simulationTime+system.timestep, system.timestep)
#system.makeDirectory()
#simulationOnce(system) #Simulate the system and create the data file
#simulationMany(system)
flipTime(system)