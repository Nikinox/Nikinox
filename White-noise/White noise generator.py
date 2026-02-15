import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.signal import welch
import sounddevice as sd   # <--- libreria per riproduzione audio

# parameters
duration = 120  # seconds
sampling_rate = 43100  # samples per second (Hz)

# total number of samples
total_samples = duration * sampling_rate

# generate white noise
white_noise = np.random.normal(0, 1, total_samples)

# plot the white noise (first 1000 samples)
plt.figure(figsize=(10, 4))
plt.plot(white_noise[:1000])
plt.title("white noise signal")
plt.xlabel("sample number")
plt.ylabel("amplitude")
plt.show()

# save the white noise as a wav file

write('white_noise.wav', sampling_rate, white_noise.astype(np.float32))

# --- PLAY AUDIO ---
print("Riproduzione in corso... attenzione al volume!")
sd.play(white_noise, samplerate=sampling_rate)
sd.wait()   # blocca finché la riproduzione non è finita

# compute the power spectral density
frequencies, power_spectral_density = welch(white_noise, fs=sampling_rate, nperseg=1024)

# plot the power spectral density
plt.figure(figsize=(10, 4))
plt.semilogy(frequencies, power_spectral_density)
plt.title("power spectral density of white noise")
plt.xlabel("frequency (Hz)")
plt.ylabel("power spectral density (V^2/Hz)")
plt.show()


#qualche correzione e aiuto da Copilot
