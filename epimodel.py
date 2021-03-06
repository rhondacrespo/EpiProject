#! /usr/bin/env python3

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
#code. We received help in designing and
#debugging my program from my friend Mark. References:
#Hubbs, Christian. “Social Distancing to Slow the Coronavirus.”
#Medium. Available at
#https://towardsdatascience.com/social-distancing-to-slow-the-coronavirus-768292f04296
#"The SIR Model," Availabe at
#https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/
#Yeghikyan, George. “Modelling the Coronavirus Epidemic with Python:
#Are Cities Prepared for an Epidemic?” Medium. Available at
#https://towardsdatascience.com/modelling-the-coronavirus-epidemic-spreading-in-a-city-with-python-babd14d82fa2
#Simple Line Plots. Available at
#https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html
#"Pass defualt variables to matplotlib." Available at
#https://stackoverflow.com/questions/41755550/pass-default-variables-to-matplotlib

import numpy as np
import matplotlib.pyplot as plt

def main():
    #sets up the inital parameters
    N = 1000 #initial population
    t_max = 100 #length of time
    dt = 0.1 #change in time
    t = np.linspace(0, t_max, int(t_max/dt) + 1) #sets up graph
    init_values = N-1, 1, 0 #sets up initial values for S, I, R
    beta = 2.0 #contact rate in the population
    gamma = 1.0 #inverse of the mean infectious period
    results = sir_model(N, t, dt, beta, gamma, init_values) #runs the model
    
    
#these are the differential equations that calculate the SIR model
def sir_model(N, t, dt, beta, gamma, init_values):
    S_0, I_1, R_0 = init_values #initial values for SIR
    S, I, R = [S_0], [I_1], [R_0] #empty lists for SIR
    dt = t[1] - t[0] #change in time
    for i in t: #these are the actual calculations 
        next_S = int(S[-1] - (beta*S[-1]*I[-1])/N*dt)
        next_I = int(I[-1] + (beta*S[-1]*I[-1]/N-gamma* I[-1]*dt))
        next_R = int(R[-1] + (gamma*I[-1]*dt))
        S.append(next_S) #these appends the calculations to the bottom of each list
        I.append(next_I)
        R.append(next_R)
    #print('this actually worked!') #I just needed to see that it worked!
    print(S)
    print(I)
    print(R)
    plot_fun(t, S[:-1], I[:-1], R[:-1])
    return np.stack([S, I, R]).T #returns the values


#plot the data as three separate lines for S, I, and R
def plot_fun(t, S, I, R):
    fig = plt.figure() #these two lines sets up the plot and axes
    ax = plt.axes()
    ax.plot(t, S, color='blue', label='Susceptible') #plots each group as a separate line on the y-axis
    ax.plot(t, I, color='red', label='Infectious')
    ax.plot(t, R, color='green', label='Removed')
    ax.set_xlabel('Time(Days)') #these label the axes
    ax.set_ylabel('Number of Individuals')
    plt.show()
    #fig, ax = plt.subplots(1)
    fig.savefig('epidemic.png') #saves to an output file
    return (fig)


#call the main function
main()

