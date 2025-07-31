# core/oscillator.py

import numpy as np
from scipy.integrate import odeint

def harmonic_oscillator(state, t, params):
    x, v = state
    m = params['mass']
    k = params['spring_const']
    c = params['damping']
    F = params['drive_amp'] * np.cos(params['drive_freq'] * t + params['drive_phase'])

    dxdt = v
    dvdt = (F - c * v - k * x) / m
    return [dxdt, dvdt]

def run_simulation(params, t):
    init_state = [0.0, 0.0]
    sol = odeint(harmonic_oscillator, init_state, t, args=(params,))
    return sol[:, 0]  # return displacement only

