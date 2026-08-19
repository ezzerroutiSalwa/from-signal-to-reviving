import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Visualisation du signal PCG
# ==========================================

time = np.arange(len(signal)) / sample_rate

plt.figure(figsize=(14, 5))

plt.plot(time, signal)

plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("PCG après suppression du DC Offset")

plt.grid(True)
plt.tight_layout()
plt.show()
