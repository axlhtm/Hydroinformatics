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

# EXAMINING THE HEADING RESULT AS IN PANDAS DATA FRAME 
link_keys = results.link.keys()
print(link_keys)

# MAXIMUM FLOW IN PIPE 10 BY CALLING THE HEADING 
flow_p10 = results.link["flowrate"].loc[:,'10']
flow_p10.max()