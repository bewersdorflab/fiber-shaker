
import serial
import time

class FiberShaker(object):
    """
    Write description here
    """

    def __init__(self, port = 'COM3', baud = 9600):
        """
        This function should probably handle connecting to the arduino (set baud rate, port, etc.) using pyserial
        """
        self.arduino = serial.Serial(port, baud)
        time.sleep(2)

    def on(self):
        """
        turns on the shaker
        :return:
            result code
        """
        self.arduino.write(str(1).encode())

    def off(self):
        """
        turn off the shaker
        :return:
            result code
        """
        self.arduino.write(str(0).encode())

    def get_status(self):
        """

        :return:
        """
        raise NotImplementedError


shaker = FiberShaker()
shaker.on()
