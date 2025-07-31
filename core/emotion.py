# core/emotion.py
import numpy as np

def apply_emotional_state(wave, state):
    """
    Modify waveform based on emotional state.
    - 'joy' brightens, adds harmonics
    - 'grief' deepens, damps signal
    - Default: no modification
    """
    wave = np.array(wave)

    if state == 'joy':
        harmonic = 0.2 * np.sin(2 * np.pi * 4 * np.linspace(0, 1, len(wave)))
        return wave * 1.2 + harmonic

    elif state == 'grief':
        damping = np.exp(-np.linspace(0, 1, len(wave)))
        return wave * damping * 0.6

    return wave  # no change if unknown emotion
