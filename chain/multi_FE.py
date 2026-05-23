from dynamical_system import dynamical_system
from .synaptic_model import update_synapse, spike_detected, g_syn_density

def update_state(current_state, dt, derivatives):
    V_new = current_state[0] + dt * derivatives[0]
    m_new = current_state[1] + dt * derivatives[1]
    h_new = current_state[2] + dt * derivatives[2]
    n_new = current_state[3] + dt * derivatives[3]

    return (V_new, m_new, h_new, n_new)

def forward_euler(T_end, dt, initial_state, N, I_ext_function):
    """
    Applies forward euler to multiple neurons 
    """
    # CONSTANTS
    E_syn = 0 # E_syn marks the synaptic reversal potential, which for AMPA is 0
    s = [0.0 for _ in range(N - 1)]

    states = [initial_state[i] for i in range(N)]
    V_histories = [[] for _ in range(N)]
    m_histories = [[] for _ in range(N)]
    h_histories = [[] for _ in range(N)]
    n_histories = [[] for _ in range(N)]
    t_history = []

    derivatives = ()

    n_steps = int(T_end / dt)
    for i in range(n_steps):
        t = i * dt
        # Save history
        t_history.append(t)

        for j in range(N):
            # Compute I_syn for postsynaptic neuron before derivatives
            V_post = states[j][0] 
            I_syn = g_syn_density * s[j-1] * (V_post - E_syn)

            if j == 0:
                # first neuron gets injected external drive
                derivatives = dynamical_system(t=t,state=states[j], I_ext_function=I_ext_function)
            else:
                # the rest try to fire from the spikes of the first neuron (no external drive)
                derivatives = dynamical_system(t=t,state=states[j], I_ext_function=lambda t: 0.0, I_syn=I_syn)

            states[j] = update_state(current_state=states[j], dt=dt, derivatives=derivatives)

            V_histories[j].append(states[j][0])
            m_histories[j].append(states[j][1])
            h_histories[j].append(states[j][2])
            n_histories[j].append(states[j][3])

            # Detect a spike underway
            if j < N - 1: # since we are getting the last 2 entries from V_history
                spike = spike_detected(V_history=V_histories[j])
                s[j] = update_synapse(s[j], dt, spike)
        
    neuron_histories = [
        (V_histories[j], t_history, m_histories[j], h_histories[j], n_histories[j])
        for j in range(N)
    ]        

    return neuron_histories
