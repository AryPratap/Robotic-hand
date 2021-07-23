import serial
import time
import logging

class SerialObject:
   
    def __init__(self, portNo, baudRate=9600, digits=1):
       
        self.portNo = portNo
        self.baudRate = baudRate
        self.digits = digits
        try:
            self.ser = serial.Serial(self.portNo, self.baudRate)
            print("Serial Device Connected")
        except:
            logging.warning("Serial Device Not Connected")

    def sendData(self, data):
        
        myString = "$"
        for d in data:
            myString += str(int(d)).zfill(self.digits)
        try:
            self.ser.write(myString.encode())
            return True
        except:
            return False

    def getData(self):
       
        data = self.ser.readline()
        data = data.decode("utf-8")
        data = data.split('#')
        dataList = []
        [dataList.append(d) for d in data]
        return dataList[:-1]
