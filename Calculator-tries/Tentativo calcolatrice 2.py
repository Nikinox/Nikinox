import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    caluclation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")# Qui andrebbe il codice per pulire il campo

root = tk.Tk()
root.geometry("600x300")

text_result= tk.Text(root, height=2, width=34, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1=tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=10, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2=tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=10, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3=tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=10, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4=tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=10, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5=tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=10, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6=tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=10, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7=tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=10, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8=tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=10, font=("Arial", 14))
btn_8.grid(row=3, column=2)
btn_9=tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=10, font=("Arial", 14))
btn_9.grid(row=3, column=3)
btn_0=tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=10, font=("Arial", 14))
btn_0.grid(row=4, column=2)

root.mainloop()


#min= 12.27 urL: https://www.youtube.com/watch?v=NzSCNjn4_RI
