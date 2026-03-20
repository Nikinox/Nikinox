import wave
import struct
import random

print("Welcome to this white noise generator! :)")

sample_rate = 44100  # 44.1 kHz, audio standard

# --- Input duration ---
print("Insert a duration in seconds:")
duration = int(input())

# duration's input error checking
while duration <= 0:
    print("Error: duration must be greater than 0. Insert again:")
    duration = int(input())

num_samples = sample_rate * duration  # Numero totale di campioni

# --- Input file name
print("Insert the name of the .wav file you want to create:")
file_name = str(input())

# if the user doesn't put the .wav in the input, we add it
if not file_name.endswith(".wav"):
    file_name += ".wav"

# audio creation
with wave.open(file_name, "w") as f:
    f.setnchannels(1)          # Mono
    f.setsampwidth(2)          # 16 bit
    f.setframerate(sample_rate)

    for _ in range(num_samples):
        value = random.randint(-32768, 32767)
        data = struct.pack('<h', value)
        f.writeframesraw(data)

    f.writeframes(b"")  # closes correctly the data block

print(f"File '{file_name}' generated successfully!")
