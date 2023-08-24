import time

LOOP_COUNT = 50000

timeDict = {}
timeDict[0]=0
start = time.time_ns()
for i in range (1,LOOP_COUNT+1):
    timeDict[i] = time.time_ns()-start

with open("cpu_test.txt", "w") as f:
    for k,v in timeDict.items():
        f.write(format(k, 'd') + ", " + format(v/1e9, 'f') + "\n")

