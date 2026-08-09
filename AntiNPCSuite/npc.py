import tkinter as tk
root = tk.Tk()

def count_letters():
    count_letters_wn = tk.Toplevel(root)
    count_letters_wn.geometry("500x500")
    count_letters_wn.title("COUNT LETTERS")

    instructions = tk.Label(count_letters_wn, text="Enter a word or a sentence:")
    instructions.pack()

    count_letters_bar = tk.Entry(count_letters_wn)
    count_letters_bar.pack(pady=15)

    def calculate_lenght():
        string = count_letters_bar.get()
        string_lenght = tk.Label(count_letters_wn, text=f"Lenght: {len(string)}\nLenght (without spaces): {len(string.replace(" ", ""))}", pady=50)
        string_lenght.pack()

    calculate_btn = tk.Button(count_letters_wn, text="CALCULATE LENGHT", command=calculate_lenght, bg="black", fg="white", pady=20)
    calculate_btn.pack()

    count_letters_wn.mainloop()


def reverse_txt():
    reverse_txt_wn=tk.Toplevel(root)
    reverse_txt_wn.geometry("500x500")
    reverse_txt_wn.title("REVERSE TEXT")

    instructions = tk.Label(reverse_txt_wn, text="Enter a word or a sentence to reverse:")
    instructions.pack()

    reverse_txt_bar = tk.Entry(reverse_txt_wn)
    reverse_txt_bar.pack(pady=15)

    text=""

    def reversetext():
        global text
        text=reverse_txt_bar.get()[::-1]
        reversed_text_label=tk.Label(reverse_txt_wn, text=text)
        reversed_text_label.pack(pady=50)
    
    def copy_reversed_text():
        reverse_txt_wn.clipboard_clear()
        reverse_txt_wn.clipboard_append(text)

    reverse_text_btn=tk.Button(reverse_txt_wn, text="REVERSE", command=reversetext, bg="green", fg="white")
    reverse_text_btn.pack()

    copy_btn=tk.Button(reverse_txt_wn, text="COPY REVERSED TEXT", command=copy_reversed_text, bg="black", fg="white")
    copy_btn.pack()

    reverse_txt_wn.mainloop()
    pass

def sort_words():
    sort_words_wn = tk.Toplevel(root)
    sort_words_wn.geometry("500x500")
    sort_words_wn.title("SORT WORDS")

    sort_mode = {"reverse": False}

    def toggle_sort():
        if sort_mode["reverse"]:
            sort_mode["reverse"] = False
            choice_btn.config(bg="black", fg="white", text="A → Z")
        else:
            sort_mode["reverse"] = True
            choice_btn.config(bg="white", fg="black", text="Z → A")

    choice_btn = tk.Button(
        sort_words_wn,
        text="A → Z",
        bg="black",
        fg="white",
        width=10,
        command=toggle_sort
    )
    choice_btn.pack(pady=10)

    words_label = tk.Label(sort_words_wn, text="Insert words separated by spaces:")
    words_label.pack()

    words_entry = tk.Entry(sort_words_wn, width=40)
    words_entry.pack(pady=10)

    result_label = tk.Label(sort_words_wn, text="", fg="blue")
    result_label.pack(pady=20)

    sorted_words = ""

    def execute_sort():
        words = words_entry.get().split()
        global sorted_words
        sorted_words = " ".join(sorted(words, reverse=sort_mode["reverse"]))
        result_label.config(text=sorted_words)
        def copy_sorted_words():
            global sorted_words
            sort_words_wn.clipboard_clear()
            sort_words_wn.clipboard_append(sorted_words)
        copy_btn=tk.Button(sort_words_wn, text="COPY", command=copy_sorted_words, bg="green", fg="white")
        copy_btn.pack()

    sort_button = tk.Button(
        sort_words_wn,
        text="SORT",
        bg="black",
        fg="white",
        pady=10,
        command=execute_sort
    )
    sort_button.pack()

    sort_words_wn.mainloop()

def upper_lower_title_txt():
    upper_lower_title_txt_wn = tk.Toplevel(root)
    upper_lower_title_txt_wn.geometry("500x500")
    upper_lower_title_txt_wn.title("UPPER / LOWER / TITLE TEXT")

    modes = ["UPPER", "LOWER", "TITLE"]
    mode_index = {"value": 0}  # 0 = UPPER

    def toggle_mode():
        mode_index["value"] = (mode_index["value"] + 1) % 3
        mode = modes[mode_index["value"]]

        if mode == "UPPER":
            mode_btn.config(text="UPPER", bg="black", fg="white")
        elif mode == "LOWER":
            mode_btn.config(text="LOWER", bg="white", fg="black")
        elif mode == "TITLE":
            mode_btn.config(text="TITLE", bg="gray", fg="white")

    mode_btn = tk.Button(
        upper_lower_title_txt_wn,
        text="UPPER",
        bg="black",
        fg="white",
        width=12,
        command=toggle_mode
    )
    mode_btn.pack(pady=10)

    text_entry = tk.Entry(upper_lower_title_txt_wn, width=40)
    text_entry.pack(pady=10)

    result_label = tk.Label(upper_lower_title_txt_wn, text="", fg="blue")
    result_label.pack(pady=20)

    def transform_text():
        text = text_entry.get()
        mode = modes[mode_index["value"]]

        if mode == "UPPER":
            result = text.upper()
        elif mode == "LOWER":
            result = text.lower()
        else:
            result = text.title()

        result_label.config(text=result)

    apply_btn = tk.Button(
        upper_lower_title_txt_wn,
        text="APPLY",
        bg="black",
        fg="white",
        pady=10,
        command=transform_text
    )
    apply_btn.pack()

    def copy_result():
        upper_lower_title_txt_wn.clipboard_clear()
        upper_lower_title_txt_wn.clipboard_append(result_label.cget("text"))

    copy_btn = tk.Button(
        upper_lower_title_txt_wn,
        text="COPY",
        bg="green",
        fg="white",
        pady=10,
        command=copy_result
    )
    copy_btn.pack(pady=10)

    upper_lower_title_txt_wn.mainloop()

def home_ui():
    global root
    root.geometry("500x500")
    root.title("ANS - Anti NPC Suite")

    count_letters_btn = tk.Button(root, text="COUNT LETTERS", command=count_letters, bg="black", fg="white")
    count_letters_btn.pack()

    reverse_txt_btn=tk.Button(root, text="REVERSE TEXT", command=reverse_txt, bg="black", fg="white")
    reverse_txt_btn.pack()

    sort_words_btn=tk.Button(root, text="SORT WORDS", command=sort_words, bg="black", fg="white")
    sort_words_btn.pack()

    upper_lower_title_txt_btn=tk.Button(root, text="UPPER/LOWER/TITLE TEXT", command=upper_lower_title_txt, bg="black", fg="white")
    upper_lower_title_txt_btn.pack()

    root.mainloop()

home_ui()
