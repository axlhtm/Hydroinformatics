# EXERCISE 1 - PIPE MODELLING 

# INPUT THE DATA 
D    = 0.02            # Diameter (m) 
visc = 10**-6          # Kinematic viscosity (m2/s)
rho  = 1000            # Water density (kg/m3)
ks   = 1*10**-6        # Roughness for concrete pipe
L    = 15.49           # Pipe length (m)
Hup  = 54.72082        # Head upstream (m)
Q    = 0.003           # Discharge (m3/s)

# DETERMINE REYNOLDS NUMBER CALCULATION 
A    = 3.14 * (D/2)**2 # Cross-section area (m2)
V    = Q / A           # Flow velocity (m/s)
Re   = V * D / visc    # Reynolds number

# DETERMINA THE FLOW REGIME 
if Re <= 2100 : 
    regime = "Laminar Flow"
elif Re >= 4000 : 
    regime = "Turbulent Flow"
elif Re > 2100 and Re < 4000 : 
    regime = "Transitional Flow"

print(regime)