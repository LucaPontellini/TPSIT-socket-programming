# TPSIT – Socket Programming

Python client–server implementations for TPSIT exercises using socket-based communication.

## How to run the exercises

Each exercise consists of a pair of files:

- `server_X.py`
- `client_X.py`

To run an exercise correctly:

1. Start the server first, for example:

```bash
python server_1.py
```

2. In another terminal, start the corresponding client:

```bash
python client_1.py
```

---

## Important note about communication ports

The exercises use **fixed ports** for socket communication.

This means that:

* You cannot start two servers using **the same port**, otherwise the second one will fail to start because the port is already in use.
* If you want to run **multiple exercises at the same time**, you need to change the ports in the `server/client` files so that each pair uses a different port.

### Example

```python
# server_1.py
PORT = 5000

# server_2.py
PORT = 5001
```

Make sure that:

* each **client/server pair uses the same port**
* **different ports are used for different exercises**

---

## Exercise 3 – Multithreading

In **exercise 3** the server uses **multithreading**, which means it can handle **multiple clients at the same time**.

Because of this:

- You start **only one server**.
- Then you can start **multiple clients**, even in different terminals.

### How to run

1. Start the server:

```bash
python server_3.py
````

2. Open one or more terminals and start the clients:

```bash
python client_3.py
```

You can start **as many clients as you want**.
The server will create a **separate thread for each client connection**, allowing them to communicate with the server simultaneously.