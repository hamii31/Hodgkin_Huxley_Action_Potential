from rate_constants import alpha_m, beta_m
from rate_constants import alpha_h, beta_h
from rate_constants import alpha_n, beta_n

def m_gating(V, m):
    """
    dm/dt = α_m(V)(1 − m) − β_m(V) m
    """
    
    return alpha_m(V) * (1 - m) - beta_m(V) * m

def h_gating(V, h):
    """
    dh/dt = α_h(V)(1 − h) − β_h(V) h
    """
    
    return alpha_h(V) * (1 - h) - beta_h(V) * h

def n_gating(V, n):
    """
    dn/dt = α_n(V)(1 − n) − β_n(V) n
    """
    
    return alpha_n(V) * (1 - n) - beta_n(V) * n
