from rest_framework import serializers

from stats.models import Master, Batting, Fielding, Pitching

class MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Master
        fields = '__all__'

class BattingSerializer(serializers.ModelSerializer):
    on_base_percentage = serializers.FloatField()
    batting_avg = serializers.FloatField()
    slugging_percentage = serializers.FloatField()
    stolen_base_pecentage = serializers.FloatField()
    walk_to_strikeout_ratio = serializers.FloatField()

    class Meta:
        model = Batting
        fields = '__all__'

class FieldingSerializer(serializers.ModelSerializer):
    fielding_percentage = serializers.FloatField()

    class Meta:
        model = Fielding
        fields = '__all__'

class PitchingSerializer(serializers.ModelSerializer):
    whip = serializers.FloatField()
    win_percentage = serializers.FloatField()

    class Meta:
        model = Pitching
        fields = '__all__'
