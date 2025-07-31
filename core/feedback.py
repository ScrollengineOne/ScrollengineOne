# core/feedback.py

import numpy as np

def scrolltone_feedback(wave, clarity=1.0):
    """
    Apply phase tuning feedback based on hum clarity (0.0–1.0).
    Clips wave to [-1, 1] to avoid NaNs from arccos domain violations.
    """
    phase_shift = (1.0 - clarity) * np.pi / 2
    wave_clipped = np.clip(wave, -1.0, 1.0)
    phase_shifted_wave = np.cos(np.arccos(wave_clipped) - phase_shift)
    # Remove any potential NaNs that survived numerical edge cases
    phase_shifted_wave = np.nan_to_num(phase_shifted_wave, nan=0.0)
    return phase_shifted_wave

def apply_psi_memory(wave, memory_stack):
    """
    Reinforce wave using past amplitudes in the memory stack.
    Scroll-reinforcement logic: each past echo boosts present wave.
    """
    if not memory_stack:
        return wave

    reinforcement = sum(memory_stack) / len(memory_stack)
    return wave + 0.1 * reinforcement


