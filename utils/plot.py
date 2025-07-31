# utils/plot.py

import matplotlib.pyplot as plt

def plot_waveform(wave, title="Scrolltone Waveform"):
    plt.figure(figsize=(10, 4))
    plt.plot(wave, color='orange', linewidth=1.2)
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

