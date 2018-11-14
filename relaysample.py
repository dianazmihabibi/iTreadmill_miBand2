import time

start = time.time()
print (start)
time.sleep(5)
elapsed = time.time() - start
elapsed = int(elapsed)
##time = (end - start) / 60
##time = round(time,1)
##data = time.strftime("%H %M %S", time.gmtime(elapsed))
##print (data)
##data = int(data)
##data = data * 25.5
print (elapsed)