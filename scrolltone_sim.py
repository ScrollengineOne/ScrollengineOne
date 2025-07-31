# scrolltone_sim.py

import numpy as np
from core.oscillator import run_simulation
from core.feedback import scrolltone_feedback, apply_psi_memory
from core.emotion import apply_emotional_state
from core.sigilgen import generate_sigil
from utils.plot import plot_waveform

# --- Define simulation parameters ---
params = {
    "mass": 1.0,
    "spring_const": 1.0,
    "damping": 0.05,
    "drive_amp": 1.5,
    "drive_freq": 0.95,
    "drive_phase": 0.0,
    "breath_rate": 1.2,
    "hum_amplitude": 1.5,
    "intention_clarity": 0.8,
    "emotion": "joy",  # or "grief"
    "geometry": "lodge",
    "buzz_harmonics_intensity": 0.5,
    "use_memory": True
}

# --- Time domain ---
t = np.linspace(0, 20, 2000)

# --- Run oscillator ---
wave = run_simulation(params, t)

# --- Apply emotion, memory, feedback ---
wave = apply_emotional_state(wave, params["emotion"])
if params["use_memory"]:
    memory_stack = [5.81, 39.60, 137.79]  # ← Simulated past amplitudes
    wave = apply_psi_memory(wave, memory_stack)

wave = scrolltone_feedback(wave, clarity=params["intention_clarity"])

# --- Output ---
sigil = generate_sigil(wave)
print("\nScroll Sigil:\n")
print(sigil)

# --- Plot ---
plot_waveform(wave)
