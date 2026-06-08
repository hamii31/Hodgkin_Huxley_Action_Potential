import numpy as np

from steady_state import m_inf, h_inf, n_inf
from forward_euler import forward_euler
from plot import plot

# Subthreshold Experiment
threshold = 0
T_end = 50
dt = 0.01
V_rest = -65
initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))

for uA in np.arange(6.95, 6.99, 0.001):
    V_history, _, _, _, _ = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t, amp=uA: amp if 5 < t < 6 else 0)
    if max(V_history) < 0:
        threshold = uA
    if max(V_history) >= 0:
        break

V_history, t_history, m_history, h_history, n_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t: threshold if 5 < t < 6 else 0)
plot(title="Threshold Experiment", subtitle=f"The last subthreshold was observed at {threshold} µA.", V_history=V_history, t_history=t_history, m_history=m_history, h_history=h_history, n_history=n_history)
