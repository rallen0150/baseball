from django.contrib import admin
from stats.models import Master, Batting, Fielding, Pitching

admin.site.register([Master, Batting, Fielding, Pitching])
