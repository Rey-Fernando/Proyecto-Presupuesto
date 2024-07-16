import os
import json

def run_server():
    request_fifo = '/tmp/request_fifo'
    response_fifo = '/tmp/response_fifo'

    if not os.path.exists(request_fifo):
        os.mkfifo(request_fifo)
    
    if not os.path.exists(response_fifo):
        os.mkfifo(response_fifo)

    budget = 0
    print("Servidor de presupuesto iniciado, esperando solicitudes...")

    while True:
        with open(request_fifo, 'r') as req_fifo:
            request = req_fifo.read().strip()
            if request:
                data = json.loads(request)
                action = data.get('action')
                amount = data.get('amount', 0)
                response = ""

                if action == 'update':
                    budget += amount
                    response = f"Presupuesto actualizado. Nuevo total: {budget}"
                elif action == 'query':
                    response = f"Presupuesto actual: {budget}"
                else:
                    response = "Acción no reconocida."

                with open(response_fifo, 'w') as res_fifo:
                    res_fifo.write(response)

if __name__ == "__main__":
    run_server()
