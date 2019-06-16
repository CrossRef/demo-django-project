from random import randint
from prometheus_client import Counter, Gauge


CRITTER_ACTIVATION_COUNT = Counter(
    "critter_activation_count", "Total count of critter activations"
)
CRITTER_MOOD = Gauge("critter_mood", "Current mood of the critter")


class Critter:
    def activate(self):
        CRITTER_ACTIVATION_COUNT.inc()
        return True

    def update_critter_mood(self):
        CRITTER_MOOD.set(randint(0, 99))
        return True

