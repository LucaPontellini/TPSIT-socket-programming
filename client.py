import socket

# Configurazione del client
HOST = "127.0.0.1"  # Indirizzo del server (localhost)
PORT = 5000 # Porta su cui il server sta ascoltando

# Creazione della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET --> IPv4
    # SOCK_STREAM --> TCP (connessione affidabile)

    s.connect((HOST, PORT))  # Connessione al server
    s.sendall(b"Ciao server!")  # Invio del messaggio al server

    data = s.recv(1024)  # Attesa della risposta del server

print("Risposta dal server:", data.decode()) # Visualizzazione della risposta