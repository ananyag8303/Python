#Import the required libraries 
import math as mt
import matplotlib.pyplot as plt
def main():
    #Ask for the required input values
    v_o = float(input("Enter the initial velocity of the particle: "))
    drag = float(input("Enter the drag coefficient of the particle: "))
    del_t = float(input("Enter the time interval: "))
#     v_o = 10
#     drag = 0.02
#     del_t =0.001
    #Define the set values needed for the calculation
    g = 9.81
    #Setting up lists to store the changing variables
    theta = [0]
    y_data = [0]
    #set up for loop to make a list of theta values
    for i in range(1,91):
        theta.append(i)
        t = [0]
        x = [0]
        y = [0]
        vx = [v_o*mt.cos(theta[i]/180*mt.pi)]
        vy = [v_o*mt.sin(theta[i]/180*mt.pi)]
        ax = [(-drag) * v_o * (v_o*mt.cos(theta[i]/180*mt.pi))] 
        ay = [(-drag) * v_o * (v_o*mt.sin(theta[i]/180*mt.pi)) - g]
        #set up a while loop to calculate the velocity values and pick out the last values
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
        #Velocity magnitude and acceleration update
            vel = mt.sqrt(vx[counter+1]**2 + vy[counter+1]**2)
            ax.append((-drag) * vel * (vx[counter]))     
            ay.append((-drag) * vel * (vy[counter]) - g)
        # Increment the counter by 1
            counter = counter + 1
        v2 = (vx[counter-1] ** 2) + (vy[counter-1] ** 2)
        y_data.append(v2/(v_o**2))
        
    plt.plot(theta[1::],y_data[1::])
    plt.ylabel("Ratio")
    plt.xlabel("Launch angle")
    plt.show()

main()
    
