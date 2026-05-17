from rate_constants import alpha_m, alpha_h, alpha_n, beta_m, beta_h, beta_n

def m_inf(V):
    """
    Derive the steady-state var of sodium-activated gates

    x_∞ = α/(α+β)
    """
    return alpha_m(V) / (alpha_m(V) + beta_m(V))

def tau_m(V):
    """
    Derive the timeframe per opening/closing of gates

    τ_x = 1/(α+β)
    """
    return 1 / (alpha_m(V) + beta_m(V))

def h_inf(V):
    """
    Derive the steady-state var of sodium-inhibited gates

    x_∞ = α/(α+β)
    """
    return alpha_h(V) / (alpha_h(V) + beta_h(V))

def tau_h(V):
    """
    Derive the timeframe per opening/closing of gates

    τ_x = 1/(α+β)
    """
    return 1 / (alpha_h(V) + beta_h(V))

def n_inf(V):
    """
    Derive the steady-state var of potassium-activated gates

    x_∞ = α/(α+β)
    """
    return alpha_n(V) / (alpha_n(V) + beta_n(V))

def tau_n(V):
    """
    Derive the timeframe per opening/closing of gates

    τ_x = 1/(α+β)
    """
    return 1 / (alpha_n(V) + beta_n(V))
