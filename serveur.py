# coding: utf-8
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import json
import random
import time

def Main():
    host = '127.0.0.1'
    port = 5000
    buffer_size = 2
    byte_order = 'little'

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(1)
        print("server listening at {} : {}".format(host, port))

        while True:

            (conn, addr) = sock.accept()
            print("connection reçu de {} : {}".format(*addr))
            msg = conn.recv(buffer_size)
            lenght = int.from_bytes(msg, byteorder='big')

            if lenght > 0:
                reponse = conn.recv(lenght).decode("utf_8")
                test = json.loads(reponse)
                print("le client a envoyé : {}".format(reponse))

                if test["Msg type"] == "STATS":
                    message = Stats(test)
                    messages = json.dumps(message)
                    first_bytes = len(messages).to_bytes(buffer_size, byteorder=byte_order)
                    encod = bytes(messages.encode("utf-8"))
                    full_message = first_bytes + encod
                    conn.send(full_message)
                    conn.close()

                elif test["Msg type"] == "CONFIG":
                    message = Config(test)
                    messages = json.dumps(message)
                    first_bytes = len(messages).to_bytes(buffer_size, byteorder=byte_order)
                    encod = bytes(messages.encode("utf-8"))
                    full_message = first_bytes + encod
                    conn.send(full_message)
                    conn.close()


def Stats(test):
    return {"Msg type": "ACK", "Msg ID": test["Msg ID"]}


def Config(test):
    return {
                "Msg type": "CONFIG",
                "Msg ID": test["Msg ID"],
                "Max player delay": random.randint(0, 240),
                "Max coin blink delay": random.randint(0, 240),
                "Victory blink delay": random.randint(0, 240),
                "Level": random.randint(1, 10),
                "Player1 color": random.choice(["blue", "red", "green"]),
                "Player2 color": random.choice(["blue", "red", "green"])
            }


if __name__ == '__main__':
    Main()
