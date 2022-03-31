def simulation(system):
    variables = system.integrate()
    data = system.data(variables)
    system.saveFits(data)

def animation(system):
    table = system.openFits()
    system.animation(table)