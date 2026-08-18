import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# ==========================================
# 1. Charger le signal audio
# ==========================================

filename = r"C:\Users\HP\Downloads\the-circor-digiscope-phonocardiogram-dataset-1.0.3\the-circor-digiscope-phonocardiogram-dataset-1.0.3\training_data\13918_MV.wav"

fs, signal = wavfile.read(filename)

print("Fréquence d'échantillonnage :", fs, "Hz")
print("Nombre d'échantillons :", len(signal))

# Si le signal est stéréo, prendre un seul canal
if signal.ndim > 1:
    signal = signal[:, 0]

# Conversion en float
signal = signal.astype(float)

# Normalisation
signal = signal / np.max(np.abs(signal))

# ==========================================
# 2. Découpage en fenêtres
# ==========================================

window_duration = 1.0  # durée d'une fenêtre en secondes
window_size = int(window_duration * fs)

N = len(signal)

# Nombre de fenêtres complètes
n_windows = N // window_size

# Vecteurs pour stocker les résultats
mean_vector = []
variance_vector = []
time_vector = []

# ==========================================
# 3. Calcul de l'espérance et de la variance
# ==========================================

for i in range(n_windows):

    start = i * window_size
    end = start + window_size

    window = signal[start:end]

    # Espérance = moyenne
    mean = np.mean(window)

    # Variance
    variance = np.var(window)

    mean_vector.append(mean)
    variance_vector.append(variance)

    # Temps correspondant au centre de la fenêtre
    time_vector.append((start + end) / (2 * fs))

# Conversion en numpy array
mean_vector = np.array(mean_vector)
variance_vector = np.array(variance_vector)
time_vector = np.array(time_vector)

# ==========================================
# 4. Affichage des vecteurs
# ==========================================

print("\nVecteur des espérances :")
print(mean_vector)

print("\nVecteur des variances :")
print(variance_vector)

# ==========================================
# 5. Affichage
# ==========================================

plt.figure(figsize=(12, 8))

# Signal original
plt.subplot(3, 1, 1)
plt.plot(np.arange(N) / fs, signal)
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.title("Signal PCG")
plt.grid()

# Espérance
plt.subplot(3, 1, 2)
plt.plot(time_vector, mean_vector, marker='o')
plt.xlabel("Temps (s)")
plt.ylabel("Espérance")
plt.title("Évolution de l'espérance")
plt.grid()

# Variance
plt.subplot(3, 1, 3)
plt.plot(time_vector, variance_vector, marker='o')
plt.xlabel("Temps (s)")
plt.ylabel("Variance")
plt.title("Évolution de la variance")
plt.grid()

plt.tight_layout()
plt.show()
