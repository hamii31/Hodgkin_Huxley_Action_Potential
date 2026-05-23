import numpy as np

from steady_state import m_inf, h_inf, n_inf
from .forward_euler import forward_euler
from plot import plot_chain
from .synaptic_model import N_syn

# Threshold Experiment
T_end = 50
dt = 0.01
V_rest = -65
uA_start = 6.5 # since the single neuron threshold experiment concluded that a 1ms 7 microamp pulse is enough for an AP
N = 5
initial_state = []

for _ in range(N):
    initial_state.append((V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest)))

def detect_spike_times(V_history, t_history):
    times = []
    for k in range(1, len(V_history)):
        if V_history[k-1] < 0 and V_history[k] >= 0:
            times.append(t_history[k])
    return times

for uA in np.arange(uA_start, 10.0, 0.1):
    neuro_history = forward_euler(T_end=T_end, dt=dt, initial_state=initial_state, N=N, I_ext_function=lambda t, amp=uA: amp if 5 < t < 6 else 0)

    plot_chain(
        title=f'Threshold Experiment at {uA:.2f} μA and {N_syn} presynaptic connections',
        neuron_histories=neuro_history
    )

    if len(detect_spike_times(neuro_history[-1][0], neuro_history[-1][1])) > 0: # check if last neuron spiked
        break
