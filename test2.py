import os
fp = open('log.txt', 'r', os.O_NONBLOCK).read()
lines = fp.split('\n')

waktu = []
bpm = []
step = []

for line in lines:
    if len(line)>= 1:
         a, b, c = line.split(',')
    
    waktu.append(str(a))
    bpm.append(str(b))
    step.append(str(c))

numbering = []
selector = []

for min in range (0, len(bpm), 60):
    selector.append(int(bpm[min]))
    numbering.append(len(selector))
##    print (numbering, selector)

    average = int(sum(selector) / len(selector))
    print (max(selector), average)

##    print(bpm)
##    selector.append(str(min))
##    print (selector)
##    print (len(bpm))

##for all in range (0, len(selector)):
##    print bpm[selector[]]