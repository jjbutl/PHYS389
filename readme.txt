#Set the directory to save files in
directory = "C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389"

#Set the simulation paramters for single pendulum (sp):
m=2 #Mass of bob m in kg
l=4 #Length of pendulum l in m
spSimulationTime = 1000 #Simulation time in s
spTimestep = 0.01 #Timestep in s
initialTheta = np.pi/2 #Initial angle theta in radians
initialz = 0 #Initial z (angular velocity) in rad*s^-1
spInput = [m,l,initialTheta,initialz,spSimulationTime,spTimestep,directory]

#Set the simulation paramters for double pendulum (dp):
m1=1 #Mass of bob m1 in kg
m2=1 #Mass of bob m2 in kg
l1=1 #Length of pendulum l1 in m
l2=1 #Length of pendulum l2 in m
dpSimulationTime = 100 #Simulation time in s
dpTimestep = 0.01 #Timestep in s
initialTheta1 = 0 #Initial angle theta1 in radians
initialTheta2 = 0 #Initial angle theta2 in radians
initialz1 = 1 #Initial z1 (angular velocity) in rad*s^-1
initialz2 = 1 #Initial z2 (angular velocity) in rad*s^-1
dpInput = [m1,m2,l1,l2,initialTheta1,initialTheta2,initialz1,initialz2,dpSimulationTime,dpTimestep,directory]

sys = "sp" #Choose "sp" for single pendulum or "dp" for double pendulum