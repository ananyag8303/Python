#To create a graoh for power vs time for a circuit using an external file

import numpy as np
import math
import matplotlib.pyplot as plt

current_data = []
voltage_data = []
power_data = []
filepath = input("Enter the filepath name: ")
with open(filepath,"r") as f:
    data = f.readlines()
    data = data[3:]
    
    for i in data:
        reading = eval(i[:-2])
        
        current_data.append((reading[0]))
        
        voltage_data.append((reading[1]))

time = np.arange(0,len(current_data)*0.00004, 0.00004)

def logpower(voltage,current):
    for i in range (len(current_data)):
        power_data.append(math.log(current_data[i]*voltage_data[i]))

logpower(voltage_data, current_data)


plt.plot( time, power_data)
plt.title("Log of power vs time")
plt.xlabel("Time(s)")
plt.ylabel("Displacement(m)")
plt.show()
