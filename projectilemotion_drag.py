#Import the required libraries 
import math as mt
import matplotlib.pyplot as plt
def main():
#Ask for required inputs from the user
    v_o = float(input("Enter the initial velocity of the particle: "))
    theta = float(input("Enter the launch angle of the particle: "))
    drag = float(input("Enter the drag coefficient of the particle: "))
    del_t = float(input("Enter the time interval: "))
#Define the set values needed for the calculation
    g = 9.81
#Setting up lists to store the changing variables
    t = [0]
    x = [0]
    y = [0]
#Velocity components
    vx = [v_o*mt.cos(theta/180*mt.pi)]
    vy = [v_o*mt.sin(theta/180*mt.pi)]
# Acceleration components
    ax = [(-drag) * v_o * (v_o*mt.cos(theta/180*mt.pi))] 
    ay = [(-drag) * v_o * (v_o*mt.sin(theta/180*mt.pi)) - g]
    #print(vx,vy,ax,ay)
#Now using Euler method to plot successive points on a graph
    counter = 0
    while (y[counter] >= 0):                   
        t.append(t[counter]+del_t)                 
    # Update velocity
        vx.append(vx[counter]+del_t*ax[counter])  
        vy.append(vy[counter]+del_t*ay[counter])
    # Update position
        x.append(x[counter]+del_t*vx[counter])    
        y.append(y[counter]+del_t*vy[counter]) 
    
        vel = mt.sqrt(vx[counter]**2 + vy[counter]**2)   # magnitude of velocity  
        ax.append((-drag) * vel * (vx[counter]))     
        ay.append((-drag) * vel * (vy[counter]) - g)
    # Increment the counter by 1
        counter = counter + 1

    plt.plot(x,y)
    plt.ylabel("y (m)")
    plt.xlabel("x (m)")
    plt.show()
    
    print("Range of projectile is {:3.1f} m".format(x[counter]))
main()
   
# The last value of x should give the range of the projectile approximately.
