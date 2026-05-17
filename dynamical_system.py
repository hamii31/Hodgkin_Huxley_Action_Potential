from steady_state import m_inf, h_inf, n_inf
from ionic_currents import sodium_channel, potassium_channel, leaky_channel
from gating_ODEs import m_gradient, h_gradient, n_gradient

# CONSTANTS
C_m = 1.0

def I_ext(t):
    print(t)
    if t > 4 and t < 7:
        return 10
    else:
        return 0

def dynamical_system(t, state):
    """
    dV/dt = (I_ext(t) − I_Na − I_K − I_L) / C_m
    dm/dt = α_m(V)(1 − m) − β_m(V) m
    dh/dt = α_h(V)(1 − h) − β_h(V) h
    dn/dt = α_n(V)(1 − n) − β_n(V) n

    t - simulated time, in milliseconds, since the start of the simulation.

    | C_m | 1.0 μF/cm² | Membrane capacitance per unit area |

    returns the full 4-vector of derivatives (dV/dt, dm/dt, dh/dt, dn/dt)
    """

    # Calculate dV/dt
    I_Na = sodium_channel(V=state[0], m=state[1], h=state[2])
    I_K = potassium_channel(V=state[0], n=state[3])
    I_L = leaky_channel(V=state[0])
    dV_dt = (I_ext(t) - I_Na - I_K - I_L) / C_m
    
    # Calculate the gating ODEs
    dm_dt = m_gradient(V=state[0], m=state[1])
    dh_dt = h_gradient(V=state[0], h=state[2])
    dn_dt = n_gradient(V=state[0], n=state[3])

    return dV_dt, dm_dt, dh_dt, dn_dt


# V = -65
# state = (V, m_inf(V=V), h_inf(V=V), n_inf(V=V))
# derivatives = dynamical_system(t=0.00, state=state)
# print(f"Expected dV/dt: 0, Got: {round(derivatives[0],1)}")
# print(f"Expected dm/dt: 0, Got: {derivatives[1]}")
# print(f"Expected dh/dt: 0, Got: {derivatives[2]}")
# print(f"Expected dn/dt: 0, Got: {derivatives[3]}")
