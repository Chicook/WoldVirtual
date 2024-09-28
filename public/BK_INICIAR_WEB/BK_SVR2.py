import socket
import requests
import json

# Arreglar mas adelante.,

# import psutil

"""
def get_processor_info():
    cpu_info = {
        'physical_cores': psutil.cpu_count(logical=False),
        'total_cores': psutil.cpu_count(logical=True),
        'max_frequency': psutil.cpu_freq().max,
        'min_frequency': psutil.cpu_freq().min,
        'current_frequency': psutil.cpu_freq().current,
        'cpu_usage': psutil.cpu_percent(interval=1)
    }
    return cpu_info
    
              #Dirección del servidor Flask
               #server_ip = '127.0.0.1'

def send_http_message():
    url = f'http://{server_ip}:5000/mensaje'
    data = {'mensaje': 'Hola desde el cliente'}
    response = requests.post(url, json=data)
    print(f"Respuesta del servidor (HTTP): {response.text}")
    
    def send_transaction(sender, recipient, amount):
    transaction_url = f'http://{server_ip}:5000/transactions/new'
    transaction_data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    response = requests.post(transaction_url, json=transaction_data)
    print(f"Respuesta del servidor (Transacción): {response.text}")
    
def send_socket_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 8080))
    client_socket.send("Hola desde el cliente".encode())
    response = client_socket.recv(1024).decode()
    print(f"Respuesta del servidor (Socket): {response}")
    client_socket.close()

# Obtener información del procesador
processor_info = get_processor_info()
print(f"Información del procesador: {processor_info}")

# Enviar un mensaje HTTP
send_http_message()

# Enviar una transacción a la blockchain
send_transaction('cliente', 'servidor', 10)

# Enviar un mensaje a través de sockets
send_socket_message()

"""
# Dirección del servidor Flask
server_ip = '192.168.1.10'

# Función para enviar un mensaje HTTP
def send_http_message():
    url = f'http://{server_ip}:5000/mensaje'
    data = {'mensaje': 'Compartiendo Recursos correctamente'}
    response = requests.post(url, json=data)
    print(f"Respuesta del servidor (HTTP): {response.text}")

# Función para enviar una transacción a la blockchain
def send_transaction(sender, recipient, amount):
    transaction_url = f'http://{server_ip}:5000/transactions/new'
    transaction_data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    response = requests.post(transaction_url, json=transaction_data)
    print(f"Respuesta del servidor (Transacción): {response.text}")

# Función para comunicarse a través de sockets
def send_socket_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 8080))
    client_socket.send("bloque creado con exito compartiendo Recurso".encode())
    response = client_socket.recv(1024).decode()
    print(f"Respuesta del servidor (Socket): {response}")
    client_socket.close()

# Enviar un mensaje HTTP
send_http_message()

# Enviar una transacción a la blockchain
send_transaction('cliente', 'servidor', 10)

# Enviar un mensaje a través de sockets
send_socket_message()
