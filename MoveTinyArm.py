import serial

def moveTo(key):

    try:
        ser = serial.Serial()  # open serial port
        ser.baudrate = 9600
        ser.port = 'COM4'
        ser.open()
        # print("serial opened!")
        ser.write(key.encode())
    except:
        print("error to open serial port!")
    ser.close()             # close port