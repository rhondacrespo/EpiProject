#rhonda crespo, carlos phillips
#april 25, 2020
#this is a simple epidemiology model using the SIR model developed by
#Kermack & McKendrick in 1927. S stands for Susceptible, I is for
#Infected, and R stands for Removed (either recovered or
#dead). Removed are assumed to not be susceptible to the disease
#again. The goal of the model is provide information as to the rate of
#infection in a population for medical experts and
#policymakers. Further implementation would incorporate how to reduce
#infection rate (immunization, social distancing, medicine, etc).
#Honor Code: We pledge that this program represents our own program
#code. We received no help in designing and
#debugging my program.  Reference URLs:

import numpy as np
import matplotlib.pyplot as plt

def main():
    #sets up the inital parameters
    N = 1000 #initial population
    t_max = 100 #length of time
    dt = 0.1 #change in time
    t = np.linspace(0, t_max, int(t_max/dt) + 1) #sets up graph
    init_values = 1 - 1/N, 1/N, 0
    beta = 2.0 #contact rate in the population
    gamma = 1.0 #inverse of the mean infectious period
    results = sir_model(N, t, dt, init_values) #runs the model

#these are the differential equations that calculate the SIR model
def sir_model(N, t, dt, init_values):
    S_0, I_0, R_0 = init_values
    S, I, R = [], [], []
    dt = t[1] - t[0]
    for i in t[1]:
        next_S = int(S[-1] - (beta*S[-1]*I[-1])*dt)
        next_I = int(I[-1] + (beta*S[-1]*I[-1]/N-gamma* I[-1]*dt))
        next_R = int( R[-1] + (gamma*I[-1]*dt))
        S.append(next_S)
        I.append(next_I)
        R.append(next_R)
    return np.stack([S, I, R]).T



#call the main function
main()
