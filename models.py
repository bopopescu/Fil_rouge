from peewee import *
mysql_db = MySQLDatabase('fil_rouge.db')


class BaseModel(Model):
    class Meta:
        database = mysql_db


class GameServer(BaseModel):
    adress_ip =IntegerField()
    nom_jeu = CharField()
    game = 'Morpion'


class ReceiverMessage(BaseModel):


class StatsPerMatch(BaseModel):
    machine = CharField()
    DateDeDebut = DateTimeField()
    DureePartie = TimeField()