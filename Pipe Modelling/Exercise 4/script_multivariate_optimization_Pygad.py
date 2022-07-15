####################################################################################
#####################   OPTIMIZATION EXERCISE (PYGAD) #############################
####################################################################################

# (1) A simple EPANET network is first imported and plotted.
# (2) Then EPANET model is launched and pressure results are printed and plotted.
# (3) Optimization inputs are assigned, i.e. input parameters (demand node) and desired output (velocity at the pipe)
# (4) The objective function is defined (fitness_func)
# (5) Setup of the optimization algorithm is defined (generations, parents, cross-over, mutation, etc.)
# (6) GA instance is created and run.
# (7) GA results are plotted
# (8) The solution is confirmed launching Epanet with the new pipe diameter and printing new pressures.


# Import Python packages:
import wntr
import pygad
#import numpy


# (1) Import and plot an EPANET model
# Import model:
inp_file = 'D:/04_IHE/01_Education/01_Courses/2022_M11_AWTD/03_Python/03_Workshops/01_workshop_WDM/network.inp'
wn = wntr.network.WaterNetworkModel(inp_file)  # The network is loaded in Python under the name "wn"
# Plot network:
wntr.graphics.plot_network(wn, title=wn.name)


# (2) Launch network and plot results
# Launch simulation:
sim = wntr.sim.EpanetSimulator(wn)
results = sim.run_sim() # simulation results are stored in a variable named "results"

# Print pressure results
pressures = results.node['pressure'].loc[0,:] 
print(pressures)
velocities = results.link['velocity'].loc[0,:] 
print(velocities)

# Plot results on the network:
pressure_at_0hr = results.node['pressure'].loc[0, :] # pressures at time-step 0 are stored
wntr.graphics.plot_network(wn, node_attribute=pressure_at_0hr, node_size=150, title='Pressure at 0 hours')


# (3) Optimization inputs:
function_inputs = [1,1] # input parameter (node demand m3/s) --> this could be an array of values
desired_output = 20 # desired output (min pressure in the system)

# (4) Objective function definition:
def fitness_func(solution, solution_idx): # Calculating the fitness value of each solution in the current population. 
    pipe_P1 = wn.get_link('P1') # Selection of pipe
    pipe_P1.diameter = function_inputs[0]*solution[0]  # Assign new diameter to pipe
    pipe_P7 = wn.get_link('P7') # Selection of pipe
    pipe_P7.diameter = function_inputs[1]*solution[1]  # Assign new diameter to pipe
    results = sim.run_sim() # Epanet is launched with the new input
    pressures = results.node['pressure'].loc[0,:]  # Pressure results are stored
    output = min(pressures[0:7]) # Minimum pressure in the system is selected and stored
    fitness = 1.0 / (abs(output - desired_output) + 0.000001)  # Fitness is computed. The value 0.000001 is used to avoid the Inf values
    return fitness
fitness_function = fitness_func

# (5) Optimization setup is defined
num_generations = 10 # Number of generations.
num_parents_mating = 2 # Number of solutions to be selected as parents in the mating pool.
sol_per_pop = 20 # Number of solutions in the population.
num_genes = 2 #len(function_inputs) --> this can be an array
init_range_low = 0.1 
init_range_high = 1
gene_space = [{'low': 0.01 ,'high': 1},{'low': 0.01 ,'high': 1}] # Solution space to be searched
last_fitness = 0

# (6) GA instance is created and run:

def callback_generation(ga_instance): # This function prints algorithm progress
    global last_fitness
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))
    print("Change     = {change}".format(change=ga_instance.best_solution()[1] - last_fitness))
    last_fitness = ga_instance.best_solution()[1]

# Creating an instance of the GA class inside the ga module. Some parameters are initialized within the constructor.
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       gene_space = gene_space,
                       callback_generation=callback_generation)

# Running the GA to optimize the parameters of the function.
ga_instance.run()

# (7) GA results are plotted:
# After the generations complete, some plots are showed that summarize the how the outputs/fitenss values evolve over generations.
ga_instance.plot_result()
# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# (8) The solution is confirmed launching Epanet and new results are printed:
pipe_P1 = wn.get_link('P1') 
pipe_P1.diameter = function_inputs[0]*solution[0]
pipe_P7 = wn.get_link('P7') 
pipe_P7.diameter = function_inputs[1]*solution[1]
results = sim.run_sim()
pressures = results.node['pressure'].loc[0,:] 
print(pressures)
print('solution diameter P1', round(1000*pipe_P1.diameter,3),'mm')
print('solution diameter P7', round(1000*pipe_P7.diameter,3),'mm')


