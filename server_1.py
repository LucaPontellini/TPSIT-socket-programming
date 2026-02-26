import socket

host = "127.0.0.1"
porta = 6789

print("SERVER: avvio...")

# creazione della socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associazione dell'indirizzo e della porta
socket_server.bind((host, porta))

# mettere il server in ascolto
socket_server.listen()
print("SERVER: in ascolto su", host, "porta", porta)

# attendere un client
connessione, indirizzo_client = socket_server.accept()
print("SERVER: connesso con", indirizzo_client)

# ricezione dei dati dal client
dati_ricevuti = connessione.recv(1024)
messaggio = dati_ricevuti.decode()
print("SERVER: messaggio ricevuto:", messaggio)

# preparazione della risposta
risposta = "Ciao client, ho ricevuto il tuo messaggio!"
connessione.sendall(risposta.encode())

# chiusura della connessione
print("SERVER: chiudo la connessione")
connessione.close()

# chiusura del server
socket_server.close()