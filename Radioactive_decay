# OOP code to simulate radioactoive decay

import random
import numpy as np
import math as mt
#Defining an outer class for the phenomenon of radioactivity
class Radioactive(object):
    '''This constructor is used to set the initial parameters of time step, initial number of undecayed nuclie and the
    decay constant. It is also going to be used to create the 2D array with size N*N'''
    def __init__(self):
    #Ask for user input on timestep and undecayed nuclei
        self.delt = float(input("Enter the value of the time step for this experiment: "))
        self.N_initial = int(input("Enter the value of the undecayed nuclei for this experiment: "))
        self.decay_constant = float(input("Enter the value of the decay constant for this experiment: "))
        self.p = (self.decay_constant) * self.delt
        self.grid = []
        for i in range(self.N_initial):
            self.grid.append([1]*self.N_initial)
    '''This fucntion will now count the number of undecayed nuclei in the 2D array created above '''
    def counter(self):
        counter_1 = 0
        for i in range(self.N_initial):
            for j in range (self.N_initial):
                if self.grid[i][j] == 1:
                    counter_1 += 1
        return counter_1
    '''This function will now decay nuclei in this 2D at random using the python random() fucntion. It will also be 
    used to calculate the time it takes for the entire 2D array to have half the number of undecayed nuclei'''
    def experiment(self):
        boundary = (self.N_initial * self.N_initial)//2
        timestep = 0
        while (self.counter() > boundary):
#             print(self.counter())
#             print(self.grid)
            timestep += 1
            for i in range(self.N_initial):
                for j in range(self.N_initial):
                    myrand = random.random()
#                     print((i,j,self.p,myrand))
                    if self.grid[i][j] == 1 and self.p > myrand:
                        self.grid[i][j] = 0
#         return timestep*self.delt, self.counter(), self.grid
        print("The simualted half life is",timestep*self.delt, 
              ".The number of undecayed nuclei is ",self.counter( ), 
              ".The real half life is 24.98. "
              "The final grid is",self.grid)

def main():
    Iodine_28 = Radioactive()
    counter = Iodine_28.counter()
    experiment = Iodine_28.experiment()
#     print(counter)
    print(experiment)
main()
