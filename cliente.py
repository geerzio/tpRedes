import socket
import threading

# Función para recibir mensajes
def receiveMessage():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error al recibir el mensaje: {e}")
            client.close()
            break

# Función para enviar mensajes
def sendMessage():
    while True:
        message = input()
        try:
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar el mensaje: {e}")
            break

# Configuración del cliente
nickname = input("Hey elige un apodo: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 3308))  # Cambiado el puerto a 55555
    print("Conectado al servidor")

    # El servidor pide el apodo ("Nick")
    message = client.recv(1024).decode('utf-8')
    print(f"Servidor: {message}")
    client.send(nickname.encode('utf-8'))  # Enviar el apodo al servidor

except Exception as e:
    print(f"Error al conectar con el servidor: {e}")
    exit()

# Iniciar hilo para recibir mensajes
receive_thread = threading.Thread(target=receiveMessage)
receive_thread.start()

# Iniciar hilo para enviar mensajes
send_thread = threading.Thread(target=sendMessage)
send_thread.start()
