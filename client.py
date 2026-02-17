import socket

class ClientTCP:
    def __init__(self):
        self.nome_server = "localhost"
        self.porta_server = 6789

    def connetti(self):
        print("CLIENT: avvio della connessione...")

        # creazione della socket
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # collegamento al server
        self.socket_client.connect((self.nome_server, self.porta_server))

        print("CLIENT: connessione della stabilità con il server")

    def comunica(self):
        print("Inserisci la stringa da inviare al server:")

        # inserimento della stringa
        messaggio = input(str())

        # trasformazione della stringa in byte (passaggio obbligatorio per la socket)
        messaggio_bytes = messaggio.encode()

        # invio dei byte al server
        self.socket_client.sendall(messaggio_bytes)

        print("CLIENT: attendo la risposta...")

        # ricezione fino a 1024 byte dal server
        dati_ricevuti = self.socket_client.recv(1024)

        # trasformazione dei byte ricevuti in una stringa
        risposta = dati_ricevuti.decode()

        # visualizzazione della risposta
        print(f"Risposta dal server: {risposta}")

        # chiusura della connessione
        print("CLIENT: chiudo la connessione")
        self.socket_client.close()

if __name__ == "__main__":
    client = ClientTCP()
    client.connetti()
    client.comunica()