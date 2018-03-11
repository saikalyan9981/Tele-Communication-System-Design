import time

import pigpio

GPIO=12

square = []

def generate( st ):

        pi = pigpio.pi()

        pi.set_mode(GPIO, pigpio.OUTPUT)

        tp = 0.1
        for b in st:
                time.sleep(tp)
                if(b=="1"):
                        pi.write(GPIO,1)
                else:
                        pi.write(GPIO,0)
        time.sleep(1)
        pi.write(GPIO,0)

#time.sleep(1)
#generate("10111001011010100110111000100000001")
