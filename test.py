import models as mo


gs1, created = mo.GameServer.get_or_create(adress_ip='192.168.32.15', nom_serveur='serveur1', game='morpion')
# mo.GameServer.get_or_create(adress_ip='192.168.32.10', nom_serveur='serveur2', game='4 en ligne')

mo.ReceiverMessage.get_or_create(msg_id=1, msg_machine=gs1, msg='lkdfsjglsdfjgdsjg')
# mo.ReceiverMessage.get_or_create(msg_id=5, msg_machine=2, msg='lgxcnvbxnbvckdfsjglsdfjgdsjg')
# mo.ReceiverMessage.get_or_create(msg_id=2, msg_machine=2, msg='lkdfsjgl,nvvn;,hvhsdfjgdsjg')
#
# mo.StatsPerMatch.get_or_create(machine_name=1, start_game='2019-03-05 08:25:00', duree=52, winner='player1')
# mo.StatsPerMatch.get_or_create(machine_name=2, start_game='2019-03-13 06:14:00', duree=35, winner='player2')
# mo.StatsPerMatch.get_or_create(machine_name=2, start_game='2019-03-13 14:53:00', duree=48, winner='player1')
# mo.StatsPerMatch.get_or_create(machine_name=1, start_game='2019-03-11 18:05:00', duree=59, winner='player1')
#
# mo.StatsPerDay.get_or_create(machine_name=1, nombre_partie=8, duree_moy_partie=54, joueur1_win=5, joueur2_win=2, egalite=1)
# mo.StatsPerDay.get_or_create(machine_name=2, nombre_partie=15, duree_moy_partie=42, joueur1_win=5, joueur2_win=8, egalite=2)
# mo.StatsPerDay.get_or_create(machine_name=1, nombre_partie=26, duree_moy_partie=32, joueur1_win=11, joueur2_win=10, egalite=5)
# mo.StatsPerDay.get_or_create(machine_name=1, nombre_partie=16, duree_moy_partie=51, joueur1_win=5, joueur2_win=5, egalite=6)


for a in mo.GameServer.list_serveur():
    print(a)

for a in mo.ReceiverMessage.liste_message(mo.GameServer.nom_serveur):
    print(a)
