from matplotlib import pyplot as plt
import wntr

# Create a water network model
inp_file = 'G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Urban Modelling/Leak Modelling/data/Netx.inp'
wn = wntr.network.WaterNetworkModel(inp_file)

# Simulate hydraulics
wn.options.hydraulic.demand_model = 'PDD'
sim = wntr.sim.WNTRSimulator(wn)

results = sim.run_sim()

fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot results on the network
pressure_at_5hr = results.node['pressure'].loc[5*3600, :]
wntr.graphics.plot_network(wn, ax=ax1, node_attribute=pressure_at_5hr, node_size=500, 
                        title='Pressure at 5 hours', node_labels=True, node_range=[75,150])



wn = wntr.morph.split_pipe(wn, '111', '111_B', '111_leak_node')
leak_node = wn.get_node('111_leak_node')
leak_node.add_leak(wn, area=.1, start_time=0*3600, end_time=12*3600)
sim = wntr.sim.WNTRSimulator(wn)
wn.options.hydraulic.demand_model = 'PDD'
results = sim.run_sim()
# Plot results on the network
pressure_at_5hr = results.node['pressure'].loc[5*3600, :]
wntr.graphics.plot_network(wn, ax=ax2, node_attribute=pressure_at_5hr, node_size=500, 
                        title='Pressure at 5 hours', node_labels=True, node_range=[75,150])

plt.show()