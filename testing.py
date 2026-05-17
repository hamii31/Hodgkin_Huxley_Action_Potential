import math
from rate_constants import alpha_m, alpha_h, alpha_n, beta_m, beta_h, beta_n
from steady_state_values import m_inf, h_inf, n_inf, tau_m, tau_h, tau_n
from gating_ODEs import m_gating, h_gating, n_gating
from ionic_currents import sodium_channel, potassium_channel, leaky_channel
from dynamical_system import dynamical_system

# CONSTANTS
V_rest = -65

# === Test the rate constants ===

print("Testing rate constants at resting voltage...")

alpha_m_rest = 0.2236
beta_m_rest = 4.0
alpha_h_rest = 0.07
beta_h_rest = 0.04743
alpha_n_rest = 0.058198
beta_n_rest = 0.125

rate_dict = {"alpha_m_rest":math.isclose(a=alpha_m_rest, b=alpha_m(V=V_rest), abs_tol=1e-3),
             "beta_m_rest":math.isclose(a=beta_m_rest, b=beta_m(V=V_rest), abs_tol=1e-3),
             "alpha_h_rest":math.isclose(a=alpha_h_rest, b=alpha_h(V=V_rest), abs_tol=1e-3),
             "beta_h_rest":math.isclose(a=beta_h_rest, b=beta_h(V=V_rest), abs_tol=1e-3),
             "alpha_n_rest":math.isclose(a=alpha_n_rest, b=alpha_n(V=V_rest), abs_tol=1e-3),
             "beta_n_rest":math.isclose(a=beta_n_rest, b=beta_n(V=V_rest), abs_tol=1e-3)}

if all(rate_dict.values()):
    print("All tests successfully passed.")
else:
    find_what_failed = {key: value for key,
                 value in rate_dict.items() if value == False}
    
    print(find_what_failed)



# === Test the steady state values and time constants ===

ssv_tc_dict = {}

print("Testing steady state values and time constants at resting voltage...")

m_inf_rest = 0.0529
h_inf_rest = 0.596
n_inf_rest = 0.318
tau_m_rest = 0.237
tau_h_rest = 8.52
tau_n_rest = 5.46

ssv_tc_dict = {"m_inf_rest":math.isclose(a=m_inf_rest, b=m_inf(V=V_rest), abs_tol=1e-3),
               "h_inf_rest":math.isclose(a=h_inf_rest, b=h_inf(V=V_rest), abs_tol=1e-3),
               "n_inf_rest":math.isclose(a=n_inf_rest, b=n_inf(V=V_rest), abs_tol=1e-3),
               "tau_m_rest":math.isclose(a=tau_m_rest, b=tau_m(V_rest), abs_tol=1e-3),
               "tau_h_rest":math.isclose(a=tau_h_rest, b=tau_h(V_rest), abs_tol=5e-3),
               "tau_n_rest":math.isclose(a=tau_n_rest, b=tau_n(V_rest), abs_tol=5e-3)}

if all(ssv_tc_dict.values()):
    print("All tests successfully passed.")
else:
    find_what_failed = {key: value for key,
                 value in ssv_tc_dict.items() if value == False}
    
    print(find_what_failed)



# === Test the gating ODEs === 

gating_ODEs_dict = {}

print("testing the gating ODEs at resting steady state and resting membrane voltage...")

m_gating_rest = 0.0
h_gating_rest = 0.0
n_gating_rest = 0.0

gating_ODEs_dict = {"m_gating_rest":math.isclose(a=m_gating_rest, b=m_gating(V=V_rest, m=m_inf(V=V_rest)), abs_tol=1e-3),
                    "h_gating_rest":math.isclose(a=h_gating_rest, b=h_gating(V=V_rest, h=h_inf(V=V_rest)), abs_tol=1e-3),
                    "n_gating_rest":math.isclose(a=n_gating_rest, b=n_gating(V=V_rest, n=n_inf(V=V_rest)), abs_tol=1e-3)}

if all(gating_ODEs_dict.values()):
    print("All tests successfully passed.")
else:
    find_what_failed = {key: value for key,
                 value in gating_ODEs_dict.items() if value == False}
    
    print(find_what_failed)



# === Test the ionic channels ===

print("Testing ionic currents at resting steady state and resting membrane voltage...")

total_membrane_current_rest = 0.0

I_Na = sodium_channel(V=V_rest, m=m_inf(V=V_rest), h=h_inf(V=V_rest))
I_K = potassium_channel(V=V_rest, n=n_inf(V=V_rest))
I_L = leaky_channel(V=V_rest)

if math.isclose(a=total_membrane_current_rest, b=I_Na + I_K + I_L, abs_tol=1e-3):
    print("All tests successfully passed.")
else:
    print("Something isn't right with your ionic currents implementation.")



# === Test the dynamical system ===

dyn_sys_dict = {}

print("Testing dynamical system at rest...")

rest_state = (V_rest, m_inf(V=V_rest), h_inf(V=V_rest), n_inf(V=V_rest))
t_rest = 0
derivatives = dynamical_system(t=t_rest, state=rest_state)

dV_dt_rest = 0.0
dm_dt_rest = 0.0
dh_dt_rest = 0.0
dn_dt_rest = 0.0

dyn_sys_dict = {"dV_dt_rest":math.isclose(a=dV_dt_rest, b=derivatives[0], abs_tol=1e-3),
                "dm_dt_rest":math.isclose(a=dm_dt_rest, b=derivatives[1], abs_tol=1e-3),
                "dh_dt_rest":math.isclose(a=dh_dt_rest, b=derivatives[2], abs_tol=1e-3),
                "dn_dt_rest":math.isclose(a=dn_dt_rest, b=derivatives[3], abs_tol=1e-3)}

if all(dyn_sys_dict.values()):
    print("All tests successfully passed.")
else:
    find_what_failed = {key: value for key,
                 value in dyn_sys_dict.items() if value == False}
    
    print(find_what_failed)
