# coding: utf-8

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import select


def Main():
    host = '127.0.0.1'
    port = 5000
    buffer_size = 1024

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(5)
        print("server listening at {} : {}".format(host, port))
        serveur_lance = True
        clients_connectes = []

        while serveur_lance:
            connexion_demande, wlist, xlist = select.select([connexion_p], [], [], 0.05)

            for connexion in connexion_demande:
                connexion_avec_client, infos_connexion = connexion.acept()
                clients_connectes.append(connexion_avec_client)

            clients_a_lire = []

            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)

            except select.error:
                pass

            else:
                for client in clients_a_lire:
                    msg_recu = client.recv(1024)
                    # msg_recu = msg_recu.decode()
                    print("Reçu {}".format(msg_recu))
                    client.send()
                    if msg_recu == "fin":
                        serveur_lance = False

            print("Fermeture de connexions")
            for client in clients_connectes:
                client.close()

            conn.close()


if __name__ == '__main__':
    Main()


