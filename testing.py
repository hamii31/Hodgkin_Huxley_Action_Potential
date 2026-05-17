import math

# CONSTANTS
V_rest = -65

# Test the rate constants
from rate_constants import alpha_m, alpha_h, alpha_n, beta_m, beta_h, beta_n

alpha_m_rest = 0.2236
beta_m_rest = 4.0
alpha_h_rest = 0.07
beta_h_rest = 0.04743
alpha_n_rest = 0.058198
beta_n_rest = 0.125
print("Testing rate constants at resting voltage...")
print(math.isclose(a=alpha_m_rest, b=round(alpha_m(V=V_rest),4)))
print(math.isclose(a=beta_m_rest, b=beta_m(V=V_rest)))
print(math.isclose(a=alpha_h_rest, b=alpha_h(V=V_rest)))
print(math.isclose(a=beta_h_rest, b=round(beta_h(V=V_rest),5)))
print(math.isclose(a=alpha_n_rest, b=round(alpha_n(V=V_rest),6)))
print(math.isclose(a=beta_n_rest, b=round(beta_n(V=V_rest),3)))

# Test the steady state values and time constants
from steady_state import m_inf, h_inf, n_inf, tau_m, tau_h, tau_n

m_inf_rest = 0.0529
h_inf_rest = 0.596
n_inf_rest = 0.318
tau_m_rest = 0.237
tau_h_rest = 8.52
tau_n_rest = 5.46
print("Testing steady state values and time constants at resting voltage...")
print(math.isclose(a=m_inf_rest, b=round(m_inf(V=V_rest),4)))
print(math.isclose(a=h_inf_rest, b=round(h_inf(V=V_rest),3)))
print(math.isclose(a=n_inf_rest, b=round(n_inf(V=V_rest),3)))
print(math.isclose(a=tau_m_rest, b=round(tau_m(V_rest),3)))
print(math.isclose(a=tau_h_rest, b=round(tau_h(V_rest),2)))
print(math.isclose(a=tau_n_rest, b=round(tau_n(V_rest),2)))

# Test the gating ODEs
from gating_ODEs import m_gating, h_gating, n_gating

print("testing the gating ODEs at resting steady state and resting membrane voltage...")

m_gating_rest = 0.0
h_gating_rest = 0.0
n_gating_rest = 0.0
print(math.isclose(a=m_gating_rest, b=m_gating(V=V_rest, m=m_inf(V=V_rest))))
print(math.isclose(a=h_gating_rest, b=h_gating(V=V_rest, h=h_inf(V=V_rest))))
print(math.isclose(a=n_gating_rest, b=n_gating(V=V_rest, n=n_inf(V=V_rest))))

# Test the ionic channels
from ionic_currents import sodium_channel, potassium_channel, leaky_channel

print("Testing ionic currents at resting steady state and resting membrane voltage...")

total_membrane_current_rest = 0.0

I_Na = sodium_channel(V=V_rest, m=m_inf(V=V_rest), h=h_inf(V=V_rest))
I_K = potassium_channel(V=V_rest, n=n_inf(V=V_rest))
I_L = leaky_channel(V=V_rest)

print(math.isclose(a=total_membrane_current_rest, b=round(I_Na + I_K + I_L, 1)))

# Test the dynamical system
from dynamical_system import dynamical_system

print("Testing dynamical system at rest...")

rest_state = (V_rest, m_inf(V=V_rest), h_inf(V=V_rest), n_inf(V=V_rest))
t_rest = 0
derivatives = dynamical_system(t=t_rest, state=rest_state)

dV_dt_rest = 0.0
dm_dt_rest = 0.0
dh_dt_rest = 0.0
dn_dt_rest = 0.0
print(math.isclose(a=dV_dt_rest, b=round(derivatives[0],1)))
print(math.isclose(a=dm_dt_rest, b=round(derivatives[1],1)))
print(math.isclose(a=dh_dt_rest, b=round(derivatives[2],1)))
print(math.isclose(a=dn_dt_rest, b=round(derivatives[3],1)))
