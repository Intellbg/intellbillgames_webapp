from django.db import models


def img_path(instance, filename):
    return f"cards/{instance.set.game}/{instance.set.code}/{instance.name}"


class Set(models.Model):
    code = models.CharField(max_length=5,unique=True)
    game = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    release_date = models.DateField(null=True)


class Card(models.Model):
    code = models.CharField(max_length=10)
    set = models.ForeignKey(
        Set, related_name="cards", on_delete=models.SET_NULL, null=True
    )
    price = models.DecimalField(decimal_places=2, max_digits=6)

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

    name = models.CharField(max_length=200)
    rotation = models.IntegerField()
    cost = models.IntegerField()
    power = models.IntegerField()
    effect = models.TextField()
    traits = models.TextField()
    type = models.CharField(max_length=1, choices=TYPES_CHOICES)
    rarity = models.CharField(max_length=5, choices=RARITY_CHOICES, null=True)
    imagen = models.ImageField(upload_to=img_path, null=True)
