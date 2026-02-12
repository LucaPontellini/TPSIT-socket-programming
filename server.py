import socket

# Configurazione del server
HOST = "127.0.0.1" # Indirizzo locale (solo il mio PC può collegarsi al server)
PORT = 5000 # Porta su cui il server rimane in ascolto

# Creazione della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET --> IPv4
    # SOCK_STREAM --> TCP (connessione affidabile)
    
    s.bind((HOST, PORT))  # Collega la socket all'indirizzo ed alla porta
    s.listen() # Mette il server in ascolto
    print("Server in ascolto su", HOST, "porta", PORT)

    conn, addr = s.accept() # Attesa di una connessione

    # Gestione della connessione con il client
    with conn:
        print("Connesso da", addr)

        # Ricezione del messaggio
        data = conn.recv(1024)  # Riceve fino a 1024 byte
        print("Messaggio ricevuto:", data.decode())  # Decodifica i byte in stringa

        # Risposta al client
        conn.sendall(b"Ciao client, ho ricevuto il tuo messaggio!")