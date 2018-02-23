

import serial
import serial.tools.list_ports
import time

class FiberShaker(object):
    """
    Write description here
    """

    def __init__(self, port=None, baud=9600):
        """

        Finds Arduino and establishes serial connection. Adapted from: stackoverflow.com/questions/24214643

        Parameters
        ----------
        port : str
            com port id, e.g. 'COM8'
        baud : int
            baud rate to connect at
        """
        if not port:
            # try to find arduino automatically
            ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if (('Arduino' in p.description) or ('ACM' in p.description))
            ]
            try:
                port = ports[0]
            except IndexError:
                raise IOError("No Arduino Found")

        self.arduino = serial.Serial(port, baud)
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
        """
        self.arduino.write(str(0).encode())
        print("Arduino Off")


    def get_status(self):
        return NotImplementedError

if __name__ == '__main__':
    shaker = FiberShaker()
    shaker.on()

