# CONSTANTS
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

# We convert pS to nanosiemens
g_syn = N * y * 0.001

"""
Convergence - how many synapses contribute

G_total = N_syn * g_syn

where N_syn is the number of presynaptic neurons feeding the postsynaptic cell.
For a 1-to-1 communication between neurons, N_syn = 1. For a realistic cortical communication,
N_syn = 1000-10000. For the multi_osc to run properly the synaptic connections must be at least
100.

Convert G_total from nS to milisiemens for the HH equations.
"""

N_syn = 100
G_total = N_syn * g_syn
G_total = G_total * 1e-6 # 1 nS = 1 000 000 mS

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
import numpy as np
r_cell = 0.0025
A_membrane = 4 * np.pi * r_cell**2

g_syn_density = G_total / A_membrane

"""
Note:
Bump up the synaptic connections (N_syn), because N_syn = 1 is too low to cause a postsynaptic spike
========================================================================================================
"""

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
        #s += 1 # bump spike utilizing summation as a realistic mechanism
    return s
