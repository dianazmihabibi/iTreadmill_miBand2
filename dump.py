import sys
import os
import time
import datetime
from base import MiBand2
from bluepy.btle import BTLEException

#Mi Band MAC = 'D6:EC:F2:B3:70:BA'
##currentDT = datetime.datetime.now()
MAC = 'D6:EC:F2:B3:70:BA'
#filepath = sys.argv[2]
##if os.path.exists(sys.argv[2]):
##    os.remove(sys.argv[2])
##fp = open('log.txt', 'a', os.O_NONBLOCK)
        
def log(rate):
##    n=0
##    if os.path.exists('log.txt'):
##        n += 1
##        filename = 'log'+ str(n) + '.txt'
    
    fp = open('log.txt', 'a', os.O_NONBLOCK)
    step = band.get_steps()
    currentDT = datetime.datetime.now()
    
##    filter data karena di atas 127 menjadi negatif
    ind=0
    tmp=0
    rate = int(rate)
    
    if rate < 0:
        tmp = rate
        ind = 130 - abs(rate)
        rate = ind * 2 + abs(rate)
##        print ("this is negative")
    
##    rate = 0
    data = "%s,%s,%s\n" % (currentDT.strftime("%d-%m-%Y %H:%M:%S"), rate, step)
    fp.write(data)
    print (data)
    fp.close()
    
    return log

while True:
    try:
        band = MiBand2(MAC, debug=True)
        band.setSecurityLevel(level="low")
        band.authenticate()
        band.initialize()
        band.start_heart_rate_realtime(heart_measure_callback=log)
        band.disconnect()
    except BTLEException:
        pass
