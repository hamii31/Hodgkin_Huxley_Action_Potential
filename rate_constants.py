"""
**Goal:** Implement six functions of voltage. 
Each describes how fast a "gate" opens (α) or closes (β) at a given membrane potential.
"""

# IMPLEMENTATION

import math

def alpha_m(V):
    """
    Opening rate of sodium-activated gates (rate of depolarization)

    α_m(V) = 0.1 (V + 40) / (1 − exp(−(V + 40)/10))

    If-else statement to prevent NaN values.
    """
    if abs(V + 40) < 1e-5:
        return 1.0
    else:
        return 0.1 * (V + 40) / (1 - math.exp(-(V + 40)/10))

def beta_m(V):
    """
    Closing rate of sodium-activated gates (rate of polarization)

    β_m(V) = 4 exp(−(V + 65)/18)
    """
    return 4 * math.exp(-(V + 65)/18)

def alpha_h(V):
    """
    Opening rate of sodium-inhibited gates (rate of polarization)

    α_h(V) = 0.07 exp(−(V + 65)/20)
    """
    return 0.07 * math.exp(-(V + 65)/20)

def beta_h(V):
    """
    Closing rate of sodium-inhibited gates (rate of depolarization)

    β_h(V) = 1 / (1 + exp(−(V + 35)/10))
    """
    return 1 / (1 + math.exp(-(V + 35)/10))

def alpha_n(V):
    """
    Opening rate of potassium-activated gates (rate of depolarization)

    α_n(V) = 0.01 (V + 55) / (1 − exp(−(V + 55)/10))
    
    If-else statement to prevent NaN values.
    """
    if abs(V + 55) < 1e-5:
        return 0.1
    else:
        return 0.01 * (V + 55) / (1 - math.exp(-(V+55)/10))
    
def beta_n(V):
    """
    Closing rate of potassium-activated gates (rate of polarization)

    β_n(V) = 0.125 exp(−(V + 65)/80)
    """
    return 0.125 * math.exp(-(V + 65)/80)


# TESTING

# V = -65

# print("Testing at resting voltage: -65 mV")
# print(f"Expected: 0.2236, Got: {round(alpha_m(V=V),4)}")
# print(f"Expected: 4.0, Got: {beta_m(V=V)}")
# print(f"Expected: 0.07, Got: {alpha_h(V=V)}")
# print(f"Expected: 0.04743, Got: {round(beta_h(V=V),5)}")
# print(f"Expected: 0.05819, Got: {round(alpha_n(V=V),6)}")
# print(f"Expected: 0.125, Got: {round(beta_n(V=V),3)}")
