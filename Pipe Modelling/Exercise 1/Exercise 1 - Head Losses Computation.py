# =============================================================================
# EXERCISE 1 : Head Losses Computation
# =============================================================================

# IMPORT THE LIBRARY
import numpy as np

# INPUT THE PARAMETER
D = 0.5                                                                        # Pipe diameter (m)
L = 1500                                                                       # Pipe length (m)
K = 0.1 / 1000                                                                 # Pipe roughness (m)
Q = 800                                                                        # Outflow discharge (l/s)
T = 10                                                                         # Water temperature (celcius)
H = 90                                                                        # Known pressure value at the pipe section

# CALCULATE THE FLOW REGIME (Re)
v = 4 * Q/(D**2*np.pi)                                                         # Pipe flow velocity (m/s)


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


