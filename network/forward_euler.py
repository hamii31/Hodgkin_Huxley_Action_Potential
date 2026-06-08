from dynamical_system import dynamical_system
from chain.synaptic_model import update_synapse, spike_detected, g_syn_density

def update_state(current_state, dt, derivatives):
    V_new = current_state[0] + dt * derivatives[0]
    m_new = current_state[1] + dt * derivatives[1]
    h_new = current_state[2] + dt * derivatives[2]
    n_new = current_state[3] + dt * derivatives[3]

    return (V_new, m_new, h_new, n_new)

def forward_euler(T_end, dt, initial_state, N, I_ext_function, connections):
    """
    I_ext_functions: list of length N, one I_ext function per neuron (use lambda t: 0.0 for neurons with no external drive)
    connections: list of (presyn, postsyn) tuples representing the synapses
    """
    # CONSTANTS
    E_syn = 0 # E_syn marks the synaptic reversal potential, which for AMPA is 0

    # One s per connection, indexed by position in the connections list
    s = [0.0 for _ in connections]

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
        t_history.append(t)

        for j in range(N):
            # Pass 1: compute I_syn for each neuron by summing over its incoming synapses
            I_syn_per_neuron = [0.0] * N
            for conn_idx, (_, post) in enumerate(connections):
                V_post = states[post][0]
                I_syn_per_neuron[post] += g_syn_density * s[conn_idx] * (V_post - E_syn)

        # Pass 2: compute derivatives for all neurons and update the states
        new_states = []
        for j in range(N):
            derivatives = dynamical_system(t=t,state=states[j], I_ext_function=I_ext_function[j], I_syn=I_syn_per_neuron[j])
            new_states.append(update_state(current_state=states[j], dt=dt, derivatives=derivatives))

        states = new_states

        # Pass 3: Append histories
        for j in range(N):
            V_histories[j].append(states[j][0])
            m_histories[j].append(states[j][1])
            h_histories[j].append(states[j][2])
            n_histories[j].append(states[j][3])

        # Pass 4: Detect a spike underway and update synapses
        for conn_idx, (pre, post) in enumerate(connections):
            spike = spike_detected(V_history=V_histories[pre])
            s[conn_idx] = update_synapse(s[conn_idx], dt, spike)                
        
    neuron_histories = [
        [V_histories[j], t_history, m_histories[j], h_histories[j], n_histories[j]]
        for j in range(N)
    ]        

    return neuron_histories
