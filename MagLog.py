import time 
import csv
import numpy as np
import serial 
import serial.tools.list_ports

HANDSHAKE = 0
STREAM = 1
timeout = 1

def find_ESP32(port=None):
    """find serial port connected to the ESP32"""
    if port is None:
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if port.manufacturer is not None and "Silicon Labs" in port.manufacturer:
                ESP32Port = port.device
    return ESP32Port

def handshake_ESP32(ESP32, sleep_time =1, print_message = True, handshake_code = 0):
    """testing connections with ESP32"""
    #initializing
    ESP32.close()
    ESP32.open()
    time.sleep(sleep_time)

    #set long timeout to establish handshake 
    timeout = ESP32.timeout
    ESP32.timeout = 2


    #discard junk in the input buffer 
    _ = ESP32.read_all()

    #request 
    ESP32.write(bytes([handshake_code]))
    #read
    handshake_message = ESP32.read_until()
    #repeat
    ESP32.write(bytes([handshake_code]))
    handshake_message = ESP32.read_until()

    #optional to print the handshake message
    if print_message:
        print("Handshake established: " + handshake_message.decode())
    #reset timeout
    # ESP32.timeout = timeout
    return 

def dataParser(raw):
    raw = raw.decode()
    if raw[-1] != "\n":
        raise ValueError(
            "Input must end with newline, otherwise message is incomplete."
        )
    x,y,z = raw.rstrip().split(",")
    return x,y,z

def dataStream(ESP32):
    SAMPLE_FREQ = 100 #hz
    SAMPLE_TIME = 30 #s
    sample_delay = 1/SAMPLE_FREQ
    N = int(SAMPLE_FREQ*SAMPLE_TIME)
    #Initialize output
    measurements = np.zeros((N, 3), dtype='float')
    #turn on stream 
    ESP32.write(bytes([STREAM]))
    print("starting streaming!")
    i = 0
    while i < N:
        raw = ESP32.read_until()
        try:
            x,y,z = dataParser(raw)
            i += 1
            time.sleep(sample_delay)
            measurements[i,0] = x
            measurements[i,1] = y
            measurements[i,2] = z
            ESP32.write(bytes([STREAM]))
        except:
            pass 
    return measurements

def dataLog(measurements,FILE):
    print('Writing data to {} ...'.format(FILE))
    N = int(np.size(measurements)/3)
    for i in range(N):
        with open(FILE, 'a', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow([measurements[i, 0], measurements[i, 1], measurements[i, 2]])

def dataplot(measurements,PIC):
    print("plotting data")


def main():
    port = find_ESP32()
    ESP32 = serial.Serial(port,baudrate=115200)
    handshake_ESP32(ESP32, handshake_code=HANDSHAKE, print_message=True)

    #stream to get measurements
    measurements = dataStream(ESP32)
    print(measurements)
    #log data 
    dataLog(measurements,"raw.txt")
if __name__ == "__main__":
    main()
