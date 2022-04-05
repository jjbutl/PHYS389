import numpy as np

def simulateOnce(system):
    variables = system.integrate()
    data = system.data(variables)
    system.saveFits(data)

def simulateMany(system):
    if system.system == "SP":
        system.createInitialRange()
        initialRange = system.loadInitialRange()
        for x in range(len(initialRange)):
            print(x)
            system.updateInitialRange
            system.initialVariables = np.array([system.initialTheta, system.initialz])
            simulateOnce(system)
    elif system.system == "DP":
        system.createInitialRange()
        initialTheta1, initialTheta2 = system.loadInitialRange()
        for x in range(len(initialTheta1)): #len(initialTheta1)
            print(x)
            system.updateInitialTheta1(initialTheta1, x)
            for y in range(len(initialTheta2)): #len(initialTheta2)
                print(y)
                system.updateInitialTheta2(initialTheta2, y)
                system.initialVariables = np.array([system.initialTheta1, system.initialTheta2, system.initialz1, system.initialz2])
                simulateOnce(system)
    else:
        print("Please enter a valid system (SP or DP).")