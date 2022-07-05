# =============================================================================
# EXERCISE 1 - PIPE MODELLING 
# =============================================================================

# IMPORT LIBRARY 
import math 

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

# DETERMINE THE HEAD LOSSES FUNCTION
def losses(Q,D, visc, ks,L) : 
    
    # Reynolds Number Calculation
    A = 3.14 * (D/2)**2   # Cross-section area (m2)
    V = Q / A             # Flow velocity (m/s)
    Re = V * D / visc     # Reynolds number 
    
    # Darcy Friction Computation
    if Re <= 2100 : 
        f = 64 / Re 
    else : 
        f = 0.25 / ((math.log10((ks/D)/3.7) + (5.74 / (Re**0.9)))**2)
    
    # Head Losses Computation
    losses = (f * V**2 ) / (2 * 9.81 * D) * L 
    
    return losses 

print(losses(Q, D, visc, ks, L))
    
    