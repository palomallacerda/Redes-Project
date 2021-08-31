# Multithread Blowfish Server (MBS)

A system capable of encrypting and decrypting a message using concepts such as socket, network architecture, transport protocols, and other pertinent subjects related to Computer Networks.

## What can it do (until now)
- Encrypt a given message using blowfish technique. See more info [here](https://pycryptodome.readthedocs.io/en/latest/src/cipher/blowfish.html)
- Decrypt a given message
- Perform multithread server connection, encrypting/decrypting multiple clients messages

## How to run
1. Install the dependencies used in this project, by running the following command in your terminal:
```
    pip install -r requirements.txt
```

2. As it was built TCP-based, you need to enable the server before making new connections.

```
    python3 src/multithread_server.py
```

3. Now is up to the client (or clients), open a new terminal and have fun!
```
    python3 src/client.py
```

```
    ╔╦╦╦═╦╗╔═╦═╦══╦═╗╔══╦═╗╔═╦╗╔═╦╦╦╦═╦╦══╦╦╗
    ║║║║╦╣╚╣╠╣║║║║║╦╣╚╗╔╣║║║╣╣╚╣║║║║║╔╣╠╗╚╣═║
    ╚══╩═╩═╩═╩═╩╩╩╩═╝.╚╝╚═╝╚═╩═╩═╩══╩╝╚╩══╩╩╝
```