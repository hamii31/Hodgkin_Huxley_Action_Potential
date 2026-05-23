from steady_state import m_inf, h_inf, n_inf
from forward_euler import forward_euler
from plot import plot

# Refractory Experiment
T_end = 50
dt = 0.01
V_rest = -65
initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))

for gap in range(1,20):
    V_history, t_history, m_history, h_history, n_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, I_ext_function=lambda t, g=gap: 10 if (5 < t < 6) or (5 + g < t < 6 + g) else 0)
    if max(V_history) >= 0:
        plot(title=f"Refractory Experiment at {10} µA", subtitle=f"At +{gap}ms gap", V_history=V_history, t_history=t_history, m_history=m_history, h_history=h_history, n_history=n_history)
