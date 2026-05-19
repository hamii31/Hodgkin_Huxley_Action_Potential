import numpy as np

from steady_state import m_inf, h_inf, n_inf
from forward_euler import forward_euler
from plot import plot

# Oscillation Experiment
T_end = 100
dt = 0.01
V_rest = -65

initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))

for uA in np.arange(0.0, 30.0, 1.0):
    V_history, t_history, m_history, h_history, n_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t, amp=uA: amp)
    plot(title=f"Oscillation Experiment at {uA} µA", subtitle=None, V_history=V_history, t_history=t_history, m_history=m_history, h_history=h_history, n_history=n_history)
