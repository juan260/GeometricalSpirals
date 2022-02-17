import numpy as np
import matplotlib.pyplot as plt

def geometricSpiral(initialLength, growth, rotationChange, \
        repetitions, name):
    brushPosition = [0.0,0.0]
    nextPosition = [0.0,0.0]
    lineLength = initialLength
    rotation = 0
    for i in range(repetitions):
        nextPosition[0] = brushPosition[0] + lineLength * np.cos(rotation)
        nextPosition[1] = brushPosition[1] + lineLength * np.sin(rotation)
        plt.plot([brushPosition[0], nextPosition[0]], \
             [brushPosition[1], nextPosition[1]])
        

        lineLength *= growth
        rotation = np.fmod(rotationChange+rotation, 2*np.pi)
        #print(rotation)
        brushPosition[0] = nextPosition[0]
        brushPosition[1] = nextPosition[1]
    plt.show()
geometricSpiral(1, 1.1, np.pi*(1-1.0/3.0), 1000, "Hola")