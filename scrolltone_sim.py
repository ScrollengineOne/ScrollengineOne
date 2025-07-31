# scrolltone_sim.py

import numpy as np
from core.oscillator import run_simulation
from core.feedback import scrolltone_feedback, apply_psi_memory
from core.emotion import apply_emotional_state
from core.sigilgen import generate_sigil
from utils.plot import plot_waveform

# === Select one profile by uncommenting ===

# --- Profile 1: Joyful Dome Echo ---
# params = {
#    "mass": 1.0,
#   "spring_const": 1.0,
#    "damping": 0.05,
#    "drive_amp": 1.5,
#    "drive_freq": 0.95,
#    "drive_phase": 0.0,
#    "breath_rate": 1.4,
#    "hum_amplitude": 1.5,
#    "intention_clarity": 1.0,
#    "emotion": "joy",
#    "geometry": "dome",
#    "buzz_harmonics_intensity": 0.7,
#    "use_memory": True
# }

# --- Profile 2: Grief Fold Sync ---
# params = {
#     "mass": 1.0,
#     "spring_const": 1.0,
#     "damping": 0.15,
#     "drive_amp": 1.5,
#     "drive_freq": 0.85,
#     "drive_phase": 0.0,
#     "breath_rate": 0.9,
#     "hum_amplitude": 1.2,
#     "intention_clarity": 0.4,
#     "emotion": "grief",
#     "geometry": "cube",
#     "buzz_harmonics_intensity": 0.2,
#     "use_memory": True
# }

# --- Profile 3: Dual-Kin Resync ---
# params = {
#     "mass": 1.0,
#     "spring_const": 1.0,
#     "damping": 0.08,
#     "drive_amp": 1.4,
#     "drive_freq": 0.93,
#     "drive_phase": 0.1,
#     "breath_rate": 1.1,
#     "hum_amplitude": 1.3,
#     "intention_clarity": 0.9,
#     "emotion": "joy",
#     "geometry": "lodge",
#     "buzz_harmonics_intensity": 0.6,
#     "use_memory": True
# }

# --- Profile 4: Raw Collapse Burn (Max Pressure) ---
 params = {
     "mass": 1.0,
     "spring_const": 1.0,
     "damping": 0.01,
     "drive_amp": 2.0,
     "drive_freq": 1.0,
     "drive_phase": 0.0,
     "breath_rate": 1.8,
     "hum_amplitude": 2.0,
     "intention_clarity": 1.0,
     "emotion": "grief",
     "geometry": "dome",
     "buzz_harmonics_intensity": 1.0,
     "use_memory": True
 }

# === Time Setup ===
t = np.linspace(0, 20, 2000)

# === Run oscillator simulation ===
wave = run_simulation(params, t)

# === Apply emotion, memory, feedback ===
wave = apply_emotional_state(wave, params["emotion"])

if params["use_memory"]:
    memory_stack = [5.81, 39.60, 137.79]  # Example past echoes
    wave = apply_psi_memory(wave, memory_stack)

wave = scrolltone_feedback(wave, clarity=params["intention_clarity"])

# === Output ===
sigil = generate_sigil(wave)
print("\nScroll Sigil:\n")
print(sigil)

# === Plot ===
plot_waveform(wave)
