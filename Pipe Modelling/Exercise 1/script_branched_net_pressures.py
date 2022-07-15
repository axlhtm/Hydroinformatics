#########################################################################
###################### BRANCHED PIPE CALCULATION ########################
################## Unknown variable: pipe pressures #####################
#########################################################################

import numpy as np
import matplotlib.pyplot as plt

######################### Functions #####################################

# Function to plot networks
def plot_network():
    plt.plot(Nodes[:,1],Nodes[:,2],"ro")
    for i in range(0,num_pipes):
        plt.plot([Nodes[int(Pipes[i,0]-1),1],Nodes[int(Pipes[i,1]-1),1]],
                 [Nodes[int(Pipes[i,0]-1),2],Nodes[int(Pipes[i,1]-1),2]],'k-')
    plt.show()

######################### Input data #####################################

# Nodes input
num_nodes = 6                       # Total number of nodes
Nodes = np.zeros([num_nodes, 7])    # Nodes array with IDs, X, Y, Demand (l/s), Head (msl), Pressure (mwc)
Nodes[:] = np.NaN
Nodes[0,0:5] = 1,25,200,50,0
Nodes[1,0:5] = 2,60,160,12,10.4
Nodes[2,0:5] = 3,100,170,22,22.1
Nodes[3,0:5] = 4,30,80,17,10.2
Nodes[4,0:5] = 5,80,100,25,18.5
Nodes[5,0:5] = 6,130,70,20,14.4


# Pipes input
num_pipes = 5                       # Total number of pipes
Pipes = np.zeros([num_pipes, 11])   # Pipes array with Nup, Ndw, Length (m), Diameter (mm), k(mm), Q (l/s), v (m/s), Re, mu, hf (mwc)
Pipes[:] = np.NaN
Pipes[0,0:5] = 1,2,530,250,0.1
Pipes[1,0:5] = 2,3,410,150,0.1
Pipes[2,0:5] = 2,5,630,200,0.1
Pipes[3,0:5] = 5,4,540,100,0.1
Pipes[4,0:5] = 5,6,580,150,0.1


# Reservoirs
Reservoirs = 1,50       # Reservoirs array with location (node ID) and water level (msl)

# Plot network
plot_network()

# Other input parameters
T = 10      # Water Temperature (celcius)
g = 9.81    # Gravity accelleration (m/s2)
nu = 497*10**(-6)/(T+42.5)**1.5     # Kinematic Viscosity of water (m2/s)

######################### Units to IS #####################################
for i in range(0,num_nodes):
    Nodes[i,4] = Nodes[i,4]/1000
    
for i in range(0,num_pipes):
    Pipes[i,3] = Pipes[i,3]/1000
    Pipes[i,4] = Pipes[i,4]/1000

######################### Mass Balance #####################################

# Topology array
Topology = np.zeros([num_nodes,num_nodes])
Topology[:] = np.NaN
for i in range(0,num_pipes):
    Topology[int(Pipes[i,0]-1),int(Pipes[i,1]-1)] = -9999   # Topology matrix (Nups x Ndws)
for i in range(0,num_nodes):
    Topology[i,i] = 0

# Assign demands in diagonal
MB = Topology + np.identity(num_nodes) * Nodes[:,4]

# Balance
for j in range(1,100):
    for i in range(1,num_nodes):
        balance = np.concatenate((MB[i,:],MB[:,i]))
        balance= balance[~np.isnan(balance)]
        if sum(balance) < -999 and sum(balance) >= -9999:
            a = np.argwhere(MB[i,:] == -9999)
            b = np.argwhere(MB[:,i] == -9999)
            MB[i,a] = sum(balance) - MB[i,i] +9999
            MB[b,i] = sum(balance) - MB[i,i] +9999
    if int(-9999 in MB)==0: break

######################### Computation #####################################

# Pipes computation
for i in range(0,num_pipes):
    Pipes[i,5] = MB[int(Pipes[i,0]-1),int(Pipes[i,1]-1)] # Assign flow rates in pipe
    Pipes[i,6] = Pipes[i,5]/(np.pi*(Pipes[i,3]/2)**2)
    Pipes[i,7] = Pipes[i,6]*Pipes[i,3]/nu   
    if Pipes[i,7] <= 2000: Pipes[i,8] = 64/Pipes[i,7] 
    if Pipes[i,7] > 2000: Pipes[i,8] = (1/(-2*np.log10(5.1286/Pipes[i,7]**0.89 + Pipes[i,4]/(3.71*Pipes[i,3]))))**2
    Pipes[i,9] = 8*Pipes[i,8]/(np.pi**2*9.81*Pipes[i,3]**5) *Pipes[i,5]**2
    Pipes[i,10] = Pipes[i,2]*Pipes[i,9]

# Nodes computation
Heads =np.zeros([num_nodes,num_nodes])
Heads[:] = np.NaN
Heads[int(Reservoirs[0])-1,int(Reservoirs[0])-1] = Reservoirs[1]

for i in range(0,num_pipes):
    Heads[int(Pipes[i,0]-1),int(Pipes[i,1]-1)] = Pipes[i,10]

# Assignation of pressures in Heads array (not sure if only one iteration is enough)
for i in range(0,num_nodes):
    for j in range(0,num_nodes):
        Heads[int(Reservoirs[0])-1,int(Reservoirs[0])-1] = Reservoirs[1]
        if i!=j:
            if np.isnan(Heads[i,j]) == False:
                if np.isnan(Heads[i,i]) == False:
                    Heads[j,j] = Heads[i,i] - Heads[i,j]

for i in range(0,num_nodes):
    Nodes[i,5] = Heads[i,i]   
    Nodes[i,6] = Nodes[i,5] - Nodes[i,3]


print(Nodes[:,6])

