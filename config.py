from configparser import ConfigParser

config = ConfigParser()
config['GENERAL'] = {
    'Directory':'C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389',
    'SimulationTime':'1000',
    'Timestep':'0.01',
    'Method':'RK45',
    'System':'DP',
    'Multiple':'n',
    'MultipleNumber':'100'
}
config['SP'] = {
    'Mass':'1',
    'Length':'1',
    'InitialTheta':'90',
    'Initialz':'0'
}
config['DP'] = {
    'Mass1':'1',
    'Mass2':'1',
    'Length1':'1',
    'Length2':'1',
    'InitialTheta1':'90',
    'InitialTheta2':'90',
    'Initialz1':'0',
    'Initialz2':'0',
}
with open('config.ini', 'w') as configfile:
    config.write(configfile)