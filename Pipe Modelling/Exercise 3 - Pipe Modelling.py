
#####################  STEADY STATE ANALYSIS (WNTR)  #############################
# (1) A simple EPANET network is first imported and plotted.
# (2) Then EPANET model is launched and pressure results are plotted.
# (3) Fianlly a parameter of a certain node (demand in N8) is modified, Epanet is relaunched and new results plotted.

# Import Python packages:
import wntr

# (1) Import and plot an EPANET model
# Import model:
inp_file = 'G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Pipe Modelling/networks/Net.inp'
wn = wntr.network.WaterNetworkModel(inp_file)  # The network is loaded in Python under the name "wn"
# Plot network:
wntr.graphics.plot_network(wn, title=wn.name)

# (2) Launch network and plot results
# Launch simulation:
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim() # simulation results are stored in a variable named "results"
# Plot results on the network:
pressure_at_0hr = results.node['pressure'].loc[0, :] # pressures at time-step 0 are stored
wntr.graphics.plot_network(wn, node_attribute=pressure_at_0hr, node_size=150, title='Pressure at 0 hours')


# (3) Change a parameter value: 
junction = wn.get_node('N8') # Variable "junction" is associated to N8
junction.demand_timeseries_list[0].base_value = 0 # Demand is changed in N8
results = sim.run_sim()  # The new Epanet model is launched
pressure_at_0hr = results.node['pressure'].loc[0, :]  # New pressures are stored
wntr.graphics.plot_network(wn, node_attribute=pressure_at_0hr, node_size=50, title='Pressure at 0 hours')


