import models as mo


# mo.GameServer.get_or_create(adress_ip='192.168.32.15', nom_serveur='serveur1', game='morpion')


for a in mo.GameServer.list_serveur():
    print(a)

for a in mo.ReceiverMessage.liste_message(mo.GameServer.nom_serveur):
    print(a)
