"""
calibrate magnetometer measurements 
h_calibrated = A * (h_raw - b)
reference: https://www.mathworks.com/help/fusion/ug/magnetometer-calibration.html
"""
import numpy as np 
import MagPlot
import matplotlib.pyplot as plt 
import csv


def CalibrateMag(File,b,A,log=False):
    FileName = "Data/" + File + ".txt"
    data = np.loadtxt(FileName)
    x,y,z = MagPlot.dataRead(FileName)
    calibrated = np.dot(data-b,A) 
    x1 = calibrated[:,0]
    y1 = calibrated[:,1]
    z1 = calibrated[:,2]
    
    if log:
        n = int(np.size(calibrated)/3)
        for i in range(n):
            with open("Data/" + File + "Cali.txt", 'a', newline='') as f:
                writer = csv.writer(f, delimiter='\t')
                writer.writerow([calibrated[i, 0], calibrated[i, 1], calibrated[i, 2]])
        print("Done Logging")
    return x1,y1,z1,x,y,z

def comparePlot(x,y,z,x1,y1,title):
    # MagPlot.dataPlot(x,y,z,title)
    MagPlot.twoDPlot(x1,y1,title+" xy plane")

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.scatter(x,y, color = "r",label='raw')
    ax.scatter(x1,y1, color = "g",label='calibrated')
    ax.set_title("Comparison "+title)
    ax.set_xlabel("x (uT)")
    ax.set_ylabel("y (uT)")
    plt.xlim([-80,80])
    plt.ylim([-80,80])
    plt.legend()
    plt.show()

def comparePlot3D(x,y,z,x1,y1,z1,title):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax = plt.axes(projection = "3d")
    ax.scatter(x,y,z, color = "r",label='raw')
    ax.scatter(x1,y1,z1, color = "g",label='calibrated')
    ax.set_title("3D Comparison Plot: " + title)
    ax.set_xlabel("x (uT)")
    ax.set_ylabel("y (uT)")
    ax.set_zlabel("z (uT)")
    plt.legend()
    plt.xlim([-80,80])
    plt.ylim([-80,80])
    # plt.zlim([-80,80])
    plt.show()
# Offset-Only: Hard Iron Compensation
# Many MEMS magnetometers have registers to compensate for the hard iron offset (x-b). 
# When only a hard iron offset compensation is needed, A becomes the identity matrix

def raw():
    b = np.array([5.536110, -29.455782, -50.467525])
    A = np.array([[0.861066,0.015673,-0.009393],
                [0.015673,0.811777,-0.003197],
                [-0.009393,-0.003197,0.916904]])
    # A = np.array([[1.161888,-0.022386,0.011825],
    #         [-0.022386,1.232314,0.004067],
    #         [0.011825,0.004067,1.090762]])
    File = "raw"
    FileName = "Data/" + File + ".txt"
    x1,y1,z1,x,y,z =CalibrateMag(File,b,A,log=False)
    title ="Hard and Soft Iron Compensation Calibration Results: " + File
    comparePlot(x,y,z,x1,y1,title)
    comparePlot3D(x,y,z,x1,y1,z1,title)

def main():
    raw()
    # raw1()
    # raw2()
    # raw3()

if __name__ == "__main__":
    main()
