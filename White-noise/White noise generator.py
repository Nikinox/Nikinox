import wave
import struct
import random

print("welcome to this white noise generator! :)")
sample_rate = 44100  #  (44.1 kHz, audio standard)
print("insert a duration in seconds")
duration = int(input())        # white noise's duration in seconds
while duration <= 0:
    print("error, please insert again the duration in seconds")
    duration = int(input())
num_samples = sample_rate * duration

print("insert the name of the .wav file you want to create")
file_name = str(input())  # file name input

with wave.open(file_name, "w") as f:  #  opens a new .wav file
    f.setnchannels(1)                 # sets one audio channel (mono)
    f.setsampwidth(2)
    f.setframerate(sample_rate)       # sets the sample rate (campioni al secondo)

    for _ in range(num_samples):      # cycle for the frequencies
        value = random.randint(-32768, 32767)
        data = struct.pack('<h', value)
        f.writeframesraw(data)                 # writes the bytes in the audio file

    f.writeframes(b"")              # closes the audio data nblock

print(f"File '{file_name}' generato con successo.")  # Messaggio di conferma a fine esecuzione
