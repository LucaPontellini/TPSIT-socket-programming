import socket

# Nome e porta del server a cui il client deve inviare i datagrammi
nome_server = "localhost"
porta_server = 6789

def main():
    print("CLIENT UDP: avvio...")

    # Creazione del socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Input dell'utente
    messaggio = input("Inserisci la stringa da inviare al server: ")

    # Invia il datagramma al server
    sock.sendto(messaggio.encode(), (nome_server, porta_server))

    # Attende la risposta (bloccante)
    dati, addr = sock.recvfrom(1024)

    print(f"SERVER: {dati.decode()}")
    print("CLIENT UDP: chiudo.")

    sock.close()

if __name__ == "__main__":
    main()