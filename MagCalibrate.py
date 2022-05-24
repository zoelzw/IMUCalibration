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

def raw1():
    b = np.array([-12.825291, -17.877001, -42.370841])
    # A = np.array([[0.861066,0.015673,-0.009393],
    #             [0.015673,0.811777,-0.003197],
    #             [-0.009393,-0.003197,0.916904]])
    A = np.array([[1.068760,-0.020584,0.107276],
            [-0.020584,1.195409,0.064189],
            [0.107276,0.064189,1.181860]])
    File = "raw1"
    FileName = "Data/" + File + ".txt"
    x1,y1,z1,x,y,z =CalibrateMag(File,b,A,log=False)
    title ="Hard and Soft Iron Compensation Calibration Results: " + File
    comparePlot(x,y,z,x1,y1,title)

def raw2():
    b = np.array([1.971420, -28.633755, -47.897918])
    A = np.array([[0.813361,0.015617,-0.000395],
                [0.015617,0.774898,-0.026269],
                [-0.000395,-0.026269,0.848409]])
    # A = np.array([[1.229943,-0.024794,-0.000195],
    #         [-0.024794,1.292348,0.040003],
    #         [-0.000195,0.040003,1.179916]])
    File = "raw2"
    FileName = "Data/" + File + ".txt"
    x1,y1,z1,x,y,z =CalibrateMag(File,b,A,log=False)
    title ="Hard and Soft Iron Compensation Calibration Results: " + File
    comparePlot(x,y,z,x1,y1,title)

def raw3():
    b = np.array([-41.075228, -19.023585, 1.356729])
    # A = np.array([[0.638605,0.016837,-0.130269],
    #             [0.016837,0.607712,-0.045542],
    #             [-0.130269,-0.045542,0.834717]])
    A = np.array([[1.617812,-0.026007,0.251062],
            [-0.026007,1.652689,0.086111],
            [0.251062,0.086111,1.641890]])
    File = "raw3"
    FileName = "Data/" + File + ".txt"
    x1,y1,z1,x,y,z =CalibrateMag(File,b,A,log=False)
    title ="Hard and Soft Iron Compensation Calibration Results: " + File
    comparePlot(x,y,z,x1,y1,title)

def main():
    raw()
    # raw1()
    # raw2()
    # raw3()

if __name__ == "__main__":
    main()
