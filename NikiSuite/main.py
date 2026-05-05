import tkinter as tk
import random
import string
import wave
import struct
import math
from tkinter import filedialog

# informations about the tools
def welcome():
    return (
        "Text shifter: a tool that shifts the letters of a string with the 'key' a->b and the reverse key b->a\n"
        "Letter shifter: a tool that replace a specific letter every time in a string\n"
        "White noise generator: a tool that can write white noise files and save them with .wav format\n"
        "Password generator: a tool that generates a password the lenght you want\n"
        "Text editor: a tool that can edit text(it has some issues)"
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
 

def text_editor():
    txt_window = tk.Toplevel(root)
    txt_window.title("NikiText")
    txt_window.geometry("650x650")

    current_file = None   # Tracks the currently opened/saved file

    def save_file():
        global current_file

        # If no file has been saved yet → behave like Save As
        if current_file is None:
            save_as_file()
            return

        # If a file already exists → overwrite it
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(my_text.get("1.0", tk.END))

        # Update window title
        txt_window.title(f"{current_file} - NikiText")


    def new_file():
        global current_file

        # If no file is currently saved → just clear the text area
        if current_file is None:
            my_text.delete(1.0, tk.END)
            txt_window.title("New File - NikiText")
        else:
            # If a file is saved → reset the file reference and clear the editor
            current_file = None
            my_text.delete(1.0, tk.END)
            txt_window.title("New File - NikiText")

    def open_file():
        # Clear the editor before loading a new file
        my_text.delete(1.0, tk.END)

        # Open file dialog with multiple supported extensions
        text_file = filedialog.askopenfilename(
            title="Open File",
            filetypes=(
                ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"),
                ("Java Files", "*.java"), ("C++ Files", "*.cpp"), ("C Files", "*.c"),
                ("Batch Files", "*.bat"), ("Bash files", "*.sh"), ("Rust files", "*.rs"),
                ("C# Files", "*.cs"), ("Kotlin Files", "*.kt"), ("Swift Files", "*.swift"),
                ("Ruby Files", "*.rb"), ("GO files", "*.go"), ("PHP files", "*.php"),
                ("JavaScript Files", "*.js"), ("TypeScript Files", "*.ts"), ("CSS Files", "*.css"),
                ("XML files", "*.xml"), ("YAML Files", "*.yml"), ("JSON Files", "*.json"),
                ("PowerShell Files", "*.ps1"), ("Perl Files", "*.pl"), ("Lua Files", "*.lua"),
                ("R Files", "*.r"), ("All Files", "*.*")
            )
        )

    def save_as_file():
        # Save As dialog with default extension and supported formats
        text_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            title="Save File",
            filetypes=(
                ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"),
                ("Java Files", "*.java"), ("C++ Files", "*.cpp"), ("C Files", "*.c"),
                ("Batch Files", "*.bat"), ("Bash files", "*.sh"), ("Rust files", "*.rs"),
                ("C# Files", "*.cs"), ("Kotlin Files", "*.kt"), ("Swift Files", "*.swift"),
                ("Ruby Files", "*.rb"), ("GO files", "*.go"), ("PHP files", "*.php"),
                ("JavaScript Files", "*.js"), ("TypeScript Files", "*.ts"), ("CSS Files", "*.css"),
                ("XML files", "*.xml"), ("YAML Files", "*.yml"), ("JSON Files", "*.json"),
                ("PowerShell Files", "*.ps1"), ("Perl Files", "*.pl"), ("Lua Files", "*.lua"),
                ("R Files", "*.r"), ("All Files", "*.*")
            )
        )

        # If the user selected a file path
        if text_file:
            name = text_file   # Placeholder for future save logic
        text_file=tk.open(text_file, "w")
        text_file.write(my_text.get(1.0, tk.END))
        text_file.close()


    my_frame = tk.Frame(txt_window)
    my_frame.pack(pady=5)

    text_scroll = tk.Scrollbar(my_frame)
    text_scroll.pack(side="right", fill="y")

    my_text = tk.Text(
        my_frame,
        width=102,
        height=51,
        font=("Arial", 16),
        selectbackground="blue",
        selectforeground="white",
        undo=True,
        yscrollcommand=text_scroll.set
    )
    my_text.pack()

    text_scroll.config(command=my_text.yview)

    my_menu = tk.Menu(txt_window)
    txt_window.configure(menu=my_menu)

    #file menu

    file_menu = tk.Menu(my_menu, tearoff=False)

    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As", command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=txt_window.quit)

    #edit menu

    edit_menu = tk.Menu(my_menu, tearoff=False)

    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")

    txt_window.mainloop()
def gamesuite():
    gamesuite_wn=tk.Toplevel(root)
    gamesuite_wn.geometry("500x500")
    gamesuite_wn.title("GameSuite")
    def tictactoe():
        tictactoe_wn=tk.Toplevel(gamesuite_wn)
        tictactoe_wn.geometry("500x500")
        tictactoe_wn.title("TIC TAC TOE")
        cells=[0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn=0
        btn = {"width": 5, "height": 2}
        c1=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c2=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c3=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c4=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c5=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c6=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c7=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c8=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        c9=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
        for i in range(3):
            tictactoe_wn.grid_columnconfigure(i, weight=1, uniform="col")
            tictactoe_wn.grid_rowconfigure(i, weight=1, uniform="row")
        c1.grid(row=0, column=0, padx=10, pady=10)
        c2.grid(row=0, column=1, padx=10, pady=10)
        c3.grid(row=0, column=2, padx=10, pady=10)

        c4.grid(row=1, column=0, padx=10, pady=10)
        c5.grid(row=1, column=1, padx=10, pady=10)
        c6.grid(row=1, column=2, padx=10, pady=10)

        c7.grid(row=2, column=0, padx=10, pady=10)
        c8.grid(row=2, column=1, padx=10, pady=10)
        c9.grid(row=2, column=2, padx=10, pady=10)

        choice = tk.Entry(tictactoe_wn)
        choice.grid()
        def fill_the_cell():
            nonlocal turn
            cell=int(choice.get())
            if turn == 0:
                match cell:
                    case 1:
                        if cells[0] == 0:
                            c1.config(text="X")
                            cells[0] = 2
                    case 2:
                        if cells[1] == 0:
                            c2.config(text="X")
                            cells[1] = 2
                    case 3:
                        if cells[2] == 0:
                            c3.config(text="X")
                            cells[2] = 2
                    case 4:
                        if cells[3] == 0:
                            c4.config(text="X")
                            cells[3] = 2
                    case 5:
                        if cells[4] == 0:
                            c5.config(text="X")
                            cells[4] = 2
                    case 6:
                        if cells[5] == 0:
                            c6.config(text="X")
                            cells[5] = 2
                    case 7:
                        if cells[6] == 0:
                            c7.config(text="X")
                            cells[6] = 2
                    case 8:
                        if cells[7] == 0:
                            c8.config(text="X")
                            cells[7] = 2
                    case 9:
                        if cells[8] == 0:
                            c9.config(text="X")
                            cells[8] = 2
                turn = 1
            elif turn == 1:
                match cell:
                    case 1:
                        if cells[0] == 0:
                            c1.config(text="O")
                            cells[0] = 1
                    case 2:
                        if cells[1] == 0:
                            c2.config(text="O")
                            cells[1] = 1
                    case 3:
                        if cells[2] == 0:
                            c3.config(text="O")
                            cells[2] = 1
                    case 4:
                        if cells[3] == 0:
                            c4.config(text="O")
                            cells[3] = 1
                    case 5:
                        if cells[4] == 0:
                            c5.config(text="O")
                            cells[4] = 1
                    case 6:
                        if cells[5] == 0:
                            c6.config(text="O")
                            cells[5] = 1
                    case 7:
                        if cells[6] == 0:
                            c7.config(text="O")
                            cells[6] = 1
                    case 8:
                        if cells[7] == 0:
                            c8.config(text="O")
                            cells[7] = 1
                    case 9:
                        if cells[8] == 0:
                            c9.config(text="O")
                            cells[8] = 1
                turn = 0
            c1.grid()
            c2.grid()
            c3.grid()
            c4.grid()
            c5.grid()
            c6.grid()
            c7.grid()
            c8.grid()
            c9.grid()
            if cells[0]*cells[1]*cells[2]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[3]*cells[4]*cells[5]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[6]*cells[7]*cells[8]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[0]*cells[3]*cells[6]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[1]*cells[4]*cells[7]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[2]*cells[5]*cells[8]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[0]*cells[4]*cells[8]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            elif cells[2]*cells[4]*cells[6]==1:
                win=tk.Label(tictactoe_wn, text="Vittoria O")
            if cells[0]*cells[1]*cells[2]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[3]*cells[4]*cells[5]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[6]*cells[7]*cells[8]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[0]*cells[3]*cells[6]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[1]*cells[4]*cells[7]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[2]*cells[5]*cells[8]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[0]*cells[4]*cells[8]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            elif cells[2]*cells[4]*cells[6]==8:
                win=tk.Label(tictactoe_wn, text="Vittoria X")
            win.grid(row=3, column=0, columnspan=3)
        confirm = tk.Button(tictactoe_wn, text="OK", command=fill_the_cell)
        confirm.grid()
        tictactoe_wn.mainloop()

    tictactoe_button=tk.Button(gamesuite_wn, text="TICTACTOE", bg="orange", fg="blue", command=tictactoe)
    tictactoe_button.pack()
    gamesuite_wn.mainloop()

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
text_editor_button=tk.Button(root, text="Text Editor", command=text_editor, bg="orange", fg="blue")
text_editor_button.pack()
game_suite=tk.Button(root, text="GameSuite", bg="orange", fg="blue", command=gamesuite)
game_suite.pack()
root.mainloop()
