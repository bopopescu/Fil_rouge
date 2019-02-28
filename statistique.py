import os
import json

partie_gen = []
stats_jour = {}
for fiche in os.listdir('./partie'):
    with open('./partie/' + fiche, 'r') as fichier:
        stats = json.loads(fichier.read())
        print(stats)
        partie_gen.append(stats)


for elements in partie_gen:
    date = elements["Start time"][:8]
    if date in stats_jour.keys():
        stats_jour[date] += 1
    else:
        stats_jour[date] = 1
print(stats_jour)
