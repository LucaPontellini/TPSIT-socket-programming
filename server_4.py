import socket

# Indirizzo e porta su cui il server rimane in ascolto
nome_server = "localhost"
porta_server = 6789

print("SERVER UDP: avvio...")

# Creazione del socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Associazione del socket all'indirizzo e porta
server_socket.bind((nome_server, porta_server))

print(f"SERVER UDP: in ascolto su {nome_server}:{porta_server}\n")

# Ciclo infinito: riceve datagrammi e risponde
while True:
    # recvfrom restituisce i dati e l'indirizzo del mittente
    dati, addr = server_socket.recvfrom(1024)
    messaggio = dati.decode()

    print(f"SERVER UDP: messaggio da {addr}: {messaggio}")

    risposta = f"Ho ricevuto: {messaggio}"
    server_socket.sendto(risposta.encode(), addr)