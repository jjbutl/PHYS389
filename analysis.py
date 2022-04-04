import numpy as np
from astropy.io import fits

def flipTime(system):
    initialTheta1, initialTheta2 = system.loadInitialRange()
    data = np.zeros((0,3))
    for x in range(len(initialTheta1)):
        print(x)
        system.updateInitialTheta1(initialTheta1, x)
        for y in range(len(initialTheta2)):
            print(y)
            system.updateInitialTheta2(initialTheta2, y)
            system.initialVariables = np.array([system.initialTheta1, system.initialTheta2, system.initialz1, system.initialz2])
            timescale = np.sqrt(system.l1/system.g)
            t = system.loadFits()
            time = t['Time']
            if (abs(abs(t["Theta1"][0]) - np.pi) <= 1e-1) and (abs(abs(t["Theta2"][0]) - np.pi) <= 1e-1):
                start = 2
            elif (abs(abs(t["Theta1"][0]) - np.pi) <= 1e-1) or (abs(abs(t["Theta2"][0]) - np.pi) <= 1e-1):
                start = 0.2
            else:
                start = 0
            mask = (time > start) & ((abs(abs(t["Theta1"]) - np.pi) <= 1e-1) | (abs(abs(t["Theta2"]) - np.pi) <= 1e-1))
            timeMasked = time[mask]
            if len(timeMasked) != 0:
                flipTime = timeMasked[0]/timescale
            else:
                flipTime = 10000
            data = np.append(data, np.array([[system.initialTheta1, system.initialTheta2, flipTime]]), axis=0)
    hdu=fits.BinTableHDU.from_columns(
        [fits.Column(name="InitialTheta1", format="E", array=data[:,0]),
        fits.Column(name="InitialTheta2", format="E", array=data[:,1]),
        fits.Column(name="FlipTime", format="E", array=data[:,2])
        ])
    file = "{0}\\Simulation_Data\\dp_m1={1}kg,m2={2}kg,l1={3}m,l2={4}m,t={5}s,step={6}ms\\dp_flip.fits".format(system.directory, system.m1, system.m2, system.l1, system.l2, int(system.simulationTime), int(system.timestep*1E3))
    hdu.writeto(file, overwrite="True")
    
