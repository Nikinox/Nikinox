import tkinter as tk
gamesuite_wn=tk.Tk()
gamesuite_wn.geometry("500x500")
gamesuite_wn.title("GameSuite")

import tkinter as tk
gamesuite_wn=tk.Tk()
def tictactoe():
    tictactoe_wn=tk.Toplevel(gamesuite_wn)
    tictactoe_wn.geometry("500x500")
    tictactoe_wn.title("TIC TAC TOE")
    cells=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn=0
    btn = {"width": 5, "height": 2}
    c1=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c2=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c3=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c4=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c5=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c6=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c7=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c8=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    c9=tk.Button(tictactoe_wn, bg="blue", fg="white", **btn)
    for i in range(3):
        tictactoe_wn.grid_columnconfigure(i, weight=1, uniform="col")
        tictactoe_wn.grid_rowconfigure(i, weight=1, uniform="row")
    c1.grid(row=0, column=0, padx=10, pady=10)
    c2.grid(row=0, column=1, padx=10, pady=10)
    c3.grid(row=0, column=2, padx=10, pady=10)

    c4.grid(row=1, column=0, padx=10, pady=10)
    c5.grid(row=1, column=1, padx=10, pady=10)
    c6.grid(row=1, column=2, padx=10, pady=10)

    c7.grid(row=2, column=0, padx=10, pady=10)
    c8.grid(row=2, column=1, padx=10, pady=10)
    c9.grid(row=2, column=2, padx=10, pady=10)

    choice = tk.Entry(tictactoe_wn)
    choice.grid()
    def fill_the_cell():
        nonlocal turn
        cell=int(choice.get())
        if turn == 0:
            match cell:
                case 1:
                    if cells[0] == 0:
                        c1.config(text="X")
                        cells[0] = 2
                case 2:
                    if cells[1] == 0:
                        c2.config(text="X")
                        cells[1] = 2
                case 3:
                    if cells[2] == 0:
                        c3.config(text="X")
                        cells[2] = 2
                case 4:
                    if cells[3] == 0:
                        c4.config(text="X")
                        cells[3] = 2
                case 5:
                    if cells[4] == 0:
                        c5.config(text="X")
                        cells[4] = 2
                case 6:
                    if cells[5] == 0:
                        c6.config(text="X")
                        cells[5] = 2
                case 7:
                    if cells[6] == 0:
                        c7.config(text="X")
                        cells[6] = 2
                case 8:
                    if cells[7] == 0:
                        c8.config(text="X")
                        cells[7] = 2
                case 9:
                    if cells[8] == 0:
                        c9.config(text="X")
                        cells[8] = 2
            turn = 1
        elif turn == 1:
            match cell:
                case 1:
                    if cells[0] == 0:
                        c1.config(text="O")
                        cells[0] = 1
                case 2:
                    if cells[1] == 0:
                        c2.config(text="O")
                        cells[1] = 1
                case 3:
                    if cells[2] == 0:
                        c3.config(text="O")
                        cells[2] = 1
                case 4:
                    if cells[3] == 0:
                        c4.config(text="O")
                        cells[3] = 1
                case 5:
                    if cells[4] == 0:
                        c5.config(text="O")
                        cells[4] = 1
                case 6:
                    if cells[5] == 0:
                        c6.config(text="O")
                        cells[5] = 1
                case 7:
                    if cells[6] == 0:
                        c7.config(text="O")
                        cells[6] = 1
                case 8:
                    if cells[7] == 0:
                        c8.config(text="O")
                        cells[7] = 1
                case 9:
                    if cells[8] == 0:
                        c9.config(text="O")
                        cells[8] = 1
            turn = 0
        c1.grid()
        c2.grid()
        c3.grid()
        c4.grid()
        c5.grid()
        c6.grid()
        c7.grid()
        c8.grid()
        c9.grid()
        if cells[0]*cells[1]*cells[2]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[3]*cells[4]*cells[5]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[6]*cells[7]*cells[8]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[0]*cells[3]*cells[6]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[1]*cells[4]*cells[7]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[2]*cells[5]*cells[8]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[0]*cells[4]*cells[8]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        elif cells[2]*cells[4]*cells[6]==1:
            win=tk.Label(tictactoe_wn, text="Vittoria O")
        if cells[0]*cells[1]*cells[2]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[3]*cells[4]*cells[5]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[6]*cells[7]*cells[8]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[0]*cells[3]*cells[6]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[1]*cells[4]*cells[7]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[2]*cells[5]*cells[8]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[0]*cells[4]*cells[8]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        elif cells[2]*cells[4]*cells[6]==8:
            win=tk.Label(tictactoe_wn, text="Vittoria X")
        win.grid(row=3, column=0, columnspan=3)
    confirm = tk.Button(tictactoe_wn, text="OK", command=fill_the_cell)
    confirm.grid()
    tictactoe_wn.mainloop()

tictactoe_button=tk.Button(gamesuite_wn, text="TICTACTOE", bg="orange", fg="blue", command=tictactoe)
tictactoe_button.pack()
gamesuite_wn.mainloop()
