import tkinter as tk
from tkinter import filedialog

txt_window = tk.Tk()
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
