import sqlite3
import os
import tkinter as tk

# === DATABASE SETUP ===

db_path = os.path.join(os.path.dirname(__file__), "pylingo.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    xp INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 0,
    last_access TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    content TEXT,
    xp INTEGER,
    exercise TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    lesson_id INTEGER,
    completed INTEGER,
    streak INTEGER
)
""")

# Crea un utente di default se non esiste
cursor.execute("SELECT id FROM users LIMIT 1")
user = cursor.fetchone()
if user is None:
    cursor.execute("INSERT INTO users (xp, streak, last_access) VALUES (0, 0, 'never')")
    conn.commit()

lessons_data = [
    {
        "title": "Variabili e Tipi di Dato",
        "content": "Il posto dove il programma ricorda le informazioni. Esistono tipi diversi: int, float, str, bool. Non puoi sommare una stringa con un numero senza convertire. In python basta scrivere il nome e assegnargli un valore o un testo con il =",
        "xp": 10,
        "exercise": "Crea tre variabili: un numero intero, un numero decimale e una stringa. Stampale tutte in una sola riga."
    },
    {
        "title": "Input e Output",
        "content": "print() e input() permettono al programma di comunicare con l'utente. Per convertire input usa str(), int() o float() attorno alla funzione input(). In print basta scrivere print(testo che vuoi stampare fra virgolette o apici) o print(nome della variabile) e per stampare un testo e una variabile si possono usare due modi, uno è scrivere print(testo fra apici+nomevariabile).",
        "xp": 10,
        "exercise": "Chiedi all’utente il suo nome e la sua età. Poi stampa una frase che li usa entrambi."
    },
    {
        "title": "Operatori e Condizioni",
        "content": "if, elif, else. Il programma prende decisioni. Importanti anche gli operatori di confronto (==, !=, >) e logici (and, or, not). Ricordati di indentare, altrimenti il programma darà un errore",
        "xp": 20,
        "exercise": "Chiedi un numero all’utente. Se è maggiore di 10 stampa 'Grande', altrimenti 'Piccolo'."
    },
    {
        "title": "Cicli",
        "content": "for e while. Servono per ripetere operazioni. Usa for quando sai quante volte ripetere, while quando dipende da una condizione.",
        "xp": 20,
        "exercise": "Stampa i numeri da 1 a 10 usando un ciclo for."
    },
    {
        "title": "Liste",
        "content": "La struttura dati più usata. Collezione ordinata di elementi. Devi saper accedere per indice, aggiungere, rimuovere e scorrere con un ciclo.",
        "xp": 30,
        "exercise": "Crea una lista di 5 numeri. Stampa solo il primo e l’ultimo elemento."
    },
    {
        "title": "Dizionari",
        "content": "Dati con un nome. Esempio: {'nome': 'Gianmaria', 'età': 14}. Fondamentali quando i dati diventano più complessi di una semplice lista.",
        "xp": 30,
        "exercise": "Crea un dizionario con nome, età e città. Poi stampa solo il valore della città."
    },
    {
        "title": "Funzioni",
        "content": "Blocchi di codice riutilizzabili con input (parametri) e output (return). Senza funzioni il codice diventa ingestibile dopo poche decine di righe.",
        "xp": 40,
        "exercise": "Scrivi una funzione che prende un numero e restituisce il numero raddoppiato."
    },
    {
        "title": "Gestione degli Errori",
        "content": "try / except. I programmi reali possono crashare. Se aspetti input dall'utente, lui troverà un modo per mandare tutto in errore.",
        "xp": 40,
        "exercise": "Chiedi un numero all’utente e prova a convertirlo in int. Se fallisce, stampa 'Errore: inserisci un numero valido'."
    },
    {
        "title": "Lettura e Scrittura di File",
        "content": "open(), .read(), .write(). Se vuoi che il programma ricordi qualcosa tra un'esecuzione e l'altra, devi salvare su file.",
        "xp": 50,
        "exercise": "Crea un file chiamato 'testo.txt' e scrivi dentro una frase a tua scelta."
    },
    {
        "title": "Moduli e Import",
        "content": "import os, import random, ecc. Python ha una libreria standard enorme. Importare moduli ti permette di usare funzionalità già pronte.",
        "xp": 50,
        "exercise": "Importa il modulo random e stampa un numero casuale tra 1 e 100."
    }
]

for lesson in lessons_data:
    cursor.execute(
        "INSERT OR IGNORE INTO lessons (title, content, xp, exercise) VALUES (?, ?, ?, ?)",
        (lesson["title"], lesson["content"], lesson["xp"], lesson["exercise"])
    )

conn.commit()

# === FUNZIONI LOGICHE ===

def get_next_lesson_id():
    cursor.execute("SELECT id FROM lessons ORDER BY id")
    all_lessons = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT lesson_id FROM progress WHERE completed = 1")
    completed = {row[0] for row in cursor.fetchall()}

    for lesson_id in all_lessons:
        if lesson_id not in completed:
            return lesson_id

    return None  # tutte completate


def open_lesson_window(lesson_id):
    cursor.execute("SELECT title, content, xp, exercise FROM lessons WHERE id = ?", (lesson_id,))
    row = cursor.fetchone()
    if row is None:
        return

    title, content, xp, exercise = row

    lesson_window = tk.Toplevel(root)
    lesson_window.title(title)
    lesson_window.geometry("400x400")

    tk.Label(lesson_window, text=title, font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(lesson_window, text=content, wraplength=350).pack(pady=10)
    tk.Label(lesson_window, text="Exercise:", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(lesson_window, text=exercise, wraplength=350).pack(pady=5)

    def complete_lesson():
        cursor.execute("SELECT completed FROM progress WHERE lesson_id = ?", (lesson_id,))
        row = cursor.fetchone()

        if row is None:
            # Prima volta → XP pieni
            cursor.execute(
                "INSERT INTO progress (user_id, lesson_id, completed, streak) VALUES (1, ?, 1, 1)",
                (lesson_id,)
            )
            cursor.execute("UPDATE users SET xp = xp + ?, streak = streak + 1 WHERE id = 1", (xp,))
        else:
            # Lezione già fatta → XP dimezzati
            cursor.execute("UPDATE users SET xp = xp + ? WHERE id = 1", (xp // 2,))

        conn.commit()
        lesson_window.destroy()

    tk.Button(lesson_window, text="Complete lesson", bg="green", fg="white", command=complete_lesson).pack(pady=20)


# === FUNZIONI UI ===

def start_lesson():
    lesson_id = get_next_lesson_id()

    if lesson_id is None:
        end_window = tk.Toplevel(root)
        end_window.title("All lessons completed")
        tk.Label(
            end_window,
            text="Perfect, now build something on your own with this knowledge",
            font=("Arial", 12),
            wraplength=350
        ).pack(pady=20)
        return

    open_lesson_window(lesson_id)


def see_progress():
    progress_window = tk.Toplevel(root)
    progress_window.title("Your Progress")
    progress_window.geometry("300x300")

    cursor.execute("SELECT xp, streak, last_access FROM users LIMIT 1")
    user_data = cursor.fetchone()

    if user_data is None:
        xp, streak, last_access = 0, 0, "never"
    else:
        xp, streak, last_access = user_data

    cursor.execute("SELECT COUNT(*) FROM progress WHERE completed = 1")
    completed_lessons = cursor.fetchone()[0]

    text = (
        f"XP: {xp}\n\n"
        f"Streak: {streak} 🔥\n\n"
        f"Last access: {last_access}\n\n"
        f"Lessons completed: {completed_lessons}"
    )

    label = tk.Label(progress_window, text=text, font=("Arial", 12))
    label.pack(pady=20)


def settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x300")
    tk.Label(settings_window, text="Settings (coming soon)", font=("Arial", 12)).pack(pady=20)


def choose_lesson():
    choose_window = tk.Toplevel(root)
    choose_window.title("Choose a lesson")
    choose_window.geometry("300x400")

    cursor.execute("SELECT id, title FROM lessons ORDER BY id")
    lessons = cursor.fetchall()

    cursor.execute("SELECT lesson_id FROM progress WHERE completed = 1")
    completed = {row[0] for row in cursor.fetchall()}

    next_lesson = get_next_lesson_id()

    for lesson_id, title in lessons:
        if lesson_id == next_lesson or lesson_id in completed:
            state = "normal"
        else:
            state = "disabled"

        def open_lesson_closure(lid=lesson_id):
            open_lesson_window(lid)

        tk.Button(choose_window, text=title, state=state, command=open_lesson_closure).pack(pady=5)


# === UI PRINCIPALE ===

root = tk.Tk()
root.title("Pylingo: learn python for free and offline")
root.geometry("500x500")

start_lesson_button = tk.Button(root, text="Start a \nnew lesson", bg="blue", fg="yellow", command=start_lesson)
start_lesson_button.pack(side="bottom", anchor="e", padx=10, pady=10)

progress_window_button = tk.Button(root, text="Your progress", command=see_progress, bg="red", fg="yellow")
progress_window_button.pack(side="top", anchor="e", padx=10, pady=10)

settings_window_button = tk.Button(root, text="Settings", command=settings, bg="black", fg="white")
settings_window_button.pack(side="top", anchor="w", padx=10, pady=10)

choose_lesson_button = tk.Button(root, text="Choose lesson", command=choose_lesson, bg="purple", fg="white")
choose_lesson_button.pack(side="bottom", anchor="w", padx=10, pady=10)

root.mainloop()

conn.close()
