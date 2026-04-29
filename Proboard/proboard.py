import tkinter as tk
clipboard_wn=tk.Tk()
clipboard_wn.title("Proboard: a clipboard manager - NikiSuite")
clipboard_wn.geometry("500x500")
history=[]
text=clipboard_wn.clipboard_get()
output=tk.Label(text=history)

def copy_to_clipboard(text):
    clipboard_wn.clipboard_clear()
    clipboard_wn.clipboard_append(text)

#define content
try:
    text=clipboard_wn.clipboard_get()
    if text not in history:
        history.append(text)
    output.config(text=history, cursor="hand2", command=copy_to_clipboard)
except:
    pass

output.pack()
clipboard_wn.mainloop()
