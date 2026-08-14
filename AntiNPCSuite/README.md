# AN Suite
## Anti NPC Suite
**A collection of tools designed to stop you from doing little pointless tasks with Python**

## What it is
It's a program that contains four other little scripts inside that are inside the STALAN collection (Stop Acting Like An NPC: https://github.com/Nikinox/Nikinox/tree/main/StopActingLikeAnNPC), including:

- A tool to calculate the lenght of a word/sentence
- A tool to reverse text
- A tool to sort words (both in the alphabetic order and reversed)
- A tool to modify text making it all UPPER, lower or Title

## What remains the same
I already did another suite a while ago, the NikiSuite, the system design behind this suite is pretty much the same:

    All the programs are funcctions associated to buttons and windows that depend on the main one, meaning that if the main window closes, everything closes

<img width="908" height="308" alt="immagine" src="https://github.com/user-attachments/assets/d89db110-296e-46cd-a0a1-6091908df54e" />

## What changes
Instead of using input bars to choose options, I tried to use some sort of buttons 
that change their color and text to show the setting they're currently in.

This improves both UI and UX and reduces the possibility of input errors.

## Stack of the project
I used like in most of my projects Python 3 and its standard libraries, 
in this project I used only tkinter.

## Possible updates
A webapp version of the project, written in HTML, CSS and Javascript.

Different language versions of the app (idioms, not programming languages).
