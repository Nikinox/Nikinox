# Importa il modulo 'random' per generare numeri casuali
import random

# Importa il modulo 'time' per gestire il tempo (non sarà usato direttamente con tkinter)
import time

# Importa il modulo 'tkinter' per creare l'interfaccia grafica
import tkinter as tk

# Crea una nuova finestra
root = tk.Tk()
root.title("cmd")

# Imposta dimensioni e colore di sfondo (nero)
root.geometry("1350x1200")
root.configure(bg="black")

# Crea un widget di tipo 'Text' per scrivere testo dentro la finestra
text_widget = tk.Text(root, bg="black", fg="lime", font=("Courier", 12))
text_widget.pack(expand=True, fill=tk.BOTH)

# Rende il widget non modificabile
text_widget.configure(state=tk.DISABLED)

# Funzione per aggiungere numeri casuali alla finestra
def stampa_numeri():
    # Genera una riga di 6 numeri casuali
    numeri = ' '.join(str(random.randint(0, 32767)) for _ in range(6)) + '\n'
    
    # Rendi il widget modificabile temporaneamente
    text_widget.configure(state=tk.NORMAL)
    
    # Inserisci il testo
    text_widget.insert(tk.END, numeri)
    
    # Scorri automaticamente verso il basso
    text_widget.see(tk.END)
    
    # Rendi il widget di nuovo non modificabile
    text_widget.configure(state=tk.DISABLED)
    
    # Richiama questa funzione ogni 50 millisecondi (0.05 secondi)
    root.after(35, stampa_numeri)

# Avvia la stampa dei numeri
stampa_numeri()

# Avvia il loop della finestra grafica
root.mainloop()
