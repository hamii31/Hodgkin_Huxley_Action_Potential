import numpy as np

from steady_state_values import m_inf, h_inf, n_inf
from forward_euler import forward_euler
from plot import plot

#Action potential init:
T_end = 50
dt = 0.01
V_rest = -65
initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))
V_history, t_history, m_history, h_history, n_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t: 10 if 4 < t < 7 else 0)

#Plot
plot(title="Action potential initialization", subtitle=None, V_history=V_history, t_history=t_history, m_history=m_history, h_history=h_history, n_history=n_history)
