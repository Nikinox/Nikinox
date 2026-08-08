import tkinter as tk
root = tk.Tk()
def count_letters():
    count_letters_wn = tk.Toplevel(root)
    count_letters_wn.geometry("500x500")
    count_letters_wn.title("COUNT LETTERS")
    instructions = tk.Label(count_letters_wn, text="Enter a word or a sentence:")
    instructions.pack()
    count_letters_bar = tk.Entry(count_letters_wn)
    count_letters_bar.pack(pady=10)
    def calculate_lenght():
        string = count_letters_bar.get()
        string_lenght = tk.Label(count_letters_wn, text=f"Lenght: {len(string)}\nLenght (without spaces): {len(string.replace(" ", ""))}", pady=50)
        string_lenght.pack()
    calculate_btn = tk.Button(count_letters_wn, text="CALCULATE LENGHT", command=calculate_lenght, bg="black", fg="white", pady=20)
    calculate_btn.pack()
    count_letters_wn.mainloop()

def home_ui():
    global root
    root.geometry("500x500")
    root.title("ANS - Anti NPC Suite")
    count_letters_btn = tk.Button(root, text="COUNT LETTERS", command=count_letters, bg="black", fg="white")
    count_letters_btn.pack()
    root.mainloop()

home_ui()
