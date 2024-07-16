import os
import json
import tkinter as tk
from tkinter import messagebox

def send_request(action, amount=0):
    request_fifo = '/tmp/request_fifo'
    response_fifo = '/tmp/response_fifo'

    request = {'action': action, 'amount': amount}

    with open(request_fifo, 'w') as req_fifo:
        req_fifo.write(json.dumps(request))

    with open(response_fifo, 'r') as res_fifo:
        response = res_fifo.read().strip()

    return response

def update_budget():
    try:
        amount = int(entry_amount.get())
        response = send_request('update', amount)
        messagebox.showinfo("Respuesta del servidor", response)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

def query_budget():
    response = send_request('query')
    messagebox.showinfo("Respuesta del servidor", response)

app = tk.Tk()
app.title("Cliente de Presupuesto")

frame = tk.Frame(app)
frame.pack(pady=20, padx=20)

label_amount = tk.Label(frame, text="Cantidad:")
label_amount.grid(row=0, column=0, padx=5, pady=5)

entry_amount = tk.Entry(frame)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

button_update = tk.Button(frame, text="Actualizar Presupuesto", command=update_budget)
button_update.grid(row=1, column=0, columnspan=2, pady=5)

button_query = tk.Button(frame, text="Consultar Presupuesto", command=query_budget)
button_query.grid(row=2, column=0, columnspan=2, pady=5)

app.mainloop()
