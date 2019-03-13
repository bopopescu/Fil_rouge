import os
import json

partie_gen = []
stats_jour = {}


def get_games():
    for fiche in os.listdir('./partie'):
        with open('./partie/' + fiche, 'r') as fichier:
            stats = json.loads(fichier.read())
            partie_gen.append(stats)


def stats_partie_jour():
    for elements in partie_gen:
        date = elements["Start time"][:8]
        if date in stats_jour.keys():
            stats_jour[date] += 1
        else:
            stats_jour[date] = 1


def temp_moyen():
    cumul_temp = 0
    for elements in partie_gen:
        debut_heure = elements["Start time"][9:11]
        debut_min = elements["Start time"][12:14]
        fin_heure = elements["End time"][9:11]
        fin_min = elements["End time"][12:14]
        if debut_heure == fin_heure:
            temp_partie = int(fin_min) - int(debut_min)
            cumul_temp += temp_partie
        else:
            temp_partie = (int(fin_min) + 60) - int(debut_min)
            cumul_temp += temp_partie
    moyenne = cumul_temp/len(partie_gen)
    stats_jour['temp_moyen'] = moyenne


def meilleur_joueur():
    joueur1 = 0
    joueur2 = 0
    for elements in partie_gen:
        if elements["Winner"] == "player1":
            joueur1 += 1
        else:
            joueur2 += 1
    if joueur1 > joueur2:
        stats_jour['winner'] = 'joueur1'
    else:
        stats_jour['winner'] = 'joueur2'


get_games()
stats_partie_jour()
temp_moyen()
meilleur_joueur()
print(stats_jour)
print(partie_gen)
