import numpy as np

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
                flipTime = 1000
            data = np.append(data, np.array([[system.initialTheta1, system.initialTheta2, flipTime]]), axis=0)
    system.saveFlip(data)
    
