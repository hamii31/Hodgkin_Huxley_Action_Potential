import numpy as np

from steady_state import m_inf, h_inf, n_inf
from .forward_euler import forward_euler
from plot import plot_chain

# Oscillation Experiment for multiple neurons
T_end = 100
dt = 0.01
V_rest = -65
N = 10
initial_state = []

for _ in range(N):
    initial_state.append((V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest)))

for uA in np.arange(0.0, 30.0, 1.0):
    neuro_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, N=N, I_ext_function=lambda t, amp=uA: amp)

    plot_chain(
        title=f'Oscillation Experiment at {uA} μA',
        neuron_histories=neuro_history
    )
