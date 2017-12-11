

import serial
import serial.tools.list_ports
import time

class FiberShaker(object):
    """
    Write description here
    """

    def __init__(self, baud = 9600):
        """
        Finds Arduino and establishes serial connection. Adapted from: stackoverflow.com/questions/24214643
        """
        port = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Arduino' in p.description
        ]
        if not port:
            raise IOError("No Arduino Found")

        self.arduino = serial.Serial(port[0],baud)
        time.sleep(2)

    def on(self):
        """
        turns on the shaker
        """

        self.arduino.write(str(1).encode())
        print("Arduino On")

    def off(self):
        """
        turn off the shaker
        :return:
            result code
        """
        self.arduino.write(str(0).encode())
        print("Arduino Off")


    def get_status(self):
        """
        :return:
        """
        return NotImplementedError

shaker = FiberShaker()
shaker.on()
time.sleep(2)
print("waiting")
time.sleep(2)
shaker.off()
