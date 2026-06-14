import numpy as np

from steady_state_values import m_inf, h_inf, n_inf
from plot import plot_network
from .forward_euler import forward_euler
from chain.synaptic_model import N_syn
from chain.helpers import detect_spike_times

# Oscillation Experiment for a feedforward neural network with AMPA-like synaptic connections
T_end = 100
dt = 0.01
V_rest = -65
layers_N = 3
N = 8
N_total = N * layers_N

# Build layers
layers = [list(range(l * N, (l + 1) * N)) for l in range(layers_N)]

# All-to-all connectivity between adjacent layers
connections = []
for l in range(layers_N - 1):
    for i in layers[l]:
        for j in layers[l + 1]:
            connections.append((i, j))

initial_state = [(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest)) for _ in range(N_total)]

for uA in np.arange(0.0, 30.0, 1.0):
    # Only layer 0 receives external drive
    I_ext_functions = [
        (lambda t, amp=uA: amp) if i in layers[0] else (lambda t: 0.0)
        for i in range(N_total)
    ]
    
    neuro_history = forward_euler(
        T_end=T_end, dt=dt,
        initial_state=initial_state, N=N_total,
        I_ext_function=I_ext_functions,
        connections=connections
    )
    
    plot_network(
        title=f'Feedforward network at {uA} μA, layers={layers_N}, N={N}, N_syn={N_syn}, N_syn_per_neuron={N_syn * N}',
        layers=layers,
        neuron_histories=neuro_history
    )
    
    # Check if last-layer neurons are oscillating
    last_layer_counts = [
        len(detect_spike_times(neuro_history[i][0], neuro_history[i][1]))
        for i in layers[-1]
    ]
    if all(c >= 5 for c in last_layer_counts):
        break
