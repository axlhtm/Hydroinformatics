#########################################################################
####################### SINGLE PIPE CALCULATION #########################
################### Unknown variable: discharge #####################
#########################################################################

import numpy as np

# Input parameters:
L_in = 1500     # Pipe length (m)
D_in = 500     # Pipe diameter (mm)
k_in = 0.1     # Pipe roughness (mm)
S_in = 10/L_in    # HGL slope (-)
T_in = 10      # Water temperature (celcius)
H_in = 90      # Known Pressure value at the pipe section (mwc)

# International (metric) System Units:
L = L_in        # Pipe length (m)
D = D_in/1000   # Pipe diameter (m)
k = k_in/1000   # Pipe roughness (m)
S = S_in        # HGL slope (-)
T = T_in        # Water temperature (celcius)
H_up = H_in     # Known Pressure value at the downstream pipe section (mwc)

# Computation pipe discharge:
v_in = 1            # initial guessed flow velocity (m/s)
error = 0.0001      # error tolerance (m/s)
iterations = 1000   # number of maximum iterations to reach a solution
for i in range(0, iterations):
    nu = 497*10**(-6)/(T+42.5)**1.5     # Kinematic Viscosity of water (m2/s)
    Re = v_in*D/nu                      # Reynolds number (-)
    if Re <= 2000: mu = 64/Re                                                 # friction factor for laminar flow
    if Re > 2000: mu = (1/(-2*np.log10(5.1286/Re**0.89 + k/(3.71*D))))**2     # friction factor for transitional or turbulent flow (Barr, 1975)
    v_c = np.sqrt(2*9.81*D*S/mu)
    if abs(v_in-v_c) < error: 
        print("Reynolds number:",round(Re,2))
        print("Friction factor:",round(mu,4))
        v = v_c
        Q = v*D**2*np.pi/4          # Pipe discharge (m3/s)
        print("Pipe discharge:",round(Q,4))
        break
    else:
        v_in = v_c
    if i == iterations-1: print("A solution could not be reached")