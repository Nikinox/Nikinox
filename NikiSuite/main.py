import tkinter as tk
import random
import string
import wave
import struct
#informations about the tools
def welcome():
    return (
        "Text shifter: a tool that shifts the letters of a string with the 'key' a->b and the reverse key b->a\n"
        "Letter shifter: a tool that replace a specific letter every time in a string\n"
        "White noise generator: a tool that can write white noise files and save them with .wav format\n"
        "Password generator: a tool that generates a password the lenght you want"
    )
#text shifter block
def txtshifter():
    txt_window=tk.Toplevel(root)
    txt_window.geometry("500x500")
    txt_window.title("Text shifter")
    welcome=tk.Label(txt_window, text="Welcome to the text shifter, a tool to shift the letters of a string with the 'key' a->b and the reverse key b->a")
    welcome.pack()
    #error checking
    text=""
    def enc():
        nonlocal text
        text=text_enter.get().lower()
        key = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[1:] + string.ascii_lowercase[0])
        text=text.translate(key)
        output_label.config(text=text)
    def dec():
        nonlocal text
        text=text_enter.get().lower()
        key = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[-1] + string.ascii_lowercase[:-1])
        text=text.translate(key)
        output_label.config(text=text)
    def copy_shifted_text():
        txt_window.clipboard_clear()
        txt_window.clipboard_append(text)
    text_enter=tk.Entry(txt_window)
    text_enter.pack(pady=10)
    output_label=tk.Label(txt_window, text=text, font=("Arial", 12))
    output_label.pack(pady=10)
    enc_button=tk.Button(txt_window, text="Encrypt", command=enc, bg="yellow", fg="black")
    enc_button.pack(pady=10)
    dec_button=tk.Button(txt_window, text="Decrypt", command=dec, bg="yellow", fg="black")
    dec_button.pack(pady=10)
    Copy_text=tk.Button(txt_window, text="Copy", command=copy_shifted_text, bg="red", fg="white")
    Copy_text.pack(pady=10)
    txt_window.mainloop()
def lettershifter():
    t_twist = ""   # variabile condivisa

    def replace_letter():
        nonlocal t_twist

        # 1) reads the inputs
        letter2replace = l_replace_enter.get().lower()
        letter2place = l_place_enter.get().lower()
        tongue_twist = tongue_twist_enter.get().lower()

        # 2) replaces the letters
        t_twist = tongue_twist.replace(letter2replace, letter2place)

        # 3) updates the label
        output_label.config(text=t_twist)

    def Copy_the_tongue_twist():
        l_window.clipboard_clear()
        l_window.clipboard_append(t_twist)

    l_window = tk.Toplevel()
    l_window.geometry("500x500")
    l_window.title("Letter replacer")

    tk.Label(l_window, text='insert the letter to replace').pack(pady=10)
    l_replace_enter = tk.Entry(l_window)
    l_replace_enter.pack(pady=10)

    tk.Label(l_window, text='insert the letter to place').pack(pady=10)
    l_place_enter = tk.Entry(l_window)
    l_place_enter.pack(pady=10)

    tk.Label(l_window, text='Insert the text you want to remix').pack(pady=10)
    tongue_twist_enter = tk.Entry(l_window)
    tongue_twist_enter.pack(pady=10)

    # label
    output_label = tk.Label(l_window, text="")
    output_label.pack(pady=10)

    genera = tk.Button(l_window, text="Replace", command=replace_letter, bg="red", fg="white")
    genera.pack(pady=10)

    copy = tk.Button(l_window, text="Copy to\nthe clipboard", command=Copy_the_tongue_twist, bg="purple", fg="red")
    copy.pack(pady=10)
def wnoise():
    wn_window=tk.Toplevel(root)
    wn_window.geometry("500x500")
    wn_window.title("White noise generator")
    tk.Label(wn_window, text="Welcome to this white noise generator! :)")
    tk.Label(wn_window, text="Enter the duration in seconds: ").pack(pady=10)
    sample_rate = 44100  # 44.1 kHz, audio standard
    wn_entry=tk.Entry(wn_window)
    wn_entry.pack()
    tk.Label(wn_window, text="Insert the name of the .wav file you want to create: ").pack(pady=20)
    wn_entry1=tk.Entry(wn_window)
    wn_entry1.pack()
    output_label=tk.Label(wn_window, text="", font=("Arial", 12))
    output_label.pack(pady=20)
    def noise_generation():
        duration=int(wn_entry.get())
        try:
            if duration <= 0:
                output_label.config(text="Error: duration must be greater than 0. Insert again:")
                duration = int(wn_entry.get())
        except ValueError:
            output_label.config(text="Error: insert a valid number")
            tk.Label(output_label)
            return

        num_samples = sample_rate * duration  # Numero totale di campioni

            # --- Input file name
        file_name = wn_entry1.get()

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
        output_label.config(text=f"File '{file_name}' generated successfully!")
        tk.Label(output_label)
    tk.Button(wn_window, text="Generate", command=noise_generation, bg="red", fg="white").pack(pady=10)
    wn_window.mainloop()
def pwgenerator():
    pwg_window=tk.Toplevel(root)
    pwg_window.geometry("500x500")
    pwg_window.title("Password generator")

    tk.Label(pwg_window, text="Enter the lenght of the password: ").pack(pady=10)
    pwg_entry=tk.Entry(pwg_window)
    pwg_entry.pack()
    output_label=tk.Label(pwg_window, text="", font=("Arial", 12))
    output_label.pack(pady=20)

    def pwg():
        try:
            lenght = int(pwg_entry.get())
            if lenght<=0:
                output_label.config(text="Error: lenght must be > 0")
                return
        except ValueError:
            output_label.config(text="Error: insert a valid number")
            return
        all_chars = string.ascii_letters + string.digits + string.punctuation
        pw="".join(random.sample(all_chars, lenght))
        pwg_window.clipboard_clear()
        pwg_window.clipboard_append(pw)
        output_label.config(text=f"Password: \n{pw}\nthe password was copied to clipboard successfully")
        def copy():
            pwg_window.clipboard_clear()
            pwg_window.clipboard_append(pw)
        copy=tk.Button(text="Copy", command=copy, bg="red", fg="white")
        copy.pack()
        tk.Label(output_label)
    tk.Button(pwg_window, text="Generate", command=pwg, bg="red", fg="white").pack(pady=10)
root=tk.Tk()
root.geometry("500x500")
root.title("NikiSuite")
tk.Label(root, text=welcome()).pack()
pwg_button = tk.Button(text="Password \n generator", command=pwgenerator, bg="orange", fg="blue")
pwg_button.pack()
wn_button = tk.Button(text="White noise \n generator", command=wnoise, bg="orange", fg="blue")
wn_button.pack()
txt_button=tk.Button(text="Text shifter", command=txtshifter, bg="orange", fg="blue")
txt_button.pack()
l_button=tk.Button(text="Letter replacer", command=lettershifter, bg="orange", fg="blue")
l_button.pack()
root.mainloop()
