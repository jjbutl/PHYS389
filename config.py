from configparser import ConfigParser

config = ConfigParser()
config['GENERAL'] = {
    'Directory':'C:\\Users\\joebu\\OneDrive\\Documents\\PHYS389\\PHYS389',
    'SimulationTime':'1000',
    'Timestep':'0.01',
    'Method':'RK45',
    'System':'TEST_DP',
    'Multiple':'n',
    'MultipleNumber':'30'
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
    'InitialTheta1':'180',
    'InitialTheta2':'180',
    'Initialz1':'0',
    'Initialz2':'0',
}
config['TEST_SP'] = {
    'Mass':'1',
    'Length':'1',
    'InitialTheta':'90',
    'Initialz':'0'
}
config['TEST_DP'] = {
    'Mass1':'1',
    'Mass2':'1',
    'Length1':'1',
    'Length2':'1',
    'InitialTheta1':'180',
    'InitialTheta2':'180',
    'Initialz1':'0',
    'Initialz2':'0',
}
with open('config.ini', 'w') as configfile:
    config.write(configfile)