from configparser import ConfigParser
import numpy as np

def simulationOnce(system):
    variables = system.integrate()
    data = system.data(variables)
    system.saveFits(data)

def simulationMany(system):
    cfg = ConfigParser()
    cfg.read('config.ini')
    general = dict(cfg.items('GENERAL'))
    sys = general['system']
    if sys == "SP":
        initialTheta = cfg[sys]['initialtheta']
        num = cfg['GENERAL']['multiplenumber']
        initialThetaRange = np.linspace(-float(initialTheta), float(initialTheta), num=float(num))
    for x in len(initialThetaRange):
        system.initialThetaDegrees = initialThetaRange[x]
        system.initialTheta = np.pi*system.initialThetaDegrees/180
        variables = system.integrate()
        data = system.data(variables)
        system.saveFlip(data)

def animation(system):
    table = system.openFits()
    system.animation(table)