import socket

# Nome e porta del server a cui il client deve connettersi
nome_server = "localhost"
porta_server = 6789

def main():
    print("CLIENT: avvio della connessione...")

    # Creazione del socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connessione al server
    sock.connect((nome_server, porta_server))
    print(f"CLIENT: connessione stabilita con {nome_server}:{porta_server}\n")

    # Input dell'utente
    messaggio = input("Inserisci la stringa da inviare al server: ")

    # Invia il messaggio al server
    sock.sendall(messaggio.encode())

    # Attende la risposta del server (bloccante)
    dati = sock.recv(1024)

    # Stampa la risposta ricevuta
    print(f"SERVER: {dati.decode()}")

    # Chiude la connessione dopo aver ricevuto la risposta
    print("CLIENT: chiudo la connessione.")
    sock.close()

if __name__ == "__main__":
    main()