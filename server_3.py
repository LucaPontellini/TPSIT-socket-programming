import socket
import threading

# Indirizzo e porta su cui il server rimane in ascolto
nome_server = "localhost"
porta_server = 6789

def gestisci_client(conn, addr):
    print(f"SERVER: connesso con {addr}")

    try:
        # Riceve un solo messaggio dal client (bloccante)
        dati = conn.recv(1024)

        # Se il client chiude senza inviare nulla
        if not dati:
            print(f"SERVER: {addr} si è disconnesso.")
            conn.close()
            return

        # Decodifica del messaggio ricevuto
        messaggio = dati.decode()
        print(f"SERVER: messaggio da {addr}: {messaggio}")

        # Prepara la risposta
        risposta = f"Ho ricevuto: {messaggio}"

        # Invia la risposta al client
        conn.sendall(risposta.encode())

        print(f"SERVER: chiudo la connessione con {addr}\n")

    except ConnectionResetError:
        # Il client ha chiuso la connessione in modo anomalo
        print(f"SERVER: connessione persa con {addr}")

    # Chiusura della connessione con il client
    conn.close()


print("SERVER: avvio...")

# Creazione del socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associazione del socket all'indirizzo e porta
server_socket.bind((nome_server, porta_server))

# Il server si mette in ascolto di nuove connessioni
server_socket.listen()
print(f"SERVER: in ascolto su {nome_server}:{porta_server}\n")

# Ciclo infinito: accetta nuovi client e crea un thread per ciascuno
while True:
    conn, addr = server_socket.accept()
    print(f"SERVER: nuova connessione da {addr}")

    # Creazione del thread dedicato al client
    thread = threading.Thread(target=gestisci_client, args=(conn, addr), daemon=True)
    thread.start()