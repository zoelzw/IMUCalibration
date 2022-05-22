import time 
import csv
import numpy as np
import serial 
import serial.tools.list_ports

def find_ESP32(port=None):
    """find serial port connected to the ESP32"""
    if port is None:
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.manufacturer is not None and "Silicon Labs" in port.manufacturer:
                ESP32Port = port.device
    return ESP32Port

def dataParser(raw):
    raw = raw.decode()

    if raw[-1] != "\n":
        raise ValueError(
            "Input must end with newline, otherwise message is incomplete."
        )
    x,y,z = raw.rstrip().split(",")
    return x,y,z

def dataStream(ESP32):
    SAMPLE_FREQ = 10 #hz
    SAMPLE_TIME = 5 #s
    N = int(SAMPLE_FREQ*SAMPLE_TIME)
    #Initialize output
    measurements = np.zeros((N, 3), dtype='float')

    i = 0
    while i < N:
        raw = ESP32.read_until()
        try:
            x,y,z = dataParser(raw)
            measurements[i,0] = x
            measurements[i,1] = y
            measurements[i,2] = z
            i += 1
        except:
            pass 
    ESP32.Close()
    print("Sensor Reading Complete")
    return measurements

def dataLog(measurements,FILE):
    print('Writing data to {} ...'.format(FILE))
    N = np.size(measurements)
    for i in range(N):
        with open(FILE, 'a', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow([measurements[i, 0], measurements[i, 1], measurements[i, 2]])
    print("done")

def main():
    port = find_ESP32()
    ESP32 = serial.Serial(port,baudrate=9600)
    

if __name__ == "__main__":
    main()
