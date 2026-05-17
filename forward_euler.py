import matplotlib.pyplot as plt

from dynamical_system import dynamical_system
from steady_state import m_inf, h_inf, n_inf

def forward_euler(T_end, dt, initial_state):
    """
    state(t + dt) = state(t) + dt · derivatives(t, state)

    state(t + dt) - state after one step
    state(t) - current state

    Forward Euler is the simplest version of the ODE solvers, 
    but useful to see a simplistic neuron model in action.

    This function implements a loop that steps from t = 0 to t = T_end with step size dt.
    On each step it calls the dynamical_system. 
    """
    V_history = []
    t_history = []
    current_state = initial_state

    n_steps = int(T_end / dt)
    for i in range(n_steps):
        t = i * dt
        derivatives = dynamical_system(t=t,state=current_state)
        V_new = current_state[0] + dt * derivatives[0]
        m_new = current_state[1] + dt * derivatives[1]
        h_new = current_state[2] + dt * derivatives[2]
        n_new = current_state[3] + dt * derivatives[3]

        current_state = (V_new, m_new, h_new, n_new)

        # Save history
        t_history.append(t)
        V_history.append(V_new)


    plt.plot(t_history, V_history)
    plt.xlabel('time (ms)')
    plt.ylabel('V (mV)')
    plt.ylim(-80, 60)
    plt.show()



# Testing params: T_end = 50 ms, dt = 0.01 ms, initial state = (V_rest, m_∞(V_rest), h_∞(V_rest), n_∞(V_rest)).
# T_end = 50
# dt = 0.01
# V_rest = -65
# initial_state=(V_rest, m_inf(V_rest), h_inf(V_rest), n_inf(V_rest))
# forward_euler(T_end=T_end, dt=dt, initial_state=initial_state)
