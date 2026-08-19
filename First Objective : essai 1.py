from pathlib import Path
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# ============================================================
# 1. Dataset path
# ============================================================

dataset_path = Path(
    r"Downloads\the-circor-digiscope-phonocardiogram-dataset-1.0.3"
)


# ============================================================
# 2. Find all WAV files
# ============================================================

wav_files = list(dataset_path.rglob("*.wav"))

print("Nombre de fichiers WAV :", len(wav_files))


# ============================================================
# 3. Check if files exist
# ============================================================

if len(wav_files) == 0:

    print("❌ Aucun fichier WAV trouvé.")

else:

    # On analyse le premier fichier
    filename = wav_files[0]

    print("\nPremier fichier trouvé :")
    print(filename)


    # ========================================================
    # 4. Load audio
    # ========================================================

    sample_rate, signal = wavfile.read(filename)

    print("\nInformations avant conversion :")
    print("Sample rate :", sample_rate)
    print("Shape :", signal.shape)


    # ========================================================
    # 5. Convert stereo to mono if necessary
    # ========================================================

    if signal.ndim == 1:

        # Le fichier est déjà mono
        print("➡️ Le fichier est déjà MONO")

    elif signal.ndim == 2:

        # Le fichier possède plusieurs canaux
        print("➡️ STÉRÉO détecté")
        print("Nombre de canaux :", signal.shape[1])

        # Conversion en mono
        signal = np.mean(signal, axis=1)

        print("✅ Conversion STÉRÉO → MONO effectuée")

    else:

        raise ValueError("❌ Format audio non supporté")


    # ========================================================
    # 6. Information after conversion
    # ========================================================

    print("\nInformations après conversion :")
    print("Shape :", signal.shape)

    sample_rate, signal = wavfile.read(filename)

    print("Type avant conversion :", signal.dtype)

    signal = signal.astype(np.float32)

    print("Type après conversion :", signal.dtype)

    dc_offset = np.mean(signal)

    print("DC Offset :", dc_offset)

    print("Minimum :", np.min(signal))
    print("Maximum :", np.max(signal))
    print("Moyenne :", np.mean(signal))
    print("Écart-type :", np.std(signal))

    signal_std = np.std(signal)

    dc_ratio = abs(dc_offset) / signal_std

    print("DC Offset :", dc_offset)
    print("Écart-type :", signal_std)
    print("DC Offset relatif :", dc_ratio)

    signal = signal - np.mean(signal)
    print("Nouvelle moyenne :", np.mean(signal))

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

    # ==========================================
    # Analyse fréquentielle avec FFT
    # ==========================================

    N = len(signal)

    # FFT
    fft_signal = np.fft.rfft(signal)

    # Fréquences correspondantes
    frequencies = np.fft.rfftfreq(N, d=1 / sample_rate)

    # Magnitude du spectre
    magnitude = np.abs(fft_signal)

    # Visualisation
    plt.figure(figsize=(14, 5))

    plt.plot(frequencies, magnitude)

    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Spectre fréquentiel du PCG - FFT")

    plt.xlim(0, sample_rate / 2)

    plt.grid(True)
    plt.tight_layout()
    plt.show()
