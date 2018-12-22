import os
import sys
import time
import datetime

waktu = []
bpm = []
step = []

def read():
    global waktu
    global bpm
    global step
    global data
    graph_data = open('log.txt', 'r',os.O_NONBLOCK).read()
    lines = graph_data.split('\n')
    batas = len(lines)-2

    for line in lines:
##    for line in lines:
        if len(line)>= 1:
            a, b, c = line.split(',')
            waktu.append(str(a))
            bpm.append(str(b))
            step.append(str(c))
            
    print (bpm, len(bpm))

read()
    

