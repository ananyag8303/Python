# To solve the SHM differential equation for different values of displacement and plot a x vs t graph
# import the required libraries
import math as mt
import matplotlib.pyplot as plt

#Ask for the input of the three variables and set up the value of a and b give the initial conditions
omega_zero = float(input("Enter the value of the angular frequency: "))
gamma = float(input("Enter the value of the gamma: "))
plot_points = 200

a = 1
#print(((gamma**2)/4) - (omega_zero**2))

plot_range = ((5*mt.pi)/omega_zero)
t = 0.0
increment = plot_range/plot_points
# print(increment)
t_data = []
x_data = []

def shm(omega_zero,gamma,t):
    while t < plot_range:
        if gamma > (2 * omega_zero):
            p = mt.sqrt(((gamma**2)/4) - (omega_zero**2))
            b = (gamma)/(2*p)
            y = mt.exp(-gamma * t/2) * (a * mt.cosh(p * t) + b * mt.sinh(p * t))
            
        elif gamma == (2 * omega_zero):
            b = gamma/2
            y = mt.exp(((-gamma * t)/2) * (a + (b * t)))
            
        else:
            omega = mt.sqrt((omega_zero**2)-((gamma**2)/4))
            b = gamma/(2 * omega)
            y = mt.exp((-gamma * t)/2) * (a*mt.cos(omega * t) + b * mt.sin(omega * t))
            
        x_data.append(y)
        t_data.append(t)
        t += increment
    return b
valueOfB = shm(omega_zero,gamma,t)
print("The value of b is", valueOfB)


plt.plot(t_data,x_data, "gx")
plt.title("Displacement vs time for a SHM oscillator")
plt.xlabel("Time(s)")
plt.ylabel("Displacement(m)")
plt.show()
