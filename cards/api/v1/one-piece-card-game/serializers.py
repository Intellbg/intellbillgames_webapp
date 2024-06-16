from rest_framework import serializers
from cards.models import OnePieceGameCard


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnePieceGameCard
        fields = "__all__"
