"""
calibrate magnetometer measurements 
h_calibrated = A * (h_raw - b)
reference: https://www.mathworks.com/help/fusion/ug/magnetometer-calibration.html
"""
import numpy as np 
import MagPlot
import matplotlib.pyplot as plt 
import csv
data = np.loadtxt("Data/raw.txt")


def CalibratePlot(b,A,title):
    # calibrated = np.dot(data-b,A) 
    N = len(data)
    calibrated = np.zeros((N, 3), dtype='float')
    for i in range(N):
        row = np.array([data[i, 0], data[i, 1], data[i, 2]])
        calibrated[i, :] = A @ (row - b)
    # print(calibrated)
    x1 = calibrated[:,0]
    y1 = calibrated[:,1]
    z1 = calibrated[:,2]
   
    # n = int(np.size(calibrated)/3)
    # for i in range(n):
    #     with open("Data/"+title + ".txt", 'a', newline='') as f:
    #         writer = csv.writer(f, delimiter='\t')
    #         writer.writerow([calibrated[i, 0], calibrated[i, 1], calibrated[i, 2]])

    MagPlot.dataPlot(x1,y1,z1,title)
    MagPlot.twoDPlot(x1,y1,title+" xy plane")


# Offset-Only: Hard Iron Compensation
# Many MEMS magnetometers have registers to compensate for the hard iron offset (x-b). 
# When only a hard iron offset compensation is needed, A becomes the identity matrix

b = np.array([5.536110, -29.455782, -50.467525])
A = np.identity(3)
CalibratePlot(b,A,"Hard Iron Compensation Calibration Results")


# # Axis Scaling Computation: Soft Iron Compensation

b = np.zeros(3)
A = np.array([[0.000862,0.000016,-0.000009],[0.000016,0.000813,-0.000003],[-0.000009,-0.000003,0.000918]])
CalibratePlot(b,A,"Soft Iron Compensation Calibration Results")

# Both
b = np.array([5.536110, -29.455782, -50.467525])
A = np.array([[0.000862,0.000016,-0.000009],[0.000016,0.000813,-0.000003],[-0.000009,-0.000003,0.000918]])
CalibratePlot(b,A,"Hard and Soft Iron Compensation Calibration Results")
