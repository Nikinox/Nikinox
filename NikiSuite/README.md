📦 NikiSuite — Portable, Minimal, Useful

📝 Overview

The NikiSuite is an open‑source, fully portable collection of tools that run without installing any external Python packages.
Its main difference from other tool collections is simple:

👉 No dependencies. No installers. No bloat. Only useful tools.

Everything runs on standard Python + Tkinter, making the suite lightweight, fast, and easy to carry on any machine.

🧰 Components of the NikiSuite

As of now, the NikiSuite includes six tools:

    🔤 Text Shifter
    
    Replaces every letter in a string with either the next or previous letter in the alphabet.
    
    🔁 Letter Replacer
    
    Replaces any letter with another one you choose.
    Example: replacing all e with q in
    This project is awesome  
    produces
    This projqct is awqsomq.
    
    🔐 Password Generator
    
    Generates a random password based on the length you choose.
    
    🎧 White Noise Generator
    
    Creates a .wav white noise file.
    You choose the duration and the filename.
    
    ➗ Basic Calculator
    
    A simple calculator for quick operations.
    
    📝 Text Editor
    
    A lightweight editor that lets you:
    
        create files
    
        open files
    
        edit text or code
    
        save and save as
    
    (You cannot run code inside it — it’s intentionally minimal.)

🏗️ Architecture

🪟 Window Structure

All sub‑windows depend on the main window.
Closing the main window closes the entire suite — clean and predictable.

⚙️ Function‑Based Design

Each tool is implemented as its own function.
Buttons only call their associated function, preventing accidental cross‑execution or internal conflicts.

📦 Zero External Dependencies

The suite uses only:

    Python standard library

    Tkinter

Nothing else.

✨ Code Philosophy

short

readable

minimal

easy to understand and modify

🚀 Future Possible Upgrades

Some potential future additions:

🎮 a small collection of games

🖼️ an advanced clipboard

🔧 improvements to existing tools

❌ Things That Will NEVER Be Added

To preserve the identity of the suite:

    tools that rely on external files

    tools requiring non‑standard Python libraries

💻 Installation

Super simple:

Copy the code

Save it into a .py file

Run it

Requirements:

Python 3

Tkinter (included by default on most systems)

🤝 Contribution Guidelines

Feel free to modify or extend the suite, as long as:

    the code remains readable

    the suite does not rely on external files

    no external libraries are used beyond standard Python

📜 License

This project is released under the AGPLv3.0 license.

📚 A Bit of History

The NikiSuite started with a simple goal:

👉 Build something big, but not enormous. Useful, but not bloated.

Originally, it included only:

    the text shifter

    the letter replacer

    the white noise generator

…and everything ran in the terminal.

The name NikiSuite comes from merging the creator’s nickname Nikinox with the word Suite.
A logo does not exist yet — maybe in the future.
