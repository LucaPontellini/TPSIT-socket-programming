import socket

nome_server = "localhost"
porta_server = 6789

print("CLIENT: avvio della connessione...")

# creazione della socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# collegamento al server
socket_client.connect((nome_server, porta_server))
print("CLIENT: connessione stabilita con il server")

# inserimento della stringa
messaggio = input("Inserisci la stringa da inviare al server: ")

# trasformazione della stringa in byte
messaggio_bytes = messaggio.encode()

# invio dei byte al server
socket_client.sendall(messaggio_bytes)

print("CLIENT: attendo la risposta...")

# ricezione fino a 1024 byte dal server
dati_ricevuti = socket_client.recv(1024)

# trasformazione dei byte ricevuti in stringa
risposta = dati_ricevuti.decode()

# visualizzazione della risposta
print(f"Risposta dal server: {risposta}")

# chiusura della connessione
print("CLIENT: chiudo la connessione")
socket_client.close()