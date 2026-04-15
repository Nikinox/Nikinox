📝 Overview

NikiText is the official text editor of the NikiSuite, designed to be lightweight, portable, and compatible with a wide range of text‑based formats.
It is not a full IDE, but a minimalist editor that allows users to open, edit, and save text and code files quickly and efficiently.

The goal is to provide an essential, understandable, and modifiable environment without external dependencies or unnecessary complexity.

✨ Features

    Open files with many different extensions (text, code, configuration)

    Create new files

    Save and Save As support

    Simple Tkinter‑based interface

    Undo/Redo, Cut/Copy/Paste

    Integrated scrollbar

    Dynamic window title updates

    Clear and extensible architecture

 Supported File Types

NikiText supports opening and saving:

    .txt

    .py

    .html, .css, .js

    .json, .xml, .yml

    .c, .cpp, .java, .cs, .kt, .swift

    .rb, .go, .php

    .ts

    .sh, .bat, .ps1

    .rs, .lua, .pl, .r

In general, any text‑based file can be opened and edited.

🧠 Architecture
1. Main Window

Handles:

    window title

    size

    menu bar

    main frame

2. Text Editor

A tk.Text widget configured with:

    readable font

    undo/redo

    custom selection colors

    vertical scrollbar

3. File Management

A global variable:
python

current_file = None

This tracks whether the user is editing a new file or an existing one.

Core functions:

    new_file()

    open_file()

    save_file()

    save_as_file()

4. Menu System

Two main menus:

    File (New, Open, Save, Save As, Exit)

    Edit (Cut, Copy, Paste, Undo, Redo)

💾 Save Logic

The Save function follows a simple rule:

    If current_file is None → behave like Save As

    If current_file contains a valid path → overwrite the file

This mirrors the behavior of traditional text editors.

🚀 Future Improvements

NikiText is intentionally simple but designed to grow.
Possible future enhancements:

    Syntax highlighting

    Line numbers

    Side file explorer

    Multiple tabs

    “Unsaved changes” confirmation popup

    Dark mode

    Custom themes

    Integration with a potential NikiShell

🛠 Requirements

    Python 3

    Tkinter (included in most Python installations)

▶️ Run

To launch NikiText:
bash

    python nikitext.py

📜 License

NikiText is part of the NikiSuite and follows an open, user‑friendly philosophy:
simple to understand, easy to modify, and free to extend.

🤝 Contributing

Contributions are welcome.
The priority is to keep the code:

    readable

    simple

    dependency‑free
