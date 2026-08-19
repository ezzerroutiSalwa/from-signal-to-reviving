sample_rate, signal = wavfile.read(filename)

print(signal.dtype)
#int16

signal = signal.astype(np.float32)
print("Type après conversion :", signal.dtype)
