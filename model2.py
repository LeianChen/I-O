# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:45:18 2018

@author: HP
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

"""
a = agentframework.Agent()
print (a.y, a.x)
a.move()
print(a.y, a.x)
"""






############################################
######### Import environment ###########
###########################################  
        
environment = []
f = open('in.txt') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    
    rowlist = []		
    for value in row:				
        rowlist.append(value)
        
    environment.append(rowlist)

f.close()
"""
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
"""

############################################

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    
############################################
######### Call eat for each agent ###########
########################################### 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        #agents[i].eat()

matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(299, 0)
matplotlib.pyplot.imshow(environment)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()








"""
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
"""