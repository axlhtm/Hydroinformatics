#########################################################################
####################### SINGLE PIPE CALCULATION #########################
################### Unknown variable: pipe pressure #####################
#########################################################################

import numpy as np

# Input parameters:
L_in = 1500     # Pipe length (m)
D_in = 500     # Pipe diameter (mm)
k_in = 0.1     # Pipe roughness (mm)
Q_in = 800     # Flow rate (l/s)
T_in = 10      # Water temperature (celcius)
H_in = 100      # Known Pressure value at the pipe section (mwc)

# International (metric) System Units:
L = L_in        # Pipe length (m)
D = D_in/1000   # Pipe diameter (m)
k = k_in/1000   # Pipe roughness (m)
Q = Q_in/1000   # Flow rate (m3/s)
T = T_in        # Water temperature (celcius)
H_up = H_in     # Known Pressure value at the downstream pipe section (mwc)

# Flow regime calculation (Re):
v = 4 * Q/(D**2*np.pi)              # Pipe flow velocity (m/s)
nu = 497*10**(-6)/(T+42.5)**1.5     # Kinematic Viscosity of water (m2/s)
Re = v*D/nu                         # Reynolds number (-)
if Re <= 2000: flow_regime = "Laminar"
if Re > 2000 and Re < 4000: flow_regime = "Transitional" 
if Re >= 4000: flow_regime = "Turbulent"
print("Flow regime:",flow_regime)

# Friction losses calculation (Darcy-Weisbach equation):
if flow_regime == "Laminar":
    mu = 64/Re                                                  # friction factor for laminar flow
else:
    mu = (1/(-2*np.log10(5.1286/Re**0.89 + k/(3.71*D))))**2     # friction factor for transitional or turbulent flow (Barr, 1975)
print("Friction factor:",round(mu,4))
h_f = 8*mu*L/(np.pi**2*9.81*D**5) * Q**2    # Friction losses in the pipe
print("Friction losses in the pipe:",np.round(h_f,2),"m")

# HGL and upstream pressure calculation:
S = h_f/L           # Slope hydraulic grade line
H_dw = H_up - h_f  # Pressure at the upstream section
print("Pressure at the downstream section:",np.round(H_dw,2),"mwc")


