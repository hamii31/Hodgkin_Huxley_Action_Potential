from steady_state_values import m_inf, h_inf, n_inf

# CONSTANTS
E_Na = 50
g_Na = 120
E_K = -77
g_K = 36
E_L = -54.4
g_L = 0.3

def sodium_channel(V, m, h):
    """
    The conductance of this channel depends on the 3 m open gates and 1 h open gate.

    I_Na = g_Na · m³ · h · (V − E_Na)

    | g_Na | 120 mS/cm² | Maximal sodium conductance |
    | E_Na | +50 mV | Sodium reversal potential |
    """
    return g_Na * m**3 * h * (V - E_Na)

def potassium_channel(V, n):
    """
    The conductance of this channel depends on the 4 n open gates. 

    I_K  = g_K  · n⁴ · (V − E_K)

    | g_K | 36 mS/cm² | Maximal potassium conductance |
    | E_K | −77 mV | Potassium reversal potential |
    """
    return g_K * n**4 * (V - (E_K))

def leaky_channel(V):
    """
    I_L  = g_L · (V − E_L)
    
    | g_L | 0.3 mS/cm² | Leak conductance (constant) |
    | E_L | −54.4 mV | Leak reversal potential |
    """
    return g_L * (V - (E_L))

# Test at steady-state gating and resting voltage
# V=-65
# print(f"Expected: Negative value, Got: {sodium_channel(V=V, m=m_inf(V=V), h=h_inf(V=V))}")
# print(f"Expected: Positive value, Got: {potassium_channel(V=V, n=n_inf(V=V))}")

# I_Na = sodium_channel(V=V, m=m_inf(V=V), h=h_inf(V=V))
# I_K = potassium_channel(V=V, n=n_inf(V=V))
# I_L = leaky_channel(V=V)

# print(f"Expected: 0, Got: {round(I_Na + I_K + I_L,0)}")
