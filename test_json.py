import json
import os
import datetime
import models as mo

class Data:
    def __init__(self, json_formatted_string):
        data = json.loads(json_formatted_string)
        self.msg = json_formatted_string
        self.msg_id = data["Msg ID"]
        self.nom_serveur = mo.GameServer.get(mo.GameServer.nom_serveur == data["Machine name"])
        self.game = data["Game type"]
        self.start_game = data["Start time"]
        self.end_game = data["End time"]
        self.start_game_format = datetime.datetime.strptime(self.start_game, "%d/%m/%y %H:%M")
        self.end_game_format = datetime.datetime.strptime(self.end_game, "%d/%m/%y %H:%M")
        self.winner = data["Winner"]

    def get_day(self):

        return self.start_game_format.date()

    def get_game_duration(self):

        return (self.end_game_format-self.start_game_format).total_seconds()

    def get_winner(self):
        return self.winner


for fiche in os.listdir('./partie'):
    with open('./partie/' + fiche, 'r') as fichier:
        test = fichier.read()
        stats = Data(test)
        mo.ReceiverMessage.get_or_create(msg_id=stats.msg_id,
                                         msg_machine=stats.nom_serveur,
                                         msg=stats.msg)
        mo.StatsPerMatch.get_or_create(machine_name=stats.nom_serveur,
                                       start_game=stats.get_day(),
                                       duree=stats.get_game_duration(),
                                       winner=stats.get_winner())
        mo.StatsPerDay.get_or_create(machine_name=stats.nom_serveur,
                                     nombre_partie=8,
                                     duree_moy_partie=54,
                                     joueur1_win=5,
                                     joueur2_win=2,
                                     egalite=1)

        print(stats.get_day)
        print(stats.get_game_duration)
        print(stats.get_winner)
