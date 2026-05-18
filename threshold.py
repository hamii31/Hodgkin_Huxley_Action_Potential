import numpy as np

from steady_state import m_inf, h_inf, n_inf
from forward_euler import forward_euler
from plot import action_potential_plot

# Threshold Experiment
threshold = 0
T_end = 50
dt = 0.01
V_rest = -65
initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))

# Iterate through a range of microamps ranging from 0-10 to find the threshold of a 1ms stimulation
for uA in np.arange(0.0, 10.0, 0.01):
    V_history, t_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t, amp=uA: amp if 5 < t < 6 else 0)
    if max(V_history) >= 0:
        print(f"V crossed 0 mV at {uA} µA")
        threshold = uA
        break
    
# Plot
action_potential_plot(title="Threshold Experiment", subtitle=f"The Action Potential was initialized at {threshold} µA.", V_history=V_history, t_history=t_history)
