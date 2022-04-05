from configparser import ConfigParser
from choose_system import chooseSystem

def configReader():
    cfg = ConfigParser()
    cfg.read('config.ini')
    general = dict(cfg.items('GENERAL'))
    sys = general['system']
    input = {**dict(cfg.items(sys)), **general}
    system = chooseSystem(sys, input)
    system.makeDirectory()
    return system