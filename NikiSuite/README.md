Intro

This is a terminal‑based suite that runs small tools, each accessible through a specific command.
Its goal is to provide lightweight, portable utilities that automate small repetitive tasks which can be time‑consuming or tedious.
Technologies and Libraries Used

    Python

    Libraries:

        wave

        random

        struct

        string

    Walrus operator (:=) for more compact input checks

The suite is built entirely with standard libraries, with no external dependencies.

Features

You can call each tool using its dedicated command and use it as many times as you want.

The tools currently included are:

    A tool that shifts each letter to the next one in the alphabet to “encrypt” a message, and shifts letters backward to “decrypt” it

    A tool that replaces all occurrences of a chosen letter with another letter of your choice (e.g., replace all a with b)

    A tool capable of generating .wav files containing white noise, with customizable duration and file name

Creation Process

The idea came from wanting to unify several small projects from my repository into a single modular system accessible from the terminal. I started by designing a simple command‑based structure so new tools could be added without rewriting the whole suite.
During development, I encountered several technical challenges: indentation issues, input handling, using the walrus operator to simplify condition checks, and especially generating valid .wav files in the white noise generator, which required careful handling of the wave library.
The project evolved through multiple iterations until it became a stable and easily extendable suite.
What I Learned

I learned how to design systems that are more complex than standalone scripts, how to structure a command‑driven workflow, and how to manage input and errors more cleanly.
I also deepened my understanding of how the terminal works and discovered tricks to make the code more compact, such as using the walrus operator.
Possible Improvements

    Adding more tools, such as a chatbot using an API

    Implementing a graphical interface to improve user interaction
