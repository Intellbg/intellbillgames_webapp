from django.db import models
from inventory.models import BaseProduct


class Set(BaseProduct):
    code = models.CharField(max_length=5, unique=True)
    game = models.CharField(max_length=100)
    release_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.code} {self.name}"
    
class Card(BaseProduct):
    code = models.CharField(max_length=10)
    card_set = models.ForeignKey(
        Set, related_name="cards", on_delete=models.SET_NULL, null=True
    )
    alternate_art = models.BooleanField(default=False)

    class Meta:
        abstract = True


class OnePieceGameCard(Card):
    CHARACTER = "C"
    EVENT = "E"
    STAGE = "S"
    DON = "D"
    TYPES_CHOICES = [
        (CHARACTER, "Character"),
        (EVENT, "Event"),
        (STAGE, "Stage"),
        (DON, "Don"),
    ]
    COMMON = "C"
    UNCOMMON = "UN"
    RARE = "R"
    SUPER_RARE = "SR"
    SECRET = "SEC"
    TREASURE_RARE = "TR"
    PROMO = "P"

    RARITY_CHOICES = [
        (COMMON, "Common"),
        (UNCOMMON, "Uncommon"),
        (RARE, "Rare"),
        (SUPER_RARE, "Super rare"),
        (SECRET, "Secret"),
        (TREASURE_RARE, "Treasure rare"),
        (PROMO, "Promo"),
    ]

    rotation = models.IntegerField()
    cost = models.IntegerField()
    power = models.IntegerField()
    effect = models.TextField()
    traits = models.TextField()
    type = models.CharField(max_length=1, choices=TYPES_CHOICES)
    rarity = models.CharField(max_length=5, choices=RARITY_CHOICES, null=True)

    def __str__(self):
        return f"{self.code} {self.name}"