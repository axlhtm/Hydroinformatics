
#####################  TRANSIENT ANALYSIS (TSNET)  #############################
# (1) First an Epanet model is loaded in Python
# (2) Transient modelling input parameters are set to complent the basic Epanet model.
# (3) The model is launched, first steady-state (initial conditions) and then the transient state, i.e. MoC solver
# (4) Results are ploted (pressure next to the valve), and the plot is saved.

# Import Python packages
import tsnet

# (1) Open an example network and create a transient model:
tm = tsnet.network.TransientModel('G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Pipe Modelling/Exercise 4/network_transient.inp')

# (2) Define additional input and simulation parameters:
# Set wavespeed
tm.set_wavespeed(500 * 1) # m/s (this could be computed and assigned pipe by pipe too)
# Set time options
tf = 100   # simulation period [s]
tm.set_time(tf)
# Set valve closure
ts = 5 # valve closure start time [s]
tc = 2 # valve closure period [s]
se = 0 # end open percentage [s]
m = 2 # closure constant [dimensionless]
tm.valve_closure('VALVE',[tc,ts,se,m]) # Valve parameters are loaded

# (3) Launch model:
# Initialize steady state simulation
t0=0
tm = tsnet.simulation.Initializer(tm,t0)
# Transient simulation
tm = tsnet.simulation.MOCSimulator(tm)


# (4) report results:
# report results
node = 'N7'
tm.plot_node_head(node)  
head = tm.get_node(node).head  
print('The maximum pressure head in the system is:',round(max(head),2), 'm.w.c.')
    
