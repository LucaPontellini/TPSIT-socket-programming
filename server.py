import socket

class ServerTCP:
    def __init__(self):
        self.host = "127.0.0.1"
        self.porta = 6789

    def avvia(self):
        print("SERVER: avvio...")

        # creazione della socket
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associazione dell'indirizzo e della porta
        self.socket_server.bind((self.host, self.porta))

        # mettere il server in ascolto
        self.socket_server.listen()
        print("SERVER: in ascolto su", self.host, "porta", self.porta)

        # attendere un client
        connessione, indirizzo_client = self.socket_server.accept()
        print("SERVER: connesso con", indirizzo_client)

        # ricezione dei dati dal client
        dati_ricevuti = connessione.recv(1024)
        messaggio = dati_ricevuti.decode()
        print("SERVER: messaggio ricevuto:", messaggio)

        # preparazione della risposta
        risposta = "Ciao client, ho ricevuto il tuo messaggio!"
        risposta_bytes = risposta.encode()

        # invio della risposta
        connessione.sendall(risposta_bytes)

        # chiusura della connessione
        print("SERVER: chiudo la connessione")
        connessione.close()

        # chiusura del server
        self.socket_server.close()

if __name__ == "__main__":
    server = ServerTCP()
    server.avvia()