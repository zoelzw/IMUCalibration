"""
calibrate magnetometer measurements 
h_calibrated = A * (h_raw - b)
reference: https://www.mathworks.com/help/fusion/ug/magnetometer-calibration.html
"""
import numpy as np 
import MagPlot

data = np.loadtxt("raw.txt")

def CalibratePlot(b,A,title):
    calibrated = np.dot(data-b,A) 
    x1 = calibrated[:,0]
    y1 = calibrated[:,1]
    z1 = calibrated[:,2]
    MagPlot.dataPlot(x1,y1,z1,title)


# Offset-Only: Hard Iron Compensation
# Many MEMS magnetometers have registers to compensate for the hard iron offset (x-b). 
# When only a hard iron offset compensation is needed, A becomes the identity matrix

b = np.array([28.557458, -39.981060, -27.428035])
A = np.identity(3)
CalibratePlot(b,A,"Hard Iron Compensation Calibration Results")


# Axis Scaling Computation: Soft Iron Compensation

b = np.zeros(3)
A = np.array([[1,1,1],[1,1,1],[1,1,1]])
CalibratePlot(b,A,"Soft Iron Compensation Calibration Results")

# Both
b = np.array([28.557458, -39.981060, -27.428035])
A = np.array([[1,1,1],[1,1,1],[1,1,1]])
CalibratePlot(b,A,"Hard and Soft Iron Compensation Calibration Results")