import tkinter as tk
import random
import string
import wave
import struct
import math

# informations about the tools
def welcome():
    return (
        "Text shifter: a tool that shifts the letters of a string with the 'key' a->b and the reverse key b->a\n"
        "Letter shifter: a tool that replace a specific letter every time in a string\n"
        "White noise generator: a tool that can write white noise files and save them with .wav format\n"
        "Password generator: a tool that generates a password the lenght you want\n"
        "Calculator: a fully functional calculator"
    )

# text shifter block
def txtshifter():
    txt_window = tk.Toplevel(root)
    txt_window.geometry("500x500")
    txt_window.title("Text shifter")
    welcome = tk.Label(txt_window, text="Welcome to the text shifter, a tool to shift the letters of a string with the 'key' a->b and the reverse key b->a")
    welcome.pack()
    text = ""
    def enc():
        nonlocal text
        text = text_enter.get().lower()
        key = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[1:] + string.ascii_lowercase[0])
        text = text.translate(key)
        output_label.config(text=text)
    def dec():
        nonlocal text
        text = text_enter.get().lower()
        key = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[-1] + string.ascii_lowercase[:-1])
        text = text.translate(key)
        output_label.config(text=text)
    def copy_shifted_text():
        txt_window.clipboard_clear()
        txt_window.clipboard_append(text)
    text_enter = tk.Entry(txt_window)
    text_enter.pack(pady=10)
    output_label = tk.Label(txt_window, text=text, font=("Arial", 12))
    output_label.pack(pady=10)
    enc_button = tk.Button(txt_window, text="Encrypt", command=enc, bg="yellow", fg="black")
    enc_button.pack(pady=10)
    dec_button = tk.Button(txt_window, text="Decrypt", command=dec, bg="yellow", fg="black")
    dec_button.pack(pady=10)
    Copy_text = tk.Button(txt_window, text="Copy", command=copy_shifted_text, bg="red", fg="white")
    Copy_text.pack(pady=10)

def lettershifter():
    t_twist = ""

    def replace_letter():
        nonlocal t_twist
        letter2replace = l_replace_enter.get().lower()
        letter2place = l_place_enter.get().lower()
        tongue_twist = tongue_twist_enter.get().lower()
        t_twist = tongue_twist.replace(letter2replace, letter2place)
        output_label.config(text=t_twist)

    def Copy_the_tongue_twist():
        l_window.clipboard_clear()
        l_window.clipboard_append(t_twist)

    l_window = tk.Toplevel(root)
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
    output_label = tk.Label(l_window, text="")
    output_label.pack(pady=10)
    genera = tk.Button(l_window, text="Replace", command=replace_letter, bg="red", fg="white")
    genera.pack(pady=10)
    copy = tk.Button(l_window, text="Copy to\nthe clipboard", command=Copy_the_tongue_twist, bg="purple", fg="red")
    copy.pack(pady=10)

def wnoise():
    wn_window = tk.Toplevel(root)
    wn_window.geometry("500x500")
    wn_window.title("White noise generator")
    tk.Label(wn_window, text="Welcome to this white noise generator! :)").pack(pady=10)
    tk.Label(wn_window, text="Enter the duration in seconds: ").pack(pady=10)
    sample_rate = 44100
    wn_entry = tk.Entry(wn_window)
    wn_entry.pack()
    tk.Label(wn_window, text="Insert the name of the .wav file you want to create: ").pack(pady=20)
    wn_entry1 = tk.Entry(wn_window)
    wn_entry1.pack()
    output_label = tk.Label(wn_window, text="", font=("Arial", 12))
    output_label.pack(pady=20)
    def noise_generation():
        try:
            duration = int(wn_entry.get())
            if duration <= 0:
                output_label.config(text="Error: duration must be greater than 0.")
                return
        except ValueError:
            output_label.config(text="Error: insert a valid number")
            return
        num_samples = sample_rate * duration
        file_name = wn_entry1.get()
        if not file_name.endswith(".wav"):
            file_name += ".wav"
        with wave.open(file_name, "wb") as f:
            f.setnchannels(1)
            f.setsampwidth(2)
            f.setframerate(sample_rate)
            for _ in range(num_samples):
                value = random.randint(-32768, 32767)
                data = struct.pack('<h', value)
                f.writeframesraw(data)
            f.writeframes(b"")
        output_label.config(text=f"File '{file_name}' generated successfully!")
    tk.Button(wn_window, text="Generate", command=noise_generation, bg="red", fg="white").pack(pady=10)

def pwgenerator():
    pwg_window = tk.Toplevel(root)
    pwg_window.geometry("500x500")
    pwg_window.title("Password generator")
    tk.Label(pwg_window, text="Enter the lenght of the password: ").pack(pady=10)
    pwg_entry = tk.Entry(pwg_window)
    pwg_entry.pack()
    output_label = tk.Label(pwg_window, text="", font=("Arial", 12))
    output_label.pack(pady=20)
    def pwg():
        try:
            lenght = int(pwg_entry.get())
            if lenght <= 0:
                output_label.config(text="Error: lenght must be > 0")
                return
        except ValueError:
            output_label.config(text="Error: insert a valid number")
            return
        all_chars = string.ascii_letters + string.digits + string.punctuation
        pw = "".join(random.sample(all_chars, lenght))
        pwg_window.clipboard_clear()
        pwg_window.clipboard_append(pw)
        output_label.config(text=f"Password: \n{pw}")
        def copy():
            pwg_window.clipboard_clear()
            pwg_window.clipboard_append(pw)
        copy_btn = tk.Button(pwg_window, text="Copy", command=copy, bg="red", fg="white")
        copy_btn.pack()
    tk.Button(pwg_window, text="Generate", command=pwg, bg="red", fg="white").pack(pady=10)

def calculator():
    """Apre una finestra calcolatrice. Richiamabile da qualsiasi bottone."""
 
    win = tk.Toplevel()
    win.title("Calculator")
    win.resizable(False, False)
    win.configure(bg="#1e1e2e")
 
    # --- Stato interno ---
    expression = ""   # espressione completa (es. "12+5")
    new_input = True  # True = il prossimo digit sovrascrive il display
 
    # --- Display ---
    display_var = tk.StringVar(value="0")
    display = tk.Entry(
        win, textvariable=display_var,
        font=("Consolas", 28), bd=0, relief="flat",
        bg="#313244", fg="#cdd6f4", justify="right",
        insertbackground="#cdd6f4", state="readonly",
        readonlybackground="#313244"
    )
    display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(12, 6), ipady=10)
 
    # --- Logica bottoni ---
    def press_digit(d):
        nonlocal expression, new_input
        if new_input:
            display_var.set(d)
            new_input = False
        else:
            current = display_var.get()
            display_var.set("0" if current == "0" else current + d)
        expression += d
 
    def press_op(op):
        nonlocal expression, new_input
        # Evita doppio operatore (sostituisce l'ultimo se già presente)
        if expression and expression[-1] in "+-*/":
            expression = expression[:-1]
        elif not new_input:
            expression = display_var.get()  # sincronizza dopo un risultato
        expression += op
        display_var.set(op)
        new_input = True
 
    def press_equal():
        nonlocal expression, new_input
        try:
            result = eval(expression)  # noqa: S307
            # Mostra intero se senza decimali inutili
            display_var.set(int(result) if result == int(result) else round(result, 10))
            expression = str(result)
        except ZeroDivisionError:
            display_var.set("Div/0")
            expression = ""
        except Exception:
            display_var.set("Error")
            expression = ""
        new_input = True
 
    def press_clear():
        nonlocal expression, new_input
        expression = ""
        display_var.set("0")
        new_input = True
 
    def press_dot():
        nonlocal new_input
        if new_input:
            display_var.set("0.")
            new_input = False
        elif "." not in display_var.get():
            display_var.set(display_var.get() + ".")
 
    def press_sign():
        nonlocal expression
        current = display_var.get()
        if current not in ("0", "Error", "Div/0"):
            val = str(-float(current))
            val = str(int(float(val))) if float(val) == int(float(val)) else val
            display_var.set(val)
            # Aggiorna anche l'expression con il valore negato
            expression = val
 
    def press_percent():
        nonlocal expression
        try:
            val = float(display_var.get()) / 100
            display_var.set(int(val) if val == int(val) else round(val, 10))
            expression = str(val)
        except Exception:
            pass
 
    def press_sqrt():
        nonlocal expression, new_input
        try:
            val = math.sqrt(float(display_var.get()))
            display_var.set(int(val) if val == int(val) else round(val, 10))
            expression = str(val)
            new_input = True
        except ValueError:
            display_var.set("Error")
            expression = ""
            new_input = True
 
    # --- Layout bottoni ---
    BUTTONS = [
        ("C",   1, 0, press_clear),
        ("+/-", 1, 1, press_sign),
        ("%",   1, 2, press_percent),
        ("√",   1, 3, press_sqrt),
 
        ("7",   2, 0, lambda: press_digit("7")),
        ("8",   2, 1, lambda: press_digit("8")),
        ("9",   2, 2, lambda: press_digit("9")),
        ("÷",   2, 3, lambda: press_op("/")),
 
        ("4",   3, 0, lambda: press_digit("4")),
        ("5",   3, 1, lambda: press_digit("5")),
        ("6",   3, 2, lambda: press_digit("6")),
        ("×",   3, 3, lambda: press_op("*")),
 
        ("1",   4, 0, lambda: press_digit("1")),
        ("2",   4, 1, lambda: press_digit("2")),
        ("3",   4, 2, lambda: press_digit("3")),
        ("−",   4, 3, lambda: press_op("-")),
 
        (".",   5, 0, press_dot),
        ("0",   5, 1, lambda: press_digit("0")),
        ("⌫",   5, 2, lambda: display_var.set(display_var.get()[:-1] or "0")),
        ("+",   5, 3, lambda: press_op("+")),
 
        ("=",   6, 3, press_equal),
    ]
 
    # Colori per categoria
    def btn_color(label):
        if label in ("C", "+/-", "%"):
            return "#585b70", "#cdd6f4"
        if label in ("÷", "×", "−", "+", "=", "√"):
            return "#fab387", "#1e1e2e"
        return "#45475a", "#cdd6f4"
 
    for (label, row, col, cmd) in BUTTONS:
        if cmd is None:
            continue
        bg, fg = btn_color(label)
        tk.Button(
            win, text=label, command=cmd,
            font=("Consolas", 18, "bold"), bd=0, relief="flat",
            bg=bg, fg=fg, activebackground=fg, activeforeground=bg,
            cursor="hand2", width=4, height=2
        ).grid(row=row, column=col, padx=4, pady=4)
 
    # Griglia responsiva
    for i in range(4):
        win.grid_columnconfigure(i, weight=1)
 

# ── main window ──────────────────────────────

root = tk.Tk()
root.geometry("500x500")
root.title("NikiSuite")

tk.Label(root, text=welcome()).pack(pady=10)

pwg_button = tk.Button(root, text="Password \n generator", command=pwgenerator, bg="orange", fg="blue")
pwg_button.pack()
wn_button = tk.Button(root, text="White noise \n generator", command=wnoise, bg="orange", fg="blue")
wn_button.pack()
txt_button = tk.Button(root, text="Text shifter", command=txtshifter, bg="orange", fg="blue")
txt_button.pack()
l_button = tk.Button(root, text="Letter replacer", command=lettershifter, bg="orange", fg="blue")
l_button.pack()
calculator_button=tk.Button(root, text="Calculator", command=calculator, bg="orange", fg="blue")
calculator_button.pack()

root.mainloop()
