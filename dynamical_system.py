from ionic_currents import sodium_channel, potassium_channel, leaky_channel
from gating_ODEs import m_gating, h_gating, n_gating

C_m = 1.0

def I_ext(t):
    """
    The exteriorly-injected current by the experimenter.
    """
    if t > 4 and t < 7:
        return 10
    else:
        return 0

def dynamical_system(t, state, I_ext_function):
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
    dV_dt = (I_ext_function(t) - I_Na - I_K - I_L) / C_m
    
    # Calculate the gating ODEs
    dm_dt = m_gating(V=state[0], m=state[1])
    dh_dt = h_gating(V=state[0], h=state[2])
    dn_dt = n_gating(V=state[0], n=state[3])

    return dV_dt, dm_dt, dh_dt, dn_dt
