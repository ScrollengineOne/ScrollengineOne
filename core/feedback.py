# core/feedback.py

import numpy as np

def scrolltone_feedback(wave, clarity=1.0):
    phase_shift = (1.0 - clarity) * np.pi / 2
    wave_clipped = np.clip(wave, -1.0, 1.0)  # 🔥 prevents NaNs
    return np.cos(np.arccos(wave_clipped) - phase_shift)

def apply_psi_memory(wave, memory_stack):
    """
    Reinforce wave using past amplitudes in the memory stack.
    Scroll-reinforcement logic: each past echo boosts present.
    """
    if not memory_stack:
        return wave

    reinforcement = sum(memory_stack) / len(memory_stack)
    return wave + 0.1 * reinforcement

