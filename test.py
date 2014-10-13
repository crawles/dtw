import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
#%matplotlib inline

a = [random.randrange(0,3) for i in range(10)]
b = [random.randrange(0,2) for i in range(10)]

x= np.array(a+[1, 1, 2, 3, 2, 0]+a)
y=np.array(b[0:3]+[0, 1, 1, 2, 3, 2, 1])


plt.plot(x,'r', label='x')
plt.plot(y, 'g', label='y')
plt.legend()


plt.close()

distances = np.zeros((len(y), len(x)))

for i in range(len(y)):
    for j in range(len(x)):
        distances[i,j] = (x[j]-y[i])**2 

def distance_cost_plot(distances):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds') 
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()

distance_cost_plot(distances)
plt.close()
    

accumulated_cost = np.zeros((len(y), len(x)))

accumulated_cost[0,0] = distances[0,0]

distance_cost_plot(accumulated_cost)

for i in range(1, len(x)):
    accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1] 

distance_cost_plot(accumulated_cost)

for i in range(1, len(y)):
    accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]    

distance_cost_plot(accumulated_cost)

for i in range(1, len(y)):
    for j in range(1, len(x)):
        accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]


path = [[len(x)-1, len(y)-1]]
i = len(y)-1
j = len(x)-1

while i>0 and j>0:
    print i,j
    if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
        i = i - 1
    elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
        j = j-1
    else:
        i = i - 1
        j= j- 1
    path.append([j, i])
path.append([0,0])

path_x = [point[0] for point in path]
path_y = [point[1] for point in path]

distance_cost_plot(accumulated_cost)
plt.plot(path_x, path_y);

raw_input()

plt.close()

def path_cost(x, y, accumulated_cost, distances):
    path = [[len(x)-1, len(y)-1]]
    cost = 0
    i = len(y)-1
    j = len(x)-1
    while i>0 and j>0:
        if i==0:
            j = j - 1
        elif j==0:
            i = i - 1
        else:
            if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                i = i - 1
            elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                j = j-1
            else:
                i = i - 1
                j= j- 1
        path.append([j, i])
    path.append([0,0])
    for [y, x] in path:
        cost = cost +distances[x, y]
    return path, cost  

path, cost = path_cost(x, y, accumulated_cost, distances)
print path
print cost


plt.plot(x, 'bo-' ,label='x')
plt.plot(y, 'g^-', label = 'y')
plt.legend();

map_x = path[i][0]
map_y = path[i][1]

paths = path_cost(x, y, accumulated_cost, distances)[0]
for [map_x, map_y] in paths:
    print map_x, x[map_x], ":", map_y, y[map_y]
    
    plt.plot([map_x, map_y], [x[map_x], y[map_y]], 'r')
