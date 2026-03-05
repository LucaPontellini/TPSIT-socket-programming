# TPSIT - Socket Programming

Python client–server implementations for TPSIT exercises using socket-based communication.

## Come eseguire gli esercizi

Ogni esercizio è composto da una coppia di file:

- `server_X.py`
- `client_X.py`

Per eseguire correttamente un esercizio:

1. Avvia prima il server, ad esempio:

```bash
python3 server_1.py
```

2. In un altro terminale avvia il client corrispondente:

```bash
python3 client_1.py
```

---

## Importante sulle porte di comunicazione

Gli esercizi utilizzano **porte fisse** per la comunicazione socket.

Questo significa che:

* Non puoi avviare due server che usano **la stessa porta**, altrimenti il secondo non partirà perché la porta risulta occupata.
* Se vuoi eseguire **più esercizi contemporaneamente**, devi modificare le porte nei file `server/client` in modo che ogni coppia utilizzi una porta diversa.

### Esempio

```python
# server_1.py
PORT = 5000

# server_2.py
PORT = 5001
```

Assicurati che:

* ogni **coppia client/server utilizzi la stessa porta**
* **porte diverse vengano usate tra esercizi differenti**