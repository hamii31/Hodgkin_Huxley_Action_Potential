import numpy as np

# CONSTANTS
g_syn = 0
G_total = 0
g_syn_density = 0


# Constant calculations
"""
Single synapse conductance

g_syn = N * y

where N is the number of synaptic connections (10-100 in AMPA receptors) and y is the single-channel
conductance in pS (picosiemens). y values are different for different receptors:
- AMPA receptors (excitatory): typically 1-20 pS
- NMDA receptors (excitatory): typically 5-50 pS
- GABA receptors (inhibitory): typically 5-100 pS
"""

# Middle ground (too low and no transmissions, too high - guaranteed transmissions)
N = 50 
y = 10 

# Convert from pS to milisiemens
g_syn = N * (y * 1e-9)

"""
Convergence - how many synapses contribute

G_total = N_syn * g_syn

where N_syn is the number of presynaptic neurons feeding the postsynaptic cell.
For a 1-to-1 communication between neurons, N_syn = 1. For a realistic cortical communication,
N_syn = 1000-10000.
"""

N_syn = 100 # change synaptic connections count 
G_total = N_syn * g_syn

"""
Density conversion

Since HH equations use density in mS/square centimeter, we need to convert the absolute conductance (G_total)

g_syn_density = G_total / A_membrane

where A_membrane is the membrane area of the postsynaptic cell. 

To get the area, we will use the radius of a large axons, which is about 25 micrometers, which needs to be converted
to centimeters for the HH equations.

The formula for the area will be for a sphere surface area:
4 · π · r^2
"""
r_cell = 0.0025
A_membrane = 4 * np.pi * r_cell**2

g_syn_density = G_total / A_membrane

tau_syn = 5.0

def spike_detected(V_history):
    if len(V_history) < 2:
        return False
    V_now = V_history[-1]
    V_prev = V_history[-2]
    return V_now >= 0 and V_prev < 0
    
def update_synapse(s, dt, spike_detected):
    """
    Updates synaptic gating variable s.
    Decays toward zero with time constant tau_syn.
    Bumps up on presynaptic spike.
    """
    s = s + dt * (-s / tau_syn) # decay
    if spike_detected:
        s = min(s + 1, 1)
    return s
