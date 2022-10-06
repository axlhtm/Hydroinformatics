# IMPORT PYTHON LIBRARY
import wntr 

# IMPORT EPANET WATER DISTRIBUTION NETWORKS (WDN)
inp_file = 'G:/My Drive/Work Data/PT. Hutomo Bangun Perkasa/Hydroinformatics/Urban Modelling/WNTR/Net1.inp'
wn       = wntr.network.WaterNetworkModel(inp_file)

# SIMULATE HYDRAULIC MODEL OF WDN
sim      = wntr.sim.EpanetSimulator(wn)
results  = sim.run_sim() 

# GRAPH WATER DISTRIBUTION NETWORKS (WDN)
wntr.graphics.plot_network(wn, title = 'Water Distribution Networks') 

# CASE: MINIMUM PRESSURE ALONG THE NETWORK IS 20 FEET. WE NEED TO CHANGE THE DIAMETER OF PIPE 10. 

# CHECK PRESSURE ALONG THE NETWORK
P_Nodes = results.node['pressure']
print(P_Nodes)