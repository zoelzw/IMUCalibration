'''
3D Scatter plot showing magnetometer readings
'''
from matplotlib import projections
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 

# prepare data 
def dataRead(FILENAME):
    x = np.loadtxt(FILENAME)[:,0]
    y = np.loadtxt(FILENAME)[:,1]
    z = np.loadtxt(FILENAME)[:,2]
    return x,y,z

def dataPlot(x,y,z,title):
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection = "3d")

    ax.scatter3D(x,y,z, color = "r")
    ax.set_title(title)
    ax.set_xlabel("x (uT)")
    ax.set_ylabel("y (uT)")
    ax.set_zlabel("z (uT)")
    plt.show()

def main():
    FILENAME = "raw.txt"
    x,y,z = dataRead(FILENAME)

    dataPlot(x,y,z,"Magentometer Raw Readings")

if __name__ == "__main__":
    main()