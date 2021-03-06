'''
3D Scatter plot showing magnetometer readings
'''
from matplotlib import projections
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats
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
 

def twoDPlot(parameter1,parameter2,title):
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes()
    ax.scatter(parameter1,parameter2, color = "r")
    ax.set_title(title)
    ax.set_xlabel("x (uT)")
    ax.set_ylabel("y (uT)")
    plt.show()
    # return 
def remove_outliers(arr, k):
    mu, sigma = np.mean(arr, axis=0), np.std(arr, axis=0, ddof=1)
    return arr[np.all(np.abs((arr - mu) / sigma) < k, axis=1)]

def main():
    FILENAME = "Data/raw3.txt"
    x,y,z = dataRead(FILENAME)
    # data = np.loadtxt("Data/raw1.txt")
    # nodata = remove_outliers(data,2)
    # x = nodata[:,0]
    # y = nodata[:,1]
    # z = nodata[:,2]
    
    
    title = "Magentometer Raw Readings"
    dataPlot(x,y,z,title)
    twoDPlot(x,y,title+" xy plane")
    twoDPlot(x,z,title+" xz plane")
    twoDPlot(y,z,title+" yz plane")

if __name__ == "__main__":
    main()