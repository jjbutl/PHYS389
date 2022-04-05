import matplotlib.pyplot as plt
import numpy as np

def animation(system):
    table = system.loadFits()
    system.animation(table)

def flipTimePlot(system):
    table = system.loadFlip()
    flipTime = table["FlipTime"]/np.sqrt(system.l/system.g)
    initialTheta1 = table["InitialTheta1"]
    initialTheta2 = table["InitialTheta2"]
    green = flipTime < 10
    red = (flipTime >= 10) & (flipTime < 100)
    purple = (flipTime >= 100) & (flipTime < 1000)
    plt.scatter(initialTheta1[green], initialTheta2[green], color="green", marker="s", s=100)
    plt.scatter(initialTheta1[red], initialTheta2[red], color="red", marker="s", s=100)
    plt.scatter(initialTheta1[purple], initialTheta2[purple], color="purple", marker="s", s=100)
    xrange = np.linspace(-np.pi, np.pi, num=1000)
    yrange = np.linspace(-np.pi, np.pi, num=1000)
    x, y = np.meshgrid(xrange, yrange)
    equation = 3*np.cos(x) + np.cos(y) - 2
    plt.contour(x, y, equation, [0], color="k")
    plt.xlabel("Initial $\\theta_{{1}}}$")
    plt.ylabel("Initial $\\theta_{{2}}}$")
    plt.show()

def energyExchange(system):
    table = system.loadFits()
    mask = table["Time"] < 20
    time = table["Time"][mask]
    pe = table["Potential_Energy"][mask]
    ke = table["Kinetic_Energy"][mask]
    te = table["Total_Energy"][mask]
    plt.plot(time, pe)
    plt.plot(time, ke)
    plt.plot(time, te)
    plt.show()

def energyConservation(system):
    table = system.loadFits()
    time = table["Time"]
    totalEnergy = table["Total_Energy"]
    initialTotalEnergy = totalEnergy[0]
    totalEnergyError = abs(totalEnergy - initialTotalEnergy)
    plt.plot(time, totalEnergyError)
    plt.show()