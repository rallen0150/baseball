from django.db import models

# Create your models here.

class Master(models.Model):
    player = models.CharField(max_length=10, blank=True)
    birth_year = models.CharField(max_length=50, blank=True, null=True)
    birth_month = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.CharField(max_length=50, blank=True, null=True)
    birth_country = models.CharField(max_length=50, blank=True)
    birth_state = models.CharField(max_length=50, blank=True)
    birth_city = models.CharField(max_length=50, blank=True)
    death_year = models.CharField(max_length=50, blank=True, null=True)
    death_month = models.CharField(max_length=50, blank=True, null=True)
    death_day = models.CharField(max_length=50, blank=True, null=True)
    death_country = models.CharField(max_length=50, blank=True)
    death_state = models.CharField(max_length=50, blank=True)
    death_city = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    given_name = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    bat = models.CharField(max_length=1, blank=True)
    throw = models.CharField(max_length=1, blank=True)
    debut = models.CharField(max_length=10, blank=True)
    last_game = models.CharField(max_length=10, blank=True)
    retro = models.CharField(max_length=10, blank=True)
    bbref = models.CharField(max_length=10, blank=True)

class Batting(models.Model):
    player = models.ForeignKey(Master)
    year = models.CharField(max_length=50, blank=True, null=True)
    stint = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    league = models.CharField(max_length=2, blank=True)
    games = models.CharField(max_length=50, blank=True, null=True)
    at_bats = models.CharField(max_length=50, blank=True, null=True)
    runs = models.CharField(max_length=50, blank=True, null=True)
    hits = models.CharField(max_length=50, blank=True, null=True)
    doubles = models.CharField(max_length=50, blank=True, null=True)
    triples = models.CharField(max_length=50, blank=True, null=True)
    homeruns = models.CharField(max_length=50, blank=True, null=True)
    rbi = models.CharField(max_length=50, blank=True, null=True)
    steals = models.CharField(max_length=50, blank=True, null=True)
    caught = models.CharField(max_length=50, blank=True, null=True)
    walk = models.CharField(max_length=50, blank=True, null=True)
    strikeout = models.CharField(max_length=50, blank=True, null=True)
    intentonal_walk = models.CharField(max_length=50, blank=True, null=True)
    hit_by_pitch = models.CharField(max_length=50, blank=True, null=True)
    sac_hit = models.CharField(max_length=50, blank=True, null=True)
    sac_fly = models.CharField(max_length=50, blank=True, null=True)
    gidp = models.CharField(max_length=50, blank=True, null=True)


    @property
    def on_base_percentage(self):
        return round((int(self.hits.replace('', '0'))+int(self.walk.replace('', '0'))+int(self.hit_by_pitch.replace('', '0'))+int(self.intentonal_walk.replace('', '0')))/
                (int(self.at_bats.replace('', '0'))+int(self.walk.replace('', '0'))+int(self.hit_by_pitch.replace('', '0'))+int(self.sac_fly.replace('', '0'))), 3)

    @property
    def batting_avg(self):
        return round((int(self.hits)/int(self.at_bats)), 3)


class Fielding(models.Model):
    player = models.ForeignKey(Master)
    year = models.CharField(max_length=50, blank=True, null=True)
    stint = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=10, blank=True)
    league = models.CharField(max_length=2, blank=True)
    position = models.CharField(max_length=3, blank=True)
    games = models.CharField(max_length=50, blank=True, null=True)
    games_started = models.CharField(max_length=50, blank=True, null=True)
    innings = models.CharField(max_length=50, blank=True, null=True)
    put_out = models.CharField(max_length=50, blank=True, null=True)
    assists = models.CharField(max_length=50, blank=True, null=True)
    errors = models.CharField(max_length=50, blank=True, null=True)
    double_play = models.CharField(max_length=50, blank=True, null=True)
    pass_ball = models.CharField(max_length=50, blank=True, null=True)
    wild_ball = models.CharField(max_length=50, blank=True, null=True)
    stolen_base = models.CharField(max_length=50, blank=True, null=True)
    caught_stealing = models.CharField(max_length=50, blank=True, null=True)
    zone_rating = models.CharField(max_length=50, blank=True, null=True)

class Pitching(models.Model):
    player = models.ForeignKey(Master)
    year = models.CharField(max_length=50, blank=True, null=True)
    stint = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=10, blank=True)
    league = models.CharField(max_length=2, blank=True)
    wins = models.CharField(max_length=50, blank=True, null=True)
    loss = models.CharField(max_length=50, blank=True, null=True)
    games = models.CharField(max_length=50, blank=True, null=True)
    games_started = models.CharField(max_length=50, blank=True, null=True)
    complete_games = models.CharField(max_length=50, blank=True, null=True)
    shutout = models.CharField(max_length=50, blank=True, null=True)
    saves = models.CharField(max_length=50, blank=True, null=True)
    ipouts = models.CharField(max_length=50, blank=True, null=True)
    hits_allowed = models.CharField(max_length=50, blank=True, null=True)
    earned_runs = models.CharField(max_length=50, blank=True, null=True)
    homeruns_allowed = models.CharField(max_length=50, blank=True, null=True)
    walks = models.CharField(max_length=50, blank=True, null=True)
    strikeouts = models.CharField(max_length=50, blank=True, null=True)
    opp_bat_avg = models.CharField(max_length=50, blank=True, null=True)
    era = models.CharField(max_length=50, blank=True, null=True)
    intentonal_walk = models.CharField(max_length=50, blank=True, null=True)
    wild_pitch = models.CharField(max_length=50, blank=True, null=True)
    hit_by_pitch = models.CharField(max_length=50, blank=True, null=True)
    balks = models.CharField(max_length=50, blank=True, null=True)
    batters_faced = models.CharField(max_length=50, blank=True, null=True)
    games_finished = models.CharField(max_length=50, blank=True, null=True)
    runs_allowed = models.CharField(max_length=50, blank=True, null=True)
    sac_hits_allowed = models.CharField(max_length=50, blank=True, null=True)
    sac_flies_allowed = models.CharField(max_length=50, blank=True, null=True)
    gidp = models.CharField(max_length=50, blank=True, null=True)

    @property
    def whip(self):
        return round((int(self.walks.replace('', '0'))+int(self.intentonal_walk.replace('', '0'))+int(self.hits_allowed.replace('', '0')))/
                      float(self.ipouts.replace('', '0')), 3)
