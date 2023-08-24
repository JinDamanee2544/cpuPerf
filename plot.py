from matplotlib import pyplot as plt

with open("cpu_test.txt", "r") as f:
    lines = f.readlines()
    xList = []
    yList = []
    for line in lines:
        line = line.strip()
        x,y = line.split(", ")
        xList.append(int(x))
        yList.append(float(y))
    plt.plot(xList, yList)
    plt.xlabel("Loop Count")
    plt.ylabel("Time (s)")
    plt.title("CPU Test")


plt.savefig("cpu_test.png")  