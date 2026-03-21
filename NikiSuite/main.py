import random
import string
import wave
import struct

#welcome message
print("Welcome to NikiSuite, a suite of useful tools that can be fun and also useful to use")

while True:
    #info messages
    print("Text shifter: a tool that shifts the letters of a string with the 'key' a->b and the reverse key b->a")
    print("Letter shifter: a tool that replace a specific letter every time in a string")
    print("White noise generator: a tool that can write white noise files and save them with .wav format")
    print("insert one of these commands to run one of the tools above: txtshifter for the text shifter, lettershifter for the letter shifter and wnoise for the white noise generator")

    #error checking
    while (command := input().lower()) not in ["txtshifter", "lettershifter", "wnoise"]:
        print("error, insert again the input")
    
#text shifter block
    if command == "txtshifter":
        print("Welcome to text shifter, a tool to shift the letters of a string with the 'key' a->b and the reverse key b->a")
        print("insert yes if you want to use this tool")
    #error checking
        while (answer := input().lower()) not in ["yes", "no"]:
            print("error, insert again the answer")

        if answer == "no":
            quit
    #running block
        while answer == "yes":
            print("Insert enc for encrypting a message, insert dec for decrypting a message encrypted")
        #error checking of the choice between encryption and decription
            while (choose := input().lower()) not in ["enc", "dec"]:
                print("error, insert again the option")
        #encryption block
            if choose == "enc":
                print('insert text:')
                text = input()
                alphabet = string.ascii_lowercase
                shifted = alphabet[1:] + alphabet[0]
                key = str.maketrans(alphabet, shifted)
                print(text.translate(key))
        #decritption block
            if choose == "dec":
                print('insert text:')
                text = input()
                alphabet = string.ascii_lowercase
                shifted = alphabet[-1] + alphabet[:-1]
                key = str.maketrans(alphabet, shifted)
                print(text.translate(key))
        #exit/continue mechanic
            print("Do you want to use again this tool? insert yes or no")

            while (answer := input().lower()) not in ["yes", "no"]:
                print("error, insert answer again")

            if answer == "no":
                break
#letter replacer block
    if command == "lettershifter":
        answer = "yes"
        while answer == "yes":
            print('insert the letter to replace')
            letter2replace = input().upper()
            print('insert the letter to place in the place of the letter you want to replace')
            letter2place=input().upper()
            print('Insert the text you wanna remix')
            tongue_twist = input().upper()
            tongue_twist=tongue_twist.replace(letter2replace, letter2place)#replaces the letter you specified every time in a sentence or a word
            print(tongue_twist)
            print("Do you want to continue using this tool?")
            #error checking
            while (answer := input().lower()) not in ["yes", "no"]:
                print("error, insert the answer again between yes and no")
            if answer == "no":
                break
   #white noise block 
    if command == "wnoise":
        print("Welcome to this white noise generator! :)")
        sample_rate = 44100  # 44.1 kHz, audio standard

        # --- Input duration ---
        print("Insert a duration in seconds:")
        # duration's input error checking
        while (duration := int(input())) <= 0:
            print("Error: duration must be greater than 0. Insert again:")

        num_samples = sample_rate * duration  # Numero totale di campioni

        # --- Input file name
        print("Insert the name of the .wav file you want to create:")
        file_name = str(input())

        # if the user doesn't put the .wav in the input, we add it
        if not file_name.endswith(".wav"):
            file_name += ".wav"

        # audio creation
        with wave.open(file_name, "wb") as f:
            f.setnchannels(1)          # Mono
            f.setsampwidth(2)          # 16 bit
            f.setframerate(sample_rate)

            for _ in range(num_samples):
                value = random.randint(-32768, 32767)
                data = struct.pack('<h', value)
                f.writeframesraw(data)

            f.writeframes(b"")  # closes correctly the data block

        print(f"File '{file_name}' generated successfully!")
