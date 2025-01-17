# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 19:29
from __future__ import unicode_literals

from django.db import migrations
import csv

def add_all_data(apps, schema_editor):
    Master = apps.get_model("stats", "Master")
    Batting = apps.get_model("stats", "Batting")
    Fielding = apps.get_model("stats", "Fielding")
    Pitching = apps.get_model("stats", "Pitching")

    with open('master.csv') as open_file:
        reader = csv.DictReader(open_file)
        for info in reader:
            Master.objects.create(player=info["playerID"], birth_year=info["birthYear"], birth_month=info["birthMonth"],
                                 birth_day=info["birthDay"], birth_country=info["birthCountry"], birth_state=info["birthState"],
                                 birth_city=info["birthCity"], death_year=info["deathYear"], death_month=info["deathMonth"],
                                 death_day=info["deathDay"], death_country=info["deathCountry"], death_state=info["deathState"],
                                 death_city=info["deathCity"], first_name=info["nameFirst"], last_name=info["nameLast"],
                                 given_name=info["nameGiven"], weight=info["weight"], height=info["height"], bat=info["bats"],
                                 throw=info["throws"], debut=info["debut"], last_game=info["finalGame"], retro=info["retroID"],
                                 bbref=info["bbrefID"])

                    ## FOR INTFIELDS TRY TO USE Master.objects.create(birth_year=info.get("birthYear", None))

    # raise Exception ("BOOM!")

    with open('batting.csv') as open_file:
        reader = csv.DictReader(open_file)
        for info in reader:
            player = Master.objects.get(player=info["playerID"])
            Batting.objects.create(player=player, year=info["yearID"], stint=info["stint"], team=info["teamID"], league=info["lgID"],
                                  games=info["G"], at_bats=info["AB"], runs=info["R"], hits=info["H"], doubles=info["2B"], triples=info["3B"],
                                  homeruns=info["HR"], rbi=info["RBI"], steals=info["SB"], caught=info["CS"], walk=info["BB"], strikeout=info["SO"],
                                  intentonal_walk=info["IBB"], hit_by_pitch=info["HBP"], sac_hit=info["SH"], sac_fly=info["SF"], gidp=info["GIDP"])

    # raise Exception ("2nd BOOM!")

    with open('fielding.csv') as open_file:
        reader = csv.DictReader(open_file)
        for info in reader:
            player = Master.objects.get(player=info["playerID"])
            Fielding.objects.create(player=player, year=info["yearID"], stint=info["stint"], team=info["teamID"], league=info["lgID"],
                                position=info["POS"], games=info["G"], games_started=info["GS"], innings=info["InnOuts"], put_out=info["PO"],
                                assists=info["A"], errors=info["E"], double_play=info["DP"], pass_ball=info["PB"], wild_ball=info["WP"],
                                stolen_base=info["SB"], caught_stealing=info["CS"], zone_rating=info["ZR"])
    # raise Exception ("3rd BOOM!")

    with open('pitching.csv') as open_file:
        reader = csv.DictReader(open_file)
        for info in reader:
            player = Master.objects.get(player=info["playerID"])
            Pitching.objects.create(player=player, year=info["yearID"], stint=info["stint"], team=info["teamID"], league=info["lgID"],
                                   wins=info["W"], loss=info["L"], games=info["G"], games_started=info["GS"], complete_games=info["CG"],
                                   shutout=info["SHO"], saves=info["SV"], ipouts=info["IPouts"], hits_allowed=info["H"], earned_runs=info["ER"],
                                   homeruns_allowed=info["HR"], walks=info["BB"], strikeouts=info["SO"], opp_bat_avg=info["BAOpp"],
                                   era=info["ERA"], intentonal_walk=info["IBB"], wild_pitch=info["WP"], hit_by_pitch=info["HBP"],
                                   balks=info["BK"], batters_faced=info["BFP"], games_finished=info["GF"], runs_allowed=info["R"],
                                   sac_hits_allowed=info["SH"], sac_flies_allowed=info["SF"], gidp=info["GIDP"])
    # raise Exception ("FINAL BOOM!!!!!")

class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_all_data)
    ]
