from configparser import ConfigParser
from choose_system import chooseSystem

def configuration():
    cfg = ConfigParser()
    cfg.read('config.ini')
    general = dict(cfg.items('GENERAL'))
    sys = general['system']
    input = {**dict(cfg.items(sys)), **general}
    return chooseSystem(sys, input)