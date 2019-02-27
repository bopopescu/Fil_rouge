import os
import json

partie_gen = []
stats_jour = {}


def main(partie_gen):
    for fiche in os.listdir('./partie'):
        with open('./partie/' + fiche, 'r') as fichier:
            stats = json.loads(fichier.read())
            print(stats)
            partie_gen.append(stats)
    return partie_gen


def stat_partie_jour():
    cpt = 0
    for item in partie_gen:
        if item["Start time"][:8] == item["Start time"][:8]:
            cpt += 1
    return cpt




main(partie_gen)
nombre = stat_partie_jour()
print(nombre)



