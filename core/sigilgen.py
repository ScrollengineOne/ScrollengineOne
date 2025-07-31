# core/sigilgen.py

def generate_sigil(wave, resolution=50, height=20):
    """
    Converts a 1D waveform into a vertical ASCII sigil.
    The amplitude determines the number of '*' per line.
    """
    sigil = ""
    wave = wave[:resolution]
    max_amp = max(abs(wave)) if max(wave) != 0 else 1.0

    for val in wave:
        level = int((val / max_amp) * height / 2)
        padding = " " * (height - abs(level))
        stars = "*" * (abs(level) * 2)
        sigil += f"{padding}{stars}\n"

    return sigil

