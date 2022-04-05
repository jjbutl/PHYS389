#Import modules
from config_reader import *
from simulation import *
from analysis import *
from unit_test import *
from graphing import *

"""SETUP"""
system = configReader()

"""SIMULATIONS"""
simulateOnce(system)
#simulateMany(system)

"""ANALYSIS"""
#flipTime(system)

"""UNIT TESTS"""
#testKE(system)
#testPE(system)

"""PLOTS"""
#flipTimePlot(system)
#energyExchange(system)
#energyConservation(system)