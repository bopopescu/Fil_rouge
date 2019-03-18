#!/usr/bin/env python3


from socket import socket, AF_INET, SOCK_STREAM


def Main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5000
    BUFFER_SIZE = 1024
    MESSAGE = 'Hello, World!'

    server_addr = (SERVER_HOST, SERVER_PORT)

    # On crée un socket TCP
    with socket(AF_INET, SOCK_STREAM) as sock:
        print("Connecting to {}:{}...".format(SERVER_HOST, SERVER_PORT))
        sock.connect(server_addr)     # On se connecte au serveur
        print("Sending message {!r}".format(MESSAGE))
        sock.send(MESSAGE.encode())   # On lui envoie un message
        msg = sock.recv(BUFFER_SIZE)  # On récupère sa réponse
        print("Received {!r}".format(msg.decode("utf-8")))


if __name__ == '__main__':
    Main()
