
#####################  STEADY STATE ANALYSIS (WNTR)  #############################
# (1) A simple EPANET network is first imported and plotted.
# (2) Then EPANET model is launched and pressure results are plotted.
# (3) Fianlly a parameter of a certain node (demand in N8) is modified, Epanet is relaunched and new results plotted.

# Import Python packages:
import wntr

# (1) Import and plot an EPANET model
# Import model:
inp_file = 'G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Pipe Modelling/Exercise 4/network_steady.inp'
wn = wntr.network.WaterNetworkModel(inp_file)  # The network is loaded in Python under the name "wn"
# Plot network:
wntr.graphics.plot_network(wn, title=wn.name)


# (2) Launch network and plot results
# Launch simulation:
wn.options.hydraulic.demand_model = 'PDD'                                       # Change to Presure Demand Driven
#sim = wntr.sim.EpanetSimulator(wn)
sim = wntr.sim.WNTRSimulator(wn)
results = sim.run_sim() # simulation results are stored in a variable named "results"

# Print pressure results
pressures = results.node['pressure'].loc[0,:] 
print(pressures)
demands = results.node['demand'].loc[0,:]
print(demands)
velocities = results.link['velocity'].loc[0,:] 
print(velocities)

# Plot results on the network:
pressure_at_0hr = results.node['pressure'].loc[0, :] # pressures at time-step 0 are stored
wntr.graphics.plot_network(wn, node_attribute=pressure_at_0hr, node_size=150, title='Pressure at 0 hours')


# (3) Change a parameter value (diameter in P1): 
wn_new = wntr.network.WaterNetworkModel(inp_file)
pipe_P1 = wn_new.get_link('P1') 
pipe_P7 = wn_new.get_link('P7')

print('diameter for pipe 1 is', pipe_P1.diameter)
print('diameter for pipe 7 is', pipe_P7.diameter)

pipe_P1.diameter = 0.8
pipe_P7.diameter = 0.76

sim = wntr.sim.EpanetSimulator(wn_new)
results = sim.run_sim()  # The new Epanet model is launched

pressure_at_0hr = results.node['pressure'].loc[0, :]  # New pressures are stored
wntr.graphics.plot_network(wn_new, node_attribute=pressure_at_0hr, node_size=50, title='Pressure at 0 hours')

pressures = results.node['pressure'].loc[0,:] 
print(pressures)



