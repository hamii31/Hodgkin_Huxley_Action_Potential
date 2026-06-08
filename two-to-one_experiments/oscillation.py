import numpy as np

from steady_state_values import m_inf, h_inf, n_inf
from plot import plot_chain
from .forward_euler import forward_euler
from chain.synaptic_model import N_syn
from chain.helpers import detect_spike_times

# Oscillation Experiment for multiple neurons
T_end = 100
dt = 0.01
V_rest = -65
N = 3
initial_state = []

# Y-shape: neurons 0 and 1 both feed into neuron 2
connections = [(0, 2), (1, 2)]

for _ in range(N):
    initial_state.append((V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest)))

for uA in np.arange(0.0, 30.0, 1.0):
    I_ext_functions = [
        lambda t, amp=uA: amp,
        lambda t, amp=uA: amp,
        lambda t: 0.0,
    ]

    neuro_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, N=N, I_ext_function=I_ext_functions, connections=connections)

    plot_chain(
        title=f'Oscillation Experiment at {uA} μA and {N_syn} presynaptic connections',
        neuron_histories=neuro_history
    )

    # check if last neuron spiked more than 5 times (oscillation)
    if len(detect_spike_times(neuro_history[-1][0], neuro_history[-1][1])) > 5: # change to 2 for N_syn = 10
        break
