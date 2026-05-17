from steady_state import m_inf, h_inf, n_inf
from rate_constants import alpha_m, beta_m
from rate_constants import alpha_h, beta_h
from rate_constants import alpha_n, beta_n

def m_gradient(V, m):
    """
    dm/dt = α_m(V)(1 − m) − β_m(V) m
    """
    
    return alpha_m(V) * (1 - m) - beta_m(V) * m

def h_gradient(V, h):
    """
    dh/dt = α_h(V)(1 − h) − β_h(V) h
    """
    
    return alpha_h(V) * (1 - h) - beta_h(V) * h

def n_gradient(V, n):
    """
    dn/dt = α_n(V)(1 − n) − β_n(V) n
    """
    
    return alpha_n(V) * (1 - n) - beta_n(V) * n


# Validate at resting voltage
# print(f"Expected: 0.0, Got: {m_gradient(V=-65, m=m_inf(V=-65))}")
# print(f"Expected: 0.0, Got: {h_gradient(V=-65, h=h_inf(V=-65))}")
# print(f"Expected: 0.0, Got: {n_gradient(V=-65, n=n_inf(V=-65))}")
