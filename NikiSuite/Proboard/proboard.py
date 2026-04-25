import tkinter as tk
clipboard_wn=tk.Tk()
clipboard_wn.title("Proboard: a clipboard manager - NikiSuite")
clipboard_wn.geometry("500x500")
history=[]
history1=clipboard_wn.clipboard_get()

#define content
try:
    history1=clipboard_wn.clipboard_get()
    history.append(history1)
    output=tk.Label(text=history)
    output.pack()
except:
    pass

clipboard_wn.mainloop()
